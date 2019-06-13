# How to build  BP-node of  BOS Mainnet

### Operation steps are the same as BOS Testnet，but need to modify bpnode/config/config.ini and genesis.json

[BOS Testnet node build steps](https://github.com/boscore/bos-testnet/blob/master/README.md)

- the operation in config: replace p2p-peer-address、 modify signature-provider、producer-name

Use follow p2p-peer-address：
```
p2p-peer-address = p2p.bossweden.org:9876
p2p-peer-address = bos.eosn.io:9876
p2p-peer-address = bos.caleos.io:9882
p2p-peer-address = bosmatrix.blockmatrix.network:13546
p2p-peer-address = bos-peer.meet.one:9876
p2p-peer-address = bos.tokenpocket.pro:9376
p2p-peer-address = p2p.bos.eosrio.io:9876
p2p-peer-address = bosp2p.api.blockgo.vip:666
p2p-peer-address = bos.caleos.io:9882
p2p-peer-address = bos.eosn.io:9876
p2p-peer-address = p2p.bossweden.org:9876
p2p-peer-address = p2p.boscaribbean.com:9876
p2p-peer-address= peer-bos.oraclechain.io:19877
p2p-peer-address= api.bos42.io:9877
p2p-peer-address = peer1-bos.eosphere.io:9876
p2p-peer-address = bos.atticlab.net:10987
p2p-peer-address = bos-node.eosauthority.com:9393
p2p-peer-address = p2p.bos.nodepacific.com:9876
p2p-peer-address = 47.91.211.240:443
p2p-peer-address = 47.91.225.161:443
p2p-peer-address = peer-bos.eospacex.com:88
p2p-peer-address = bos-peer.eosio.sg:9879
p2p-peer-address = bos.eosargentina.io:9876
p2p-peer-address =bosapi-two.eosstore.co:9871
p2p-peer-address = bos-peer.eosio.sg:9879
```
Please reference the newest  access tool: [eosnation node statistics tool](https://validate.eosnation.io/bos/reports/endpoints.html)


- [genesis.json](https://github.com/boscore/bosres/blob/master/genesis.json)


### use snapshot start up BOS node

- Advantage
  1. Synchronize node quckly
  You can use the newest snapshot, it can start up node and achieve the head block within 3~4 min,time cost is greatly reduced.
  
  2. Save server resources 
  Use the snapshot mode to start the node, block.log will only save the data after the node is started, occupying less disk space. And the CPU and RAM started with snapshots are much smaller than the full node. Significantly reduce server costs.
- Disadvantages
  Because the node is started after saved data, the history of the account transaction cannot be found before.


when starting up add ```--snapshot=xxxx``` to docker-compose-bostest.yaml,such as:
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

BOS Mainnet snapshot:[Download address and Documentation](https://eosnode.tools/snapshots/bos)
