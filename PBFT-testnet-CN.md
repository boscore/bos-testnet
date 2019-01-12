欢迎来到 bos-testnet

[View in English](PBFT-testnet.md)

## docker images 
You should update the last version from https://hub.docker.com/r/boscore/boslib/tags

### 克隆项目

```
git clone https://github.com/boscore/bos-testnet.git
git checkout lib-test
cd fullnode
```
fullnode 和 bpnode的主要区别是bpnode 的config中增加了producer_plugin插件用来出块。
### 5秒之内搭建一个全节点

```
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
## 链信息

```
"chain_id": "514cb0a66d3f60fd213dea0c9fd1a30b4405e3375599c40efd597c089b832118"

```

## P2P 节点列表

```
p2p-peer-address = 13.230.195.142:9871
p2p-peer-address =  52.194.161.6:9877 
p2p-peer-address = 13.230.195.142:9872 
p2p-peer-address = 47.244.41.129:448
p2p-peer-address = 47.244.42.171:548
p2p-peer-address = 47.91.244.124:448
p2p-peer-address = 47.254.82.241:448
p2p-peer-address = 54.197.4.64:9006
p2p-peer-address = 3.84.104.121:9007
p2p-peer-address = 13.231.97.118:9002
p2p-peer-address = 45.79.145.205:8849
p2p-peer-address = 139.162.61.239:8849
p2p-peer-address = 45.79.145.205:9111
p2p-peer-address = 139.162.61.239:9111
```


## HTTP API 节点列表

API nodes:
```
http://52.194.161.6:9999/v1/chain/get_info 
http://139.162.61.239:8111/v1/chain/get_info

```

支持 `get actions` ( filter-on=* ) 的API:
```

```

## 水龙头

在 `bos` 上创建账号非常简单:

#### 免费账号
创建免费账号: https://faucet-bos-lib-testnet.keosd.io/create/"account-name"

例子:
```
curl https://faucet-bos-lib-testnet.keosd.io/create/bosaccount11
```

#### 获得免费Token
获得免费Token: https://faucet-bos-lib-testnet.keosd.io/get_token/"account-name"

每一次调用能获得100EOS, 每天最多获得1000个EOS.

例子:
``` 
curl https://faucet-bos-lib-testnet.keosd.io/get_token/bosaccount11
```

## 电报监控地址：
 
