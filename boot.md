## boot system
```
# step 1: prepare config.ini and genesis.json by start a node with eosio
# step 2: run nodeos

nodeos --config-dir /data/eos-config -d /data/eos-data --genesis-json /data/eos-config/genesis.json


# step 3: prepare wallet，准备钱包

cleos wallet create 
cleos wallet import --private-key <private-key>

# step 4: set contract eosio.bios

CONTRACTS_FOLDER='/opt/EOS-Mainnet/eos/build/contracts' 
cleos set contract eosio ${CONTRACTS_FOLDER}/eosio.bios -p eosio

# step 5: create system accounts

for account in eosio.bpay eosio.msig eosio.names eosio.ram eosio.ramfee eosio.saving eosio.stake eosio.token eosio.vpay eosio.wrap bos.dev bos.gov tklimit.sets
do 
    echo -e "\n creating $account \n"; 
    cleos create account eosio ${account} EOS7hHHDtnPRbhMmfHJHUEKQyiutKrt9wZPdy1JbaATVLyxpCkrop; 
    sleep 1; 
done

cleos create account eosio bos EOS5oWpvWPYE7GzzJGfqLe9yDHzqrTT1gMiW9cBNftbaze3ZsfCXW

for account in   uid bos.stake1 bos.stake2  bos.stake3
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

# set an abp 
cleos  create account eosio boscoretokyo EOS7B2h89KDYXzVNj6G8MLkFgQExfns1ssTH19MkDTPcFBTfssJb4
cleos push action eosio setprods '{"schedule":[{"producer_name":"boscoretokyo","block_signing_key":"EOS7B2h89KDYXzVNj6G8MLkFgQExfns1ssTH19MkDTPcFBTfssJb4"}]}' -p eosio

# step 6: set token and msig contract
cleos set contract eosio.token ${CONTRACTS_FOLDER}/eosio.token -p eosio.token 
cleos set contract eosio.msig ${CONTRACTS_FOLDER}/eosio.msig -p eosio.msig

# step 7: create and issue token

cleos push action eosio.token create '["eosio", "10000000000.0000 BOS"]' -p eosio.token 
cleos push action eosio.token issue '["eosio", "1013000000.0000 BOS", "BOSCore"]' -p eosio


# setp 8: setting privileged account for eosio.msig

cleos push action eosio setpriv '{"account": "eosio.msig", "is_priv": 1}' -p eosio

# step 9: set contract eosio.system

cleos set contract eosio ${CONTRACTS_FOLDER}/eosio.system -x 1000 -p eosio

# step 10: set contract eosio.wrap

cleos set contract eosio.wrap ${CONTRACTS_FOLDER}/eosio.wrap -x 1000 -p eosio

# step 11: transfer some token 

cleos transfer eosio bos        "100000000 BOS"
cleos transfer eosio bos.stake1 "300000000 BOS"
cleos transfer eosio bos.stake2 "300000000 BOS"
cleos transfer eosio bos.stake3 "200000000 BOS"

cleos transfer eosio bos.dapp    "70000000 BOS"
cleos transfer eosio bos.boost   "20000000 BOS"
cleos transfer eosio bos.airdrop "10000000 BOS"


# step 12: resign all system account

for account in eosio.bpay eosio.msig eosio.names eosio.ram eosio.ramfee eosio.saving eosio.stake eosio.token eosio.vpay eosio.wrap bos.dev bos.gov tklimit.sets
do
    cleos  push action eosio updateauth '{"account": "'$account'", "permission": "active", "parent": "owner", "auth":{"threshold": 1, "keys": [], "waits": [], "accounts": [{"weight": 1, "permission": {"actor": "eosio", "permission": active}}]}}' -p ${account}@active
    cleos  push action eosio updateauth '{"account": "'$account'", "permission": "owner", "parent": "",       "auth":{"threshold": 1, "keys": [], "waits": [], "accounts": [{"weight": 1, "permission": {"actor": "eosio", "permission": active}}]}}' -p ${account}@owner
  sleep 1;
done

#check system accounts
for account in eosio.bpay eosio.msig eosio.names eosio.ram eosio.ramfee eosio.saving eosio.stake eosio.token eosio.vpay  eosio.wrap bos.dev bos.gov tklimit.sets
do 
    echo --- ${account} --- && cleos get account ${account} && sleep 1; 
done

cleos push action eosio updateauth '{"account": "eosio", "permission": "active", "parent": "owner", "auth":{"threshold": 1, "keys": [], "waits": [], "accounts": [{"weight": 1, "permission": {"actor": "eosio.prods", "permission": active}}]}}' -p eosio@active 
cleos push action eosio updateauth '{"account": "eosio", "permission": "owner", "parent": "", "auth":{"threshold": 1, "keys": [], "waits": [], "accounts": [{"weight": 1, "permission": {"actor": "eosio.prods", "permission": active}}]}}' -p eosio@owner

#check eosio
cleos get account eosio

# step 13  aridrop EOS Mainne 

```


