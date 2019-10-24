## 请进电报：
https://t.me/BOSTestnet

BOS Tesnet监控地址：
https://t.me/bosteststatus 

BOS Testnet 浏览器:
- https://bos-test.bloks.io/
- https://bos-test.eosx.io/
- https://local.bloks.io/?nodeUrl=bos-test.eospacex.com&coreSymbol=BOS
  

[View in English](README.md)

## docker images 
You should update the last version from https://hub.docker.com/r/boscore/bos/tags/

### 克隆项目

```
git clone https://github.com/boscore/bos-testnet.git
cd fullnode
```
fullnode 和 bpnode的主要区别是bpnode 的config中增加了producer_plugin插件用来出块。
### 5秒之内搭建一个全节点

```
cd bos-testnet/
./run.sh
```

### 1分钟内手动搭建全节点

第一步，创建所需要的目录:

```
mkdir -p /data/eos/nodeos-data-volume/nodeos-data-bostest/data
```

第二步，准备配置文件:

```
cp -r config /data/eos/nodeos-data-volume/nodeos-data-bostest
```

第三步，启动全节点

```
docker-compose -f docker-compose-bostest-init.yaml up -d
```

### 暂停/重启 同步

暂停:

```
docker-compose -f docker-compose-bostest.yaml down
```

重启:

```
docker-compose -f docker-compose-bostest.yaml down
docker-compose -f docker-compose-bostest.yaml up -d
```

# 在BOS主网部署操作是一样的，修改一些内容.[详情](https://github.com/boscore/bos-testnet/blob/master/deploy-mainnetbp.md)

## 链信息

```
"chain_id": "33cc2426f1b258ef8c798c34c0360b31732ea27a2d7e35a65797850a86d1ba85"

```

## P2P 节点列表

```
p2p-peer-address = 47.90.101.71:443
p2p-peer-address = 52.69.198.164:9003
p2p-peer-address = 34.80.177.78:9876
p2p-peer-address = 52.69.198.164:9003
p2p-peer-address = br.eosrio.io:29876
p2p-peer-address = bos-test.eosdac.io:39877
p2p-peer-address = 47.88.155.76:9877
p2p-peer-address = bostestnet.eoscafeblock.com:9877
p2p-peer-address = test-bos.atticlab.net:10876
p2p-peer-address = peer01-bostest.blockzone.net:543
p2p-peer-address = peer02-bostest.blockzone.net:543
p2p-peer-address = peer.bostest.alohaeos.com:9876
p2p-peer-address = bos-test.eoshenzhen.io:9876
p2p-peer-address = bos-testnet.eosamsterdam.xeos.me:9899
p2p-peer-address = bos-test.eosdac.io:39877
```


## HTTP API 节点列表

API nodes:
```
https://api-bostest.blockzone.net/v1/chain/get_info
https://bos-testnet.eosphere.io/v1/chain/get_info
https://boscore.eosrio.io/v1/chain/get_info
https://api.bostest.alohaeos.com/v1/chain/get_info
http://bos-test.eoshenzhen.io:8888/v1/chain/get_info
```

支持 `get actions` ( filter-on=* ) 的API:
```
https://api-bostest.blockzone.net
https://boscore.eosrio.io/v1/history/ (MongoDB based)
https://bos-test.keosd.io/v1/history/ (MongoDB based)
```

State History Support:

```
http://sh-bostest.eoshenzhen.io:8088
```


## 水龙头

在 `bos` 上创建账号非常简单:

#### 免费账号
创建免费账号: https://faucet-bos-testnet.keosd.io/create/<new_account>.

例子:
```
curl https://faucet-bos-testnet.keosd.io/create/111111111ooo
```

#### 获得免费Token
获得免费Token: https://faucet-bos-testnet.keosd.io/get_token/<your_account_name>. 

每一次调用能获得100EOS, 每天最多获得1000个EOS.

例子:
``` 
curl https://faucet-bos-testnet.keosd.io/get_token/111111111ooo
```






