## 
- 中继节点ip
- 合约名字



## 详细操作

需要用的两个网络的url：

kylin-api= -u http://kylin.meet.one:8888

bos-api= -u http://bos-testnet.meet.one:8888

### 1) 从kylin测试网上转出"50.0000 EOS"到BOS测试网上
````
cleos ${kylin-api}  transfer  ibctoken2bos  "10.0000 EOS" "boscoretest2@bos notes infomation" -p  ibckylintest
cleos ${kylin-api} get currency balance  eosio.token ibckylintest #减少
cleos ${kylin-api} get currency balance  eosio.token ibc2token555 #增加 
````
在BOS测试网上查看
```
$cleos ${bos-api} get currency balance  ibc2token555 boscoretest2
100.0000 EOSPG
```

### 2) 从BOS测试网上，转出“50.0000 BOS”到kylin测试网上
```
cleos ${bos-api} transfer boscoretest2  ibctoken2bos "50.0000 BOS" "boscoretest2@bos notes infomation" -p  ibckylintest
cleos ${kylin-api}  transfer    "10.0000 EOS" 
cleos ${bos-api} get currency balance  eosio.token boscoretest2 #减少
cleos ${bos-api} get currency balance  eosio.token ibc2token555 #增加 
```
在kylin测试网上进行查看
```
$cleos ${kylin-api} get currency balance ibc2token555 ibckylintest
50.0000 BOSPG
```

### 3) 从kylin测试网上转出"10.0000 BOSPG"到BOS测试网
````
cleos ${kylin-api} push action ibc2token555 transfer '["ibckylintest","ibc2token555","10.0000 BOSPG" "ibc receiver=boscoretest2"]' -p ibckylintest   
cleos ${kylin-api} get currency balance ibc2token555 ibckylintest #减少10 BOSPS
````
在BOS测试网上查看
```
$cleos ${bos-api} get currency balance  eosio.token boscoretest2 #增加 10 BOS
```

### 4) 从BOS测试网上转出"10.0000 EOSPG"到kylin测试网
````
cleos ${bos-api} push action ibc2token555 transfer '["boscoretest2","ibc2token555","10.0000 EOSPG" "ibc receiver=ibckylintest"]' -p boscoretest2   
cleos ${bos-api} get currency balance ibc2token555 boscoretest2 #减少10 BOSPS
````
在kylin测试网上查看
```
$cleos ${kylin-api} get currency balance  eosio.token ibckylintest #增加 10 EOS
```

*说明：由于进行的跨链转账，所以到账时间会有延迟*

