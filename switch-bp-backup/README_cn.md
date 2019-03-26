## 主备切换的逻辑代码：
用python起2个线程,
flag  用于记录当前运行的bp节点是否在master,若是则为true;否则为false

### 线程1:
​	不断监测bp-master的状态，如果状态不ok,并且当前运行节点是master,线程1挂起（con.wait()）,由线程2执行切换；
​	线程1继续执行监测，检测master bp的状态，假如bp_master节点不ok,并且flag位false,说明已经切换到了备节点，无需切换；
​	线程1继续执行监测时如果发现master ok了，并且flag=false，则通知线程2切换回master；
​	线程1继续执行监测如果master ok并且flag=true,则无需切换。
​

### 线程2:
​	线程2拿到全局锁之后：
​        假如master_bp不ok且flag=true,直接挑选一个slave并resume，完成切换；
​       假如master_bp ok了，且flag=false,则切换回master节点；
​
### 使用：
	1. 首先在bp.json中按实际修改master & slaver 的地址
	2. 在命令行运行
	   ```
	   $ python bpswitch.py bp.json 
	   ```