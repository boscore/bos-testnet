
[点击查看中文](PBFT-testnet-CN.md)

### docker images 
You should update the last version from https://hub.docker.com/r/boscore/boslib/tags

### Clone project

```
git clone https://github.com/boscore/bos-testnet.git
git checkout lib-test
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

"chain_id": "514cb0a66d3f60fd213dea0c9fd1a30b4405e3375599c40efd597c089b832118"

```

## P2P LIST

```
p2p-peer-address = 13.230.195.142:9871
p2p-peer-address =  52.194.161.6:9877 
p2p-peer-address = 13.230.195.142:9872 
p2p-peer-address =  47.244.41.129:448
p2p-peer-address =  47.244.42.171:548
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


## HTTP API LIST

API nodes:
```
http://52.194.161.6:9999/v1/chain/get_info 
http://13.230.195.142:4444/v1/chain/get_info
```

API nodes support get actions ( filter-on=* ):
```

```

## Faucet

Creating accounts on bostest is pretty simple:

#### Free Account
Create account using: https://faucet-bos-lib-testnet.keosd.io/create/"account-name"


Example:
```
curl https://faucet-bos-lib-testnet.keosd.io/create/bosaccount11
```


#### Get Free tokens
Get free token with: https://faucet-bos-lib-testnet.keosd.io/get_token/"account-name" 
Example
```
curl https://faucet-bos-lib-testnet.keosd.io/get_token/bosaccount11
```


## telegram monitor 


