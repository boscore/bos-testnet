## Logics for active/standby switchover:
Start with 2 threads in python,
Flag is used to record whether the currently running bp node is in the master, if it is true; otherwise it is false

### Thread 1:
- Continuously monitor the status of the bp-master. If the status is not ok, and the current running node is the master, the thread 1 hangs (con.wait()), and the thread 2 performs the switching;
- Thread 1 continues to perform monitoring to detect the status of the master bp. If the bp_master node is not ok, and the flag bit is false, it indicates that the standby node has been switched to, and no handover is required.
- When thread 1 continues to perform monitoring, if it finds that master is ok, and flag=false, it notifies thread 2 to switch back to master;
- Thread 1 continues to perform monitoring if master ok and flag=true, no switching is required.


### Thread 2:
After thread 2 gets the global lock:
If master_bp is not ok and flag=true, directly select a slave and resume to complete the switch;
If master_bp is ok, and flag=false, switch back to the master node;