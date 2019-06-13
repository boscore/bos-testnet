
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
p2p-peer-address = 13.230.195.142:9234
p2p-peer-address = 47.88.155.76:9876
p2p-peer-address = 47.75.242.50:9876
p2p-peer-address = bos-testnet.eosphere.io:9876
p2p-peer-address = bostest.eosn.io:9876
p2p-peer-address = tst.bossweden.org:9899
p2p-peer-address = bos.testnet.eosargentina.io:9876
p2p-peer-address = peer.bostest.alohaeos.com:9876
p2p-peer-address = bos-test.eoshenzhen.io:9876
```


## HTTP API LIST

API nodes:
```
https://bos-testnet.eosphere.io/v1/chain/get_info
https://boscore.eosrio.io/v1/chain/get_info
https://api.bostest.alohaeos.com/v1/chain/get_info
http://bos-test.eoshenzhen.io:8888/v1/chain/get_info
```

API nodes support get actions ( filter-on=* ):
```
https://bostest.api.blockgo.vip
https://boscore.eosrio.io/v1/history/ (MongoDB based)
https://history-api-bos-testnet.keosd.io/v1/history/ (MongoDB based)
http://bos-test.eoshenzhen.io:8888/v1/chain/get_info
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

