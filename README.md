
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
cd bos-testnet/
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

# The deployment of BOSMainnet check [Detial](deploy-mainnetbp-EN.md)

## Chain info

```

"chain_id": "33cc2426f1b258ef8c798c34c0360b31732ea27a2d7e35a65797850a86d1ba85"

```


## P2P LIST

```
p2p-peer-address = 47.90.101.71:443
p2p-peer-address = 52.69.198.164:9003
p2p-peer-address = 34.80.177.78:9876
p2p-peer-address = 52.69.198.164:9003
p2p-peer-address = br.eosrio.io:29876
p2p-peer-address = bos-test.eosdac.io:39877
p2p-peer-address = 47.88.155.76:9877
p2p-peer-address = 47.245.31.246:2019
p2p-peer-address = 13.230.195.142:9234
p2p-peer-address = 47.88.155.76:9876
p2p-peer-address = 47.75.242.50:9876
p2p-peer-address = 47.252.81.49:9876
p2p-peer-address = 47.252.80.188:9876
p2p-peer-address = 47.245.53.152:9876
p2p-peer-address = 47.245.31.246:9876
p2p-peer-address = bos-testnet.eosphere.io:9876
p2p-peer-address = tst.bossweden.org:9899
p2p-peer-address = bos.testnet.eosargentina.io:9876
p2p-peer-address = peer.bostest.alohaeos.com:9876
p2p-peer-address = bos-test.eoshenzhen.io:9876
p2p-peer-address = 47.90.101.71:443
```


## HTTP/HTTPS API LIST

API nodes:
```
https://bos-testnet.eosphere.io/v1/chain/get_info
https://boscore.eosrio.io/v1/chain/get_info
https://api.bostest.alohaeos.com/v1/chain/get_info
http://bos-test.eoshenzhen.io:8888/v1/chain/get_info
https://bos-test.eoshenzhen.io:7443/v1/chain/get_info
http://47.252.81.49:8888/v1/chain/get_info
http://47.252.80.188:8888/v1/chain/get_info
http://47.245.53.152:8888/v1/chain/get_info
http://47.245.31.246:8888/v1/chain/get_info
```

HISTORY API nodes support get actions ( filter-on=* ):
```
https://bostest.api.blockgo.vip
https://boscore.eosrio.io/v1/history/ (MongoDB based)
https://bos-test.keosd.io/v1/history/ (MongoDB based)
https://bos-test.eoshenzhen.io:7443/v1/history/
```

State History Support:

```
http://sh-bostest.eoshenzhen.io:8088
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

