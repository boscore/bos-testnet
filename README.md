
[点击查看中文](README_CN.md)

## Dependencies

- [Docker](https://docs.docker.com) Docker 17.05 or higher is required
- [docker-compose](https://docs.docker.com/compose/) version >= 1.10.0

## Clone project

```
git clone https://github.com/boscore/bos-testnet.git
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
