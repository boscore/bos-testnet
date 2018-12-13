
## step 1: prepare config.ini and genesis.json by start a node with eosio
## step 2: run nodeos
```
nodeos --config-dir /data/eos-config -d /data/eos-data --genesis-json /data/eos-config/genesis.json
```

## step 3: prepare wallet，准备钱包
```
cleos wallet create 
cleos wallet import --private-key <private-key>
```
## step 4: set contract eosio.bios
```
CONTRACTS_FOLDER='/opt/EOS-Mainnet/eos/build/contracts' 
cleos set contract eosio ${CONTRACTS_FOLDER}/eosio.bios -p eosio
```
## step 5: create system accounts
```
for account in eosio.bpay eosio.msig eosio.names eosio.ram eosio.ramfee eosio.saving eosio.stake eosio.token eosio.vpay eosio.wrap bos.dev bos.gov
do 
    echo -e "\n creating $account \n"; 
    cleos create account eosio ${account} EOS7hHHDtnPRbhMmfHJHUEKQyiutKrt9wZPdy1JbaATVLyxpCkrop; 
    sleep 1; 
done
```
```
cleos create account eosio bos EOS5oWpvWPYE7GzzJGfqLe9yDHzqrTT1gMiW9cBNftbaze3ZsfCXW

for account in  bos.stake1 bos.stake2  bos.stake3
do 
    echo -e "\n creating $account \n"; 
    cleos create account eosio ${account} EOS6Vi3dHtsMrw6gjZvyDRqeDttMhCia4NzH2zQdYbKYErTp5eJud; 
    sleep 1; 
done

for account in  bos.dapp bos.boost bos.airdrop
do 
    echo -e "\n creating $account \n"; 
    cleos create account eosio ${account} EOS7eXDuaVRSoYjcEgMkADf3VonfXN1TfLwG4Ts9aLxFngsxTep7B; 
    sleep 1; 
done

```


## step 6: set token and msig contract
```
cleos set contract eosio.token ${CONTRACTS_FOLDER}/eosio.token -p eosio.token 
cleos set contract eosio.msig ${CONTRACTS_FOLDER}/eosio.msig -p eosio.msig
```

## step 7: create and issue token
```
./nb.py -t
cless push action eosio.token create '["eosio", "10000000000.0000 BOS"]' -p eosio.token 
cless push action eosio.token issue '["eosio", "1013000000.0000 BOS", "BOSCore"]' -p eosio
```

## setp 8: setting privileged account for eosio.msig
```
cless push action eosio setpriv '{"account": "eosio.msig", "is_priv": 1}' -p eosio
```
## step 9: set contract eosio.system
```
cleos set contract eosio ${CONTRACTS_FOLDER}/eosio.system -x 1000 -p eosio
```
## step 10: set contract eosio.wrap
```
cleos set contract eosio.wrap ${CONTRACTS_FOLDER}/eosio.wrap -x 1000 -p eosio
```
## step 11: create some account
```
cless transfer eosio bos        "100000000 BOS"
cless transfer eosio bos.stake1 "300000000 BOS"
cless transfer eosio bos.stake2 "300000000 BOS"
cless transfer eosio bos.stake3 "200000000 BOS"

cless transfer eosio bos.dapp    "70000000 BOS"
cless transfer eosio bos.boost   "20000000 BOS"
cless transfer eosio bos.airdrop "10000000 BOS"
```


# TokenPeg bos.pegtoken合约会部署在下面三个系统账户中
bos.btc
bos.eth
bos.eos
注意：bos.btc 可以指定某一个账户具有某一个锚定币的发行权限，比如 huobipeg0001 可以发行 BTCHB 币种

csc bos.btc bos.pegtoken
csc bos.eth bos.pegtoken
csc bos.eos bos.pegtoken
增加bosissuances账户
```
cless system newaccount --stake-net "10.0000 BOS" --stake-cpu "10.0000 BOS" --buy-ram "10.0000 BOS" eosio bosissuances EOS7fEuHBCPSYBNC9GorAbbyuswNXQfDwmun5pr6dLLCXog83NJu6 EOS7fEuHBCPSYBNC9GorAbbyuswNXQfDwmun5pr6dLLCXog83NJu6
```
## step 12: transfer token
bos: 100M BOS belongs to BOSCore
bosbkstake01: 300M BOS for BOS.BANK
bosbkstake02: 300M BOS for BOS.BANK
bosbkstake03: 300M BOS for BOS.BANK
check eosio balance
cleos get currency balance eosio.token eosio
创建BP账户

