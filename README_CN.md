
欢迎来到 bos-testnet

[View in English](README.md)

## docker images 
You should update the last version from https://hub.docker.com/r/boscore/bos/tags/

## 克隆项目

```
git clone clone https://github.com/boscore/bos-testnet.git
cd fullnode
```

## 5秒之内搭建一个全节点

```
./run.sh
```

## 1分钟内手动搭建全节点

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

## 暂停/重启 同步

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
"chain_id": "795eca928742876c50687e7954e60f63c9e34bcc547cd1ab4a831e9f8c058c7f"

```

## P2P 节点列表

```
p2p-peer-address = 120.197.130.116:9000
p2p-peer-address = 13.230.87.138:9866
p2p-peer-address = 120.197.130.117:9000
p2p-peer-address = 120.197.130.117:9001
p2p-peer-address = 120.197.130.117:9002
p2p-peer-address = 120.197.130.117:9003
p2p-peer-address = 45.79.145.205:9000
p2p-peer-address = 47.91.244.124:443
p2p-peer-address = 8.208.9.182:443
p2p-peer-address = 47.254.82.241:443
p2p-peer-address = 47.254.134.167:443
p2p-peer-address = 149.129.133.66:443
```


## HTTP API 节点列表

API nodes:
```

```

支持 `get actions` ( filter-on=* ) 的API:
```

```

## 水龙头

在 `bos` 上创建账号非常简单:

#### 免费账号
创建免费账号: http://13.230.195.142/create_account?new_account_name

例子:
```
curl http://13.230.195.142/create_account\?111111111ooo
```

#### 获得免费Token
获得免费Token: http://13.230.195.142/get_token?your_account_name. 
每一次调用能获得100EOS, 每天最多获得1000个EOS.

例子:
``` 
curl http://13.230.195.142/get_token?111111111ooo
```





