# CryptoKylin-Testnet

Welcome to the CryptoKylin-Testnet

[点击查看中文](README_CN.md)

## Dependencies

- [Docker](https://docs.docker.com) Docker 17.05 or higher is required
- [docker-compose](https://docs.docker.com/compose/) version >= 1.10.0

## Clone project

```
git clone git@github.com:cryptokylin/CryptoKylin-Testnet.git
cd fullnode
```

## Setup a fullnode in 5 seconds using the shell

```
./run.sh
```

## Setup a fullnode manually in 1 minute

The first step, create the desired directory:

```
mkdir -p /data/eos/nodeos-data-volume/nodeos-data-kylin/data
```

The second step is to prepare the configuration file:

```
cp -r config /data/eos/nodeos-data-volume/nodeos-data-kylin
```

The third step, join the network:

```
docker-compose -f docker-compose-kylin-init.yaml up -d
```

## Stop/Restart syncing

To stop:

```
docker-compose -f docker-compose-kylin.yaml down
```

To restart:

```
docker-compose -f docker-compose-kylin.yaml down
docker-compose -f docker-compose-kylin.yaml up -d
```
## Chain info

```

"chain_id": ""

```

## P2P LIST

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


## HTTP API LIST

API nodes:
```

```

API nodes support get actions ( filter-on=* ):
```

```

## Faucet

Creating accounts on cryptokylin is pretty simple:

#### Free Account
Create account using: http://faucet.  /create_account?new_account_name

Example:
```
curl http://faucet.   /create_account\?111111111ooo
```


#### Get Free tokens
Get free token with: http://faucet.   /get_token?your_account_name.   




## Backup files

For those of you who want to sync fast to the latest block, you can use these backup files here:

#### Docker version

- 

#### Non docker version

- 

### How to use backup
#### docker version
- 
- 
- 

#### Non docker version
- 


Docker 
boscore/bos:v1.0.1
https://hub.docker.com/r/boscore/bos/tags/

genesis.json
Private key: XXX
Public key: EOS79F2FfmAfoYPSqCdyxfUYq3Jhzvpk8meAZEyBrCi6tUPKP2sVh



简易eosio启动
灵感来自python,bios
/data4/bos/build/programs/nodeos/nodeos    --max-irreversible-block-age -1    --contracts-console    --verbose-http-errors    --genesis-json /data4/boscore-testnet/genesis.json    --blocks-dir /data4/boscore-testnet/nodes/00-eosio/blocks    --config-dir /data4/boscore-testnet/nodes/00-eosio    --data-dir /data4/boscore-testnet/nodes/00-eosio    --chain-state-db-size-mb 1024    --http-server-address 120.197.130.116:8000    --p2p-listen-endpoint 120.197.130.116:9000    --max-clients 40    --p2p-max-nodes-per-host 40    --enable-stale-production    --producer-name eosio    --private-key '["EOS79F2FfmAfoYPSqCdyxfUYq3Jhzvpk8meAZEyBrCi6tUPKP2sVh","5KjU2RwtxGNNJP3WinuNdBsqtSMZoTKV1Hjn2Mf2CXndQ7yXW7m"]'    --plugin eosio::http_plugin    --plugin eosio::chain_api_plugin    --plugin eosio::producer_plugin    --plugin eosio::history_plugin    --plugin eosio::history_api_plugin    2>>./nodes/00-eosio/stderr


Archived 账户

# ?
cless system newaccount --transfer eosio techplusplus EOS5LckXWhDN99gwtvD5wB56Sq8cAEphDDJoEQ8euVBVWRa242Bqj EOS7tJWvs7wQPkxMJCqkvw15Zuq2KFoGhCiRfrngAJXHPsXSbwdaD --stake-net "10.0000 BOS" --stake-cpu "10.0000 BOS" --buy-ram "10.0000 BOS" 

cless transfer bosbkstake1 techplusplus "3000000 BOS"

# ?
cless system newaccount --transfer eosio boscoreiocom   EOS72XwtJ4QEDSs2KtnrLYzwjTNQfdVSWrUmYfPwaHddzmQvYmdhP   EOS8NK9CaKiuGystkv9c5UhjecM4PP3E1uGHPedP8aeGt2YpJDkYv  --stake-net "10.0000 BOS" --stake-cpu "10.0000 BOS" --buy-ram "10.0000 BOS" 


# ?
cless system newaccount --transfer eosio bosanmonous   EOS7hjYGvhRF99czdXE5acUPjnWoKebpxebgRZqXxPUSxmT1K9q97 EOS5zhvmicLyPRvvY1a5TbYj1aNfqbMmd1ezgknWLrbR87fMnpnwo

  --stake-net "10.0000 BOS" --stake-cpu "10.0000 BOS" --buy-ram "10.0000 BOS" 


运维Tips:
lsof -p 5380 -nP | grep  TCP
lsof 的 -nP 参数用于将 ip 地址和端口号显示为正常的数值类型

图片: https://uploader.shimo.im/f/moQREvMBBB0vrF8U.png



图片: https://uploader.shimo.im/f/5j79aaCvDfM1cNc9.png




 ps aux | grep youbeforeme2
 
 ps aux  | grep -v grep | grep youbeforeme2 | awk '{print $2}'
 
kill -2 $(ps aux  | grep -v grep | grep youbeforeme2 | awk '{print $2}')
图片: https://uploader.shimo.im/f/624hBjCSP8MO940N.png


Docker 设置
进入images
docker run -i -t 8dbd9e392a96 /bin/bash
打包Docker

Docker创建镜像有两种方法：
1、使用docker commit命令
2、使用docker build命令