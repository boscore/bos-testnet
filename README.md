
[点击查看中文](README_CN.md)

### docker images 
You should update the last version from https://hub.docker.com/r/boscore/bos/tags/

### Clone project

```
git clone https://github.com/boscore/bos-testnet.git
cd fullnode
```
The diffrence between fullnode and bpnode is the config.ini bpnode have producer_plugin.
### Setup a fullnode in 5 seconds using the shell

```
./run.sh
```

### Setup a fullnode manually in 1 minute

The first step, create the desired directory:

```
mkdir -p /data/eos/nodeos-data-volume/nodeos-data-bostest/data
```

The second step is to prepare the configuration file:

```
cp -r config /data/eos/nodeos-data-volume/nodeos-data-bostest
```

The third step, join the network:

```
docker-compose -f docker-compose-bostest-init.yaml up -d
```

### Stop/Restart syncing

To stop:

```
docker-compose -f docker-compose-bostest.yaml down
```

To restart:

```
docker-compose -f docker-compose-bostest.yaml down
docker-compose -f docker-compose-bostest.yaml up -d
```

## Chain info

```

"chain_id": "33cc2426f1b258ef8c798c34c0360b31732ea27a2d7e35a65797850a86d1ba85"

```

## P2P LIST

```
p2p-peer-address = 13.230.195.142:9866
p2p-peer-address = 120.197.130.117:9020
p2p-peer-address = 120.197.130.117:9021
p2p-peer-address = 120.197.130.117:9022
p2p-peer-address = 120.197.130.117:9023
p2p-peer-address = 120.197.130.117:9024
p2p-peer-address = 47.91.244.124:443
p2p-peer-address = 8.208.9.182:443
p2p-peer-address = 47.254.82.241:443
p2p-peer-address = 47.254.134.167:443
p2p-peer-address = 149.129.133.66:443
p2p-peer-address = 35.221.141.101:9878
p2p-peer-address = 35.221.141.101:9880
p2p-peer-address = 35.221.141.101:9900
p2p-peer-address = 35.236.174.234:9902
p2p-peer-address = 35.236.174.234:9903
p2p-peer-address = 35.236.174.234:9904
p2p-peer-address = bos-testnet.meet.one:9876
p2p-peer-address = 47.75.252.36:9878
```


## HTTP API LIST

API nodes:
```
http://47.254.82.241:80/v1/chain/get_info 
http://47.254.134.167:80/v1/chain/get_info 
http://49.129.133.66:80/v1/chain/get_info 
http://8.208.9.182:80/v1/chain/get_info 
http://47.91.244.124:80/v1/chain/get_info 
http://120.197.130.117:8020/v1/chain/get_info
http://bos-testnet.meet.one:8888/v1/chain/get_info
http://bos-testnet.mytokenpocket.vip:8890/v1/chain/get_info
```

API nodes support get actions ( filter-on=* ):
```
https://bostest.api.blockgo.vip
```

## Faucet

Creating accounts on bostest is pretty simple:

#### Free Account
Create account using: https://faucet-bos-testnet.keosd.io/create/<new_account>.


Example:
```
curl https://faucet-bos-testnet.keosd.io/create/111111111ooo
```


#### Get Free tokens
Get free token with: https://faucet-bos-testnet.keosd.io/get_token/<your_account_name>.  
Example
```
curl https://faucet-bos-testnet.keosd.io/get_token/111111111ooo
```


## telegram monitor 
https://t.me/bosteststatus 

