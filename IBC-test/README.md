
## 在测试网络如何使用跨链转账eos和bos
- 中继节点ip
- [中继节点搭建和合约部署相关文档](https://github.com/boscore/ibc-test-env/blob/master/bos-plus-kylin-testnets/README.md)
### 合约名字

- eos的中继合约账户： ibctoken2bos
- bos的中继合约账户： ibctoken2eos

## 详细操作

需要用的两个网络的url：

kylin-api= -u http://kylin.meet.one:8888

bos-api= -u http://bos-testnet.meet.one:8888

### 1) 从kylin测试网上转出"50.0000 EOS"到BOS测试网上
````
cleos ${kylin-api}  transfer  ibctoken2bos  "10.0000 EOS" "boscoretest2@bos notes infomation" -p  ibckylintest
cleos ${kylin-api} get currency balance  eosio.token ibckylintest #减少
cleos ${kylin-api} get currency balance  eosio.token ibctoken2bos #增加 
````
在BOS测试网上查看
```
$cleos ${bos-api} get currency balance  ibctoken2eos boscoretest2
100.0000 EOSPG
```

### 2) 从BOS测试网上转出"10.0000 EOSPG"到kylin测试网
````
cleos ${bos-api} push action ibctoken2eos transfer '["boscoretest2","ibctoken2eos","10.0000 EOSPG" "ibckylintest@eos notes infomation"]' -p boscoretest2   
cleos ${bos-api} get currency balance ibctoken2eos boscoretest2 #减少10 BOSPS
````
在kylin测试网上查看
```
$cleos ${kylin-api} get currency balance  eosio.token ibckylintest #增加 10 EOS
```
### 3) 从BOS测试网上boscoretest2 转给boscoretest1 "10.0000 EOSPG"
````
cleos ${bos-api} push action ibctoken2eos transfer '["boscoretest2","boscoretest1","10.0000 EOSPG" "transfer"]' -p boscoretest2   
cleos ${bos-api} get currency balance ibctoken2eos boscoretest2 #减少10 BOSPS
cleos ${bos-api} get currency balance ibctoken2eos boscoretest1 #增加10 BOSPS
````


### 4) 从BOS测试网上，转出“50.0000 BOS”到kylin测试网上
```
cleos ${bos-api} transfer boscoretest2  ibctoken2eos "50.0000 BOS" "boscoretest2@eos notes infomation" -p  ibckylintest
cleos ${bos-api} get currency balance  eosio.token boscoretest2 #减少
cleos ${bos-api} get currency balance  eosio.token ibctoken2eos #增加 
```
在kylin测试网上进行查看
```
$cleos ${kylin-api} get currency balance ibctoken2bos ibckylintest
50.0000 BOSPG
```

### 5) 从kylin测试网上转出"10.0000 BOSPG"到BOS测试网
````
cleos ${kylin-api} push action ibctoken2bos transfer '["ibckylintest","ibctoken2bos","10.0000 BOSPG" "boscoretest2@bos notes infomation"]' -p ibckylintest   
cleos ${kylin-api} get currency balance ibctoken2bos ibckylintest #减少10 BOSPS
````
在BOS测试网上查看
```
$cleos ${bos-api} get currency balance  eosio.token boscoretest2 #增加 10 BOS
```

### 6) 从BOS测试网上ibckylintest 转给ibckylintesa "10.0000 EOSPG"
````
cleos ${kylin-api} push action ibctoken2bos transfer '["ibckylintest","ibckylintesa","10.0000 EOSPG" "transfer"]' -p ibckylintest  
cleos ${kylin-api} get currency balance ibctoken2bos ibckylintest #减少10 EOSPG
cleos ${kylin-api} get currency balance ibctoken2bos ibckylintesa #增加10 EOSPG
````

*说明：由于进行的跨链转账，所以到账时间会有延迟*

## 如何将kylin测试网络的token通过跨链转移到bos测试网上

下面的两步骤都是token合约操作的，如果想要注册token，请联系我们并且提供相关的信息。

### 在kylin测试网上，通过中继合约进行token的注册
```
#cleos ${kylin-api}  push action ibctoken2bos regacpttoken   '["<token-contract>","<max_accept>","<admin-account>","<min_once_transfer>","<max_once_transfer>", "<max_once_transfer>",<max_tfs_per_minute>,"<organization>","<website>","<service_fee_mode>","<service_fee_fixed>",<service_fee_ratio>,"<failed_fee_mode>","<failed_fee_fixed>",<failed_fee_ratio>,<active>,"<peerchain_sym>"]' -p ibctoken2bos
例如：
cleos ${kylin-api}  push action ibctoken2bos regacpttoken   '["eostoretoken","1000000000.0000 EST","eosstoreeost","5.0000 EST","500.0000 EST", "100000.0000 EST",1000,"eos store","www.eosstore.com","fixed","0.1000 EST",0.01,"fixed","0.1000 EST",0.01,true,"4,EST"]' -p ibctoken2bos
```
### 在bos测试网上注册锚定的token的信息

```
#cleos  ${bos-api}  push action ibctoken2eos regpegtoken  '["<max_supply>","<min_once_withdraw>","<max_once_withdraw>", "<max_daily_withdraw>",<max_wds_per_minute>,"<administrator>","<peerchain_contract>","<peerchain_sym>","<failed_fee_mode>","<failed_fee_fixed>",<failed_fee_ratio>,<active>]' -p ibctoken2eos
例如：
cleos  ${bos-api}  push action ibctoken2eos regpegtoken  '["1000000000.0000 EST","10.0000 EST","5000.0000 EST", "100000.0000 EST",1000,"bosstoreeost","eostoretoken","4,EST","fixed","0.1000 EST",0.01,true]' -p ibctoken2eos
```
新增加的token转账就如上面写的eos转账是一样










