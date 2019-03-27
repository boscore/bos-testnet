#!/usr/bin/env python
# -*- coding:utf-8 -*-
import threading
import time
import requests
import logging
import json
import sys
import inspect
import traceback

from itertools import cycle

global flag
flag = True  # flag = true为切到主了，false 为已经切换了备


def log(message):
    caller_info = inspect.stack()[1]
    print("[%s %s %d] %s" % (time.strftime("%Y-%m-%d %H:%M:%S"), caller_info[3], caller_info[2], message))


class MainProcess(object):
    """
     used to check the status of bp nodes,can be configured more than two nodes
     automatically switch to the healthy node
     notify the action by telegram
    """

    def __init__(self, slavers, **kwargs):
        self.api_version = kwargs.get('api_version', 'v1')
        self.max_retries = kwargs.get('max_retries', 2)
        print(slavers)
        self.slavers = cycle(self._nodes(slavers))
        self.url = ''
        self.next_bp()

    def next_bp(self):
        self.set_bp(next(self.slavers))

    def set_bp(self, url):
        self.url = url

    @staticmethod
    def _nodes(slavers):
        return [x for x in slavers]

    """select the available slave node """

    def select_node(self, _count=0):
        slave_node = self.url
        log(f"try to make connection with slave node {slave_node}...")
        slave_info_url = f"{slave_node}/{self.api_version}/chain/get_info"
        try:
            result = requests.get(slave_info_url, timeout=3.0)
        except (requests.exceptions.ConnectionError,
                requests.exceptions.HTTPError) as e:
            log("beg in to find next available node due to exception :%s" % e)
            self.next_bp()
            print("next bp is %s" % (self.url))
            return self.select_node(_count=_count + 1)
        except Exception as e:
            raise e
        else:
            return slave_node
        return None

    def pause(self, url):
        url = f"{url}/{self.api_version}/producer/pause"
        try:
            pause_action = requests.request("POST", url)
            # self.notify_users("pause bp success", conf_dict)
        except Exception as e:
            msg = "pause bp failed due to %s" % e.__class__.__name__
            # self.notify_users(msg, conf_dict)

    def resume(self, url):
        url = f"{url}/{self.api_version}/producer/resume"
        try:
            resume_action = requests.request("POST", url)
            # self.notify_users("resume bp success",conf_dict)
        except Exception as e:
            msg = "resume bp failed due to %s" % e.__class__.__name__
            # self.notify_users(msg, conf_dict)

    # Send Telegram Bot
    @staticmethod
    def notify_users(msg, conf_dict):
        conf_dict = conf_dict
        try:
            url = "https://api.telegram.org/bot%s/sendMessage" % (conf_dict["telegram"]["token"])
            param = {"chat_id": conf_dict["telegram"]["chat_id"], "text": msg, }
            result = requests.post(url, param, timeout=5.0)
            print("telegram_alarm send message:%s %s", msg, result.text)
        except Exception as e:
            print('send_telegram_msg get exception:%s ' % e)
            print(traceback.print_exc())


"""
check the health of node, select one of the slaves as  backup node
"""
STATUS = {}


def check_node(node):
    global STATUS
    node = node
    k = "%s" % node
    if k not in STATUS:
        STATUS[k] = {'head_block_num': 10, 'last_irreversible_block_num': 0}
    try:
        url = "%s/v1/chain/get_info" % (node)
        print(f"check node:{url}")
        result = requests.get(url, timeout=3.0)
        if result.status_code / 100 != 2:
            logging.info('Failed to connect with node %s' % url)
            return False
        result_info = json.loads(result.text)
        # print("%s %s" % (time.strftime("%Y-%m-%d %H:%M:%S"), result_info))
        # print("STATUS-%s-%s" % (time.strftime("%Y-%m-%d %H:%M:%S"), STATUS))
        if result_info["head_block_num"] >= STATUS[k]['head_block_num'] and \
                result_info["last_irreversible_block_num"] >= STATUS[k]['last_irreversible_block_num']:
            return True
        STATUS[k]['head_block_num'], STATUS[k]['last_irreversible_block_num'] = result_info["head_block_num"], result_info["last_irreversible_block_num"]
    except Exception as e:
        return False
        logging.info("Get exception:%s" % e)


con = threading.Condition()


def fun1():
    global flag
    global master_status
    while True:
        master_status = check_node(g_master_bp)
        print("check the status of bp master...")
        if con.acquire():
            if not master_status and flag:
                print("begin to switch to slave")
                con.wait()
                con.notify()
            elif not master_status and not flag:
                print("dont need to switch to master,beacause master has not recovered!")
            elif master_status and not flag:
                print("switch back to the master")
                con.notify()
                con.wait()
            elif master_status and flag:
                print("master bp is ok")
            con.release()


def fun2():
    global flag
    global master_status
    global selected_node

    while True:
        master_status = check_node(g_master_bp)

        if con.acquire():
            if not master_status and flag:
                print("begin to switch to slave")
                selected_node = h.select_node()
                h.resume(selected_node)  # switch the selected node
                flag = False
                con.wait()
                con.notify()
            elif master_status and not flag:
                msg = "master bp is ok ,try to switch back to master"
                print(msg)
                # pause the slave node
                h.pause(selected_node)

                # resume the master node
                h.resume(g_master_bp)

                flag = True
                con.wait()
                con.notify()
            con.release()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: %s bp.conf' % (sys.argv[0]))
        sys.exit(1)
    conf_dict = {}
    with open(sys.argv[1], "r") as fp:
        conf_dict = json.loads(fp.read())

    if not conf_dict:
        print("ERROR: bp.json can not be empty: %s" % (sys.argvp[1]))
        sys.exit(1)
    global g_master_bp
    g_master_bp = conf_dict['master']

    slavers = conf_dict['slaver']
    h = MainProcess(slavers)
    # select_node=h.select_node()
    # print(f"selected_slave: {select_node}")

    threading.Thread(target=fun1).start()
    threading.Thread(target=fun2).start()
    global master_status