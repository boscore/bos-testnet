# bos测试网跨链换币使用文档
## 一、说明
bos测试网跨链换币所有的服务已部署完成，完成主链btc/eth跟侧链合约btc/eth的兑换，服务都是跑在测试网上，所以跨链换币的测试也必须在在测试网上测试。

## 二、bos合约
1、bos侧链兑换合约现支持两种合约token btc/eth的兑换，每个币种各由一个合约来完成兑换，下表是btc/eth的合约账号、承兑商账号、承兑人账号、承兑商合作方、承兑商审核员

| 币种   | 合约账号  | 承兑商         |  承兑人      |  partner                                  | 审核员
| 
btc  bos.btc  boshuobipool  btchuobipool   hbpartner111/hbswspartner/huobipartner     huobiauditor
eth  bos.eth  boshuobipool  ethhuobipool   hbpartner111/ hbswspartner

## 2、账号权限及功能
账号(账号名)                      权限及功能                           备注
合约账号(bos.btc)     合约部署者，在主网启动时部署该合约          cleos --url http://172.18.12.23:8888 get scope bos.btc ---此命令可以查看合约账号下承兑商、承兑人、合作方、partner、审核员的数目
承兑商(boshuobipool)  由合约账号创建，负责token的发行、销毁、费率设置、提币设置，初始化承兑人信息等
1、cleos --url http://172.18.12.23:8888 get table bos.btc BTC stats ---此命令可以查看合约token btc的承兑商、承兑人、发行总量、最大最小换币金额、费率等信息
2、cleos --url  http://172.18.12.23:8888 get table bos.btc BTC operates ---此命令可以查看承兑商btc的发行和销毁记录
承兑人(btchuobipool)
由承兑商赋予权限，负责token的转入转出功能
cleos --url  http://172.18.12.23:8888 get table bos.btc bos.btc symbols ---此命令可以查看btc币种的名称和精度
partner(huobipartner)
合作方权限由承兑商设置，负责给账号申请充币地址
cleos --url  http://172.18.12.23:8888 get table bos.btc BTC applicants ---此命令可以查看btc 承兑商的合作方账号
审核员(huobiauditor)
审核员权限由承兑商设置，可以同意或拒绝大额提币，将提币失败的合约token退还给用户
cleos --url  http://172.18.12.23:8888 get table bos.btc BTC auditors ---此命令可以查看承兑商的审核员账号
3、合约方法使用，具体每个合约方法的使用可参考：锚定币合约设计方案

三、 bos测试网跨链换币服务可分为三个功能：为bos 账号申请获取btc/eth充币地址，主链btc/eth兑换为侧链合约token btc/eth，侧链合约token btc/eth兑换为主链btc/eth。
  1、为bos账号申请获取btc/eth充币地址。在主链btc/eth兑换为侧链合约token btc/eth之前，需要为bos账号提供充币的btc/eth地址，bos账号和btc/eth地址的映射关系最终会以交易的形式广播到链上，通过合约表可以获取这个关系。以下步骤是bos账号跟btc/eth地址建立映射关系的步骤
序号
步骤
备注
1
在测试网创建bos账号
通过命令行查看账号是否创建成功
cleos --url http://172.18.12.23:8888 get account bostokentest
2
为创建成功的账号申请btc/eth主链的充币地址。地址申请是由承兑商授权的合作方完成并签名的，所以需要将预申请账号交由合作方代为申请或着自己申请成为合作方，此时合作方可以调用合约方法applyaddr为bos账号申请btc/eth充币地址
cleos --url http://172.18.12.23:8888 push action bos.btc applyaddr '[ "huobipartner", "BTC", "bostokentest" ]' -p huobipartner 其中”bostokentest”为代申请的账号
3
查看为bos账号申请的btc/eth地址是否成功（从申请btc/eth地址，到链上状态为0可能需要花费两分钟时间）
cleos --url  http://172.18.12.23:8888 get table bos.btc BTC addrs ---通过此命令可以查看btc地址是否分配成功，state为0表示分配成功，state为非0表示未分配成功
2、主链btc/eth兑换为侧链合约token btc/eth。将主链btc/eth充币到bos账号对应的充币地址，即可在侧链获取到对应的合约token btc/eth
	2.1、因为btc/eth服务都运行在测试网上，测试时需要将测试币转到映射的地址上面完成兑换，测试节点的部署和测试币的申请可以参考：

	2.2、以下步骤为从主链btc/eth兑换为侧链合约token btc/eth的步骤
序号
步骤
备注
1
通过cleos获取bos账号对应的btc/eth地址（前提是bos账号映射btc/eth地址的步骤已经完成）
cleos --url  http://172.18.12.23:8888 get table bos.btc BTC addrs ---此命令可以读取bos账号对应的btc/eth地址
2
从btc/eth测试链向btc/eth映射的地址转账，转账方式已经在2.1中的参考文件中说明
转账方式请参考2.1中的参考文件
3
bos钱包将调用合约方法deposit向指定的账户发行对应充币金额的合约token btc/eth
合约方法deposit
4
查看主链btc/eth 兑换为侧链btc/eth是否成功（从btc/eth向充币地址充币到侧链获取到合约token可能要花费btc 为1个小时或eth为5分钟的时间）
cleos --url  http://172.18.12.23:8888 get table bos.btc BTC deposits ---此命令可以查看兑换状态
3、侧链合约token兑换为主链btc/eth，用户通过调用withdraw方法将提币数量、提币地址作为参数将侧链的合约token转账到承兑人账号，跨链服务将读取到对应的提币地址、提币数量，将btc/eth提币到用户地址，以下为操作步骤
序号
步骤
备注
1
用户调用合约方法withdraw提币
cleos --url http://172.18.12.23:8888 push action bos.btc withdraw '["bostokentest", "3JQSigWTCHyBLRD979JWgEtWP5YiiFwcQB", "0.10000000 BTC", "BTC提币" ]' -p bostokentest  ---此方法是将合约token提币到主链btc/eth，其中包括提币账号、提币地址、提币数量，memo
2
bos跨链服务会在安全的确认块数内将btc/eth提币到用户提供的btc/eth地址下。如果主链成功bos跨链服务会通过调用feedback方法将主链的提币hash广播到侧链上；否则如果失败bos跨链服务会调用rollback服务将失败信息反馈到链上
btc/eth地址要提供测试链的地址
3
提币成功以后用户可以通过调用合约方法查看提币记录
cleos --url  http://172.18.12.23:8888 get table bos.eth ETH withdraws ---此方法会获取到提币记录，包括：主链侧链的交易hash，提币金额、提币限制、提币状态