## boot test net 
The following content is only for the BOS Testnet.
### bosfaucet111
```
cleos system newaccount --transfer --stake-net "10.0000 BOS" --stake-cpu "10.0000 BOS" --buy-ram "10.0000 BOS" eosio bosfaucet111 EOS77JF1pyiVsKBxonqP65MBo3RpH1beBwzrFBDHeqEwp2zTxqkDS    EOS5q9rNusgMU4qWRfbFhgsd7hwihkBrkAEPFrSS5zpdHTEBUa85C 

cleos transfer eosio bosfaucet111 "100000000.0000 BOS" 

```

### 创建BP账户

```
cleos  system newaccount --stake-net "10.0000 BOS" --stake-cpu "10.0000 BOS" --buy-ram "10.0000 BOS"  eosio boscorebos11 EOS5zhvmicLyPRvvY1a5TbYj1aNfqbMmd1ezgknWLrbR87fMnpnwo 
cleos  system newaccount --stake-net "10.0000 BOS" --stake-cpu "10.0000 BOS" --buy-ram "10.0000 BOS"  eosio boscorebos12 EOS6oAKmx9cMhvfdZ4pacWhvPuFjd6n6JgF886xmKFY85Gdkw2rik 
cleos  system newaccount --stake-net "10.0000 BOS" --stake-cpu "10.0000 BOS" --buy-ram "10.0000 BOS"  eosio boscorebos13 EOS4wc7dsUsWS4L4QDMpJBhUqaqx6f4ZU7tSrGunGWYUAiSWygjtr 

for account in youbeforeme1 youbeforeme2 youbeforeme3 bosmiaomiao1 bosmiaomiao2 bosmiaomiao3 bosmiaomiao4 bosmiaomiao5 pinganbaobao pinganbaobei
do
    cleos  system newaccount --stake-net "10.0000 BOS" --stake-cpu "10.0000 BOS" --buy-ram "10.0000 BOS"  eosio ${account}  EOS5v5oqe1LtNVheTAZGcWkTbrZ8UJ7TFZg2LNsj3q6iwdBZP9au3;
    sleep 1;
done

for account in london111111 franklin1111 dubai1111111 bombay111111 hongkong1111
do
    cleos  system newaccount --stake-net "10.0000 BOS" --stake-cpu "10.0000 BOS" --buy-ram "10.0000 BOS"  eosio ${account} EOS4wVs4b9gUnQURXdDsLmnJEXMpqE1ir28L48gCEpMyutnd6Gxrj;
    sleep 1;
done

cleos  system newaccount --stake-net "10.0000 BOS" --stake-cpu "10.0000 BOS" --buy-ram "10.0000 BOS"  eosio zeromindzero  EOS5gLn1NVinyJPvn2U4ow45GdBaoVdcz7zVDwfsTCLzft63KMC36
cleos  system newaccount --stake-net "10.0000 BOS" --stake-cpu "10.0000 BOS" --buy-ram "10.0000 BOS"  eosio montecarloio  EOS6NYP8EujJURbArAHUMYCSjJAH7Vwa5Sxx7aLUiXiEwWN8XsYJw
cleos  system newaccount --stake-net "10.0000 BOS" --stake-cpu "10.0000 BOS" --buy-ram "10.0000 BOS"  eosio alphalimited  EOS7RcQx7g7tJGf3DSYSUgF2FWuNh1TTMAPuo7c82WCnWG6V4F4fR
cleos  system newaccount --stake-net "10.0000 BOS" --stake-cpu "10.0000 BOS" --buy-ram "10.0000 BOS"  eosio alphaxsydney  EOS7Vgx98hC4eisQVubCNvBGGN8gM7BKucZ5mJzgVUXpJMLF65okg
cleos  system newaccount --stake-net "10.0000 BOS" --stake-cpu "10.0000 BOS" --buy-ram "10.0000 BOS"  eosio mindtosydney  EOS8BeTKczXv6uEKksV8fF74R1fiARTVWJ7Qwtn8mRmM17aYqkSjb
cleos  system newaccount --stake-net "10.0000 BOS" --stake-cpu "10.0000 BOS" --buy-ram "10.0000 BOS"  eosio montexsydney  EOS8R9yKbEJ5mbU7hG5dV8pbhmaYMYpXxhCwpKwQ5j28QEikaKxUK

cleos  transfer  eosio  zeromindzero "100000000.0000 BOS"
cleos  transfer  eosio  youbeforeme1 "100000000.0000 BOS"
cleos  transfer  eosio  london111111 "100000000.0000 BOS"
cleos  transfer  eosio  boscorebos11 "100000000.0000 BOS"

```






