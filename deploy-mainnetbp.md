# 如何搭建BOS主网的bp节点

- [English](deploy-mainnetbp-EN.md)
- [中文](deploy-mainnetbp.md)

### 操作步骤跟测试网搭建相同，需要修改bpnode/config文件夹下面的config.ini文件和genesis.json文件

[测试网节点搭建步骤](https://github.com/boscore/bos-testnet/blob/master/README.md)

- 在config中需要操作：替换p2p-peer-address、修改signature-provider、producer-name

使用的p2p-peer-address如下：
```
p2p-peer-address = peer.bos.alohaeos.com:9876
p2p-peer-address = bos.atticlab.net:10987
p2p-peer-address = peer01-bos.blockzone.net:543
p2p-peer-address = peer02-bos.blockzone.net:543
p2p-peer-address = p2p-bos.eosbeijing.one:6001
p2p-peer-address = bosp2p.eoscafeblock.com:9070
p2p-peer-address = bos.eosn.io:9876
p2p-peer-address = p2p.bos.nodepacific.com:9876
p2p-peer-address = peer1-bos.eosphere.io:9876
p2p-peer-address = p2p.bos.eosrio.io:9876
p2p-peer-address = api.bos.eostribe.io:9310
p2p-peer-address = bos.cryptolions.io:1987
p2p-peer-address = bos.csx.io:9876
p2p-peer-address = peering.bos.dapp.pub:9876
p2p-peer-address = peering.bos.eoscanada.com:9876
p2p-peer-address = p2p.hellobos.one:9876
p2p-peer-address = bos.tokenpocket.pro:9376
p2p-peer-address = bos-peer.slowmist.io:19876

```
最新接入点请参考工具: [eosnation节点统计工具](https://validate.eosnation.io/bos/reports/endpoints.html)


- [genesis.json](https://github.com/boscore/bosres/blob/master/genesis.json)


### 用快照启动BOS节点

- 优点
  1. 快速同步节点
  使用最新快照启动的节点，能够在 3~4 分钟内完成节点同步达到主网高度，时间成本大大降低。
  
  2. 节省服务器资源
  使用快照方式启动的节点，block.log内只会保存节点启动之后的数据，占用的磁盘空间更小。并且用快照启动的 CPU 和 RAM 的使用上都要远远小于全节点。大大降低服务器成本。

- 缺点
  由于是保存节点启动之后的数据，账户交易的history在之前的无法查到。


启动的时候在docker-compose-bostest.yaml文件中增加```--snapshot=xxxx```,例如：
```
version: "3"

services:
  nodeosd:
    image: boscore/bos:latest
    command: /opt/eosio/bin/nodeos --data-dir=/data --config-dir=/etc/nodeos --snapshot=/data/snapshots/snapshot-0000001b3311bc919360c885a554366598feee03a99f1da7244ed8904ce562e0.bin
    hostname: nodeosd
    ports:
      - 8890:8888
      - 9878:9876
    expose:
      - "8888"
    volumes:
      - /data/eos/nodeos-data-volume/nodeos-data-bostest/config:/etc/nodeos
      - /data/eos/nodeos-data-volume/nodeos-data-bostest/data:/data
```

bos主网的快照:[下载地址与说明文档](https://eosnode.tools/snapshots/bos)
