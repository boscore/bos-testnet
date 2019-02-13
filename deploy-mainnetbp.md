# 如何搭建BOS主网的bp节点

操作步骤跟测试网搭建相同，需要在config中修改bp的名字和signature-key

[测试网节点搭建步骤](https://github.com/boscore/bos-testnet/blob/master/README.md)

只需要在config中替换p2p-peer-address和genesis即可

- 使用的p2p-peer-address如下：
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
最新接入请参考工具: [eosnation节点统计工具](https://validate.eosnation.io/bos/reports/endpoints.html)


- genesis.json
[genesis.josn链接](https://github.com/boscore/bosres/blob/master/genesis.json)