```
cless system newaccount --transfer eosio winlinwinlin EOS7qX9gEBuEDmEgW2WaUdgmGWJB3swojXA5tCUgcfwQw9ZczYCUj  EOS5F1H46ojiKcUhRvzh9d91r7rtgNBZ14zosHUqf7J7ekNAzCba7 --stake-net "10.0000 BOS" --stake-cpu "10.0000 BOS" --buy-ram "10.0000 BOS"

cless transfer bosbkstake1 winlinwinlin "3000000 BOS"

# ? 
cless system newaccount --transfer eosio zeromindzero EOS7XCmjTfthmLnKQmLM8EEke97PFsuxQwZsbP4HsudwEJahkryeG EOS5gLn1NVinyJPvn2U4ow45GdBaoVdcz7zVDwfsTCLzft63KMC36 --stake-net "10.0000 BOS" --stake-cpu "10.0000 BOS" --buy-ram "10.0000 BOS" 

cless transfer bosbkstake1 zeromindzero "3000000 BOS"

# ?
cless system newaccount --transfer eosio boscorebos11    EOS7hjYGvhRF99czdXE5acUPjnWoKebpxebgRZqXxPUSxmT1K9q97    EOS5zhvmicLyPRvvY1a5TbYj1aNfqbMmd1ezgknWLrbR87fMnpnwo  --stake-net "10.0000 BOS" --stake-cpu "10.0000 BOS" --buy-ram "10.0000 BOS" 
cless transfer bosbkstake1 boscorebos11 "3000000 BOS"

# ?
cless system newaccount --transfer eosio boscorebos12    EOS84H324q8mu2oS1BwDcWXKJDpNgCiDauYgcVpRcYEzXxvfNvifa     EOS6oAKmx9cMhvfdZ4pacWhvPuFjd6n6JgF886xmKFY85Gdkw2rik  --stake-net "10.0000 BOS" --stake-cpu "10.0000 BOS" --buy-ram "10.0000 BOS" 
# ?
cless system newaccount --transfer eosio boscorebos13  EOS7enNAQLxT8biyNM39nApGYJrcS59TQY9dPBBeyZn1A4Ai9ouCk  EOS4wc7dsUsWS4L4QDMpJBhUqaqx6f4ZU7tSrGunGWYUAiSWygjtr --stake-net "10.0000 BOS" --stake-cpu "10.0000 BOS" --buy-ram "10.0000 BOS"


# ?
cless system newaccount --transfer eosio youbeforeme1 EOS8arxL9mNRfdVN43j2yTjqr8BuPM3rz3iBZi18JZ5zngQFX16ZA EOS5v5oqe1LtNVheTAZGcWkTbrZ8UJ7TFZg2LNsj3q6iwdBZP9au3 --stake-net "10.0000 BOS" --stake-cpu "10.0000 BOS" --buy-ram "10.0000 BOS" 
cless transfer bosbkstake1 youbeforeme1 "3000000 BOS"

cless system newaccount --transfer youbeforeme1 youbeforeme2 EOS8arxL9mNRfdVN43j2yTjqr8BuPM3rz3iBZi18JZ5zngQFX16ZA EOS5v5oqe1LtNVheTAZGcWkTbrZ8UJ7TFZg2LNsj3q6iwdBZP9au3 --stake-net "10.0000 BOS" --stake-cpu "10.0000 BOS" --buy-ram "10.0000 BOS"

cless transfer youbeforeme1 youbeforeme2 "20 BOS"

cless system newaccount --transfer youbeforeme2 youbeforeme3 EOS8arxL9mNRfdVN43j2yTjqr8BuPM3rz3iBZi18JZ5zngQFX16ZA EOS5v5oqe1LtNVheTAZGcWkTbrZ8UJ7TFZg2LNsj3q6iwdBZP9au3 --stake-net "10.0000 BOS" --stake-cpu "10.0000 BOS" --buy-ram "10.0000 BOS"

cless system newaccount --transfer youbeforeme1 pearlrivers1 EOS8arxL9mNRfdVN43j2yTjqr8BuPM3rz3iBZi18JZ5zngQFX16ZA EOS5v5oqe1LtNVheTAZGcWkTbrZ8UJ7TFZg2LNsj3q6iwdBZP9au3 --stake-net "10.0000 BOS" --stake-cpu "10.0000 BOS" --buy-ram "10.0000 BOS"

cless system newaccount --transfer youbeforeme1 pearlrivers2 EOS8arxL9mNRfdVN43j2yTjqr8BuPM3rz3iBZi18JZ5zngQFX16ZA EOS5v5oqe1LtNVheTAZGcWkTbrZ8UJ7TFZg2LNsj3q6iwdBZP9au3 --stake-net "10.0000 BOS" --stake-cpu "10.0000 BOS" --buy-ram "10.0000 BOS"

cless system newaccount --transfer youbeforeme1 pearlrivers3 EOS8arxL9mNRfdVN43j2yTjqr8BuPM3rz3iBZi18JZ5zngQFX16ZA EOS5v5oqe1LtNVheTAZGcWkTbrZ8UJ7TFZg2LNsj3q6iwdBZP9au3 --stake-net "10.0000 BOS" --stake-cpu "10.0000 BOS" --buy-ram "10.0000 BOS"

cless system newaccount --transfer youbeforeme1 newjerseyusa EOS8arxL9mNRfdVN43j2yTjqr8BuPM3rz3iBZi18JZ5zngQFX16ZA EOS5v5oqe1LtNVheTAZGcWkTbrZ8UJ7TFZg2LNsj3q6iwdBZP9au3 --stake-net "10.0000 BOS" --stake-cpu "10.0000 BOS" --buy-ram "10.0000 BOS"
```


