# encoding=utf-8
'''
Q) How would you synchronize a linked list across multiple computers. If nodes are added/removed to a linked list on one computer, all others must reflect this change.


'''

#Distributed locks!

'''
1) Consider you have a global lock manager (it can any node from your cluster)
2) In case of any node wants wright, it send request for exclusive permission to lock manager.
3) Lock manager check (in locks accounting data)
(a)if already no one (any node) has exclusive hold on this lock
and no-one has Read hold as well then
allows exclusive permission to requesting node. and update lock accounting.

else if any/multiple nodes holds read lock then
Send revoke request to every lock holder.
once it receives ACK (release) from all the nodes allow exclusive permission to requesting node.


  (b) if any node already holds the exclusive lock
Then based on lock request wait or return.
If wait then.
Send revoke request to exclusive lock holder,
Once exclusive lock holder done with its operation then it can ACK along with changed data as piggyback data.



i.e.
"Once exclusive lock holder done with its operation then it can ACK along with changed data as piggyback data."

Means once any node modifies the data with exclusive permission (i.e. from other no one can even read) and if lock manager now requesting lock revoke from exclusive lock holder, it means now some node trying to read or write. then
The previous node which has modified the data (with exclusive lock) will send modified data in the form of "piggyback" and using this piggyback data any one (who gets the read or write lock grant) can get the latest/updated information.
'''