# bosfaucet111
```
cless system newaccount --transfer --stake-net "10.0000 BOS" --stake-cpu "10.0000 BOS" --buy-ram "10.0000 BOS" eosio bosfaucet111 EOS77JF1pyiVsKBxonqP65MBo3RpH1beBwzrFBDHeqEwp2zTxqkDS    EOS5q9rNusgMU4qWRfbFhgsd7hwihkBrkAEPFrSS5zpdHTEBUa85C 

cleos transfer eosio eosfaucet111 "100000000.0000 BOS" 
#cleos transfer eosio eosio.faucet "199999730.0000 BOS"

```

## step last: resign all system account
```
for account in eosio.bpay eosio.msig eosio.names eosio.ram eosio.ramfee eosio.saving eosio.stake eosio.token eosio.vpay eosio.wrap bos.dev bos.gov
do
    cleos  push action eosio updateauth '{"account": "'$account'", "permission": "active", "parent": "owner", "auth":{"threshold": 1, "keys": [], "waits": [], "accounts": [{"weight": 1, "permission": {"actor": "eosio", "permission": active}}]}}' -p ${account}@active
    cleos  push action eosio updateauth '{"account": "'$account'", "permission": "owner", "parent": "",       "auth":{"threshold": 1, "keys": [], "waits": [], "accounts": [{"weight": 1, "permission": {"actor": "eosio", "permission": active}}]}}' -p ${account}@owner
  sleep 1;
done


#check system accounts
for account in eosio.bpay eosio.msig eosio.names eosio.ram eosio.ramfee eosio.saving eosio.stake eosio.token eosio.vpay  bos.dev bos.gov
do 
    echo --- ${account} --- && cleos get account ${account} && sleep 1; 
done

cleos push action eosio updateauth '{"account": "eosio", "permission": "active", "parent": "owner", "auth":{"threshold": 1, "keys": [], "waits": [], "accounts": [{"weight": 1, "permission": {"actor": "eosio.prods", "permission": active}}]}}' -p eosio@active 
cleos push action eosio updateauth '{"account": "eosio", "permission": "owner", "parent": "", "auth":{"threshold": 1, "keys": [], "waits": [], "accounts": [{"weight": 1, "permission": {"actor": "eosio.prods", "permission": active}}]}}' -p eosio@owner

#check eosio
cleos get account eosio
```

