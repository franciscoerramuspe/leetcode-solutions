'''
Given the head of a singly linked list, reverse the list, and return the reversed list

input:
1 -> 2 -> 5 -> 3 -> 6

output:
1 <- 2 <- 5 <- 3 <- 6

have a dummy node and a prev pointer
have a cur pointer starting at the head of the linked list
as we traverse the list, crate a tmp ptr that points to cur
 
tmp = cur
cur=cur.next
tmp.next=prv
prv=tmp

         1  ->  2  ->  5  ->  3  ->  6
dummy <-   <-  <-  <-   <-    prv   tmp
                                    cur

Time:O(N)
Space:O(1)
'''
class Node():
    def __init__(self, val, next):
        self.val=val
        self.next=next

def reverseLinkedList(head):
    dummy=Node()
    prev=dummy
    cur=head

    while cur:
        tmp=cur
        cur=cur.next
        tmp.next=prev
        prev=tmp
        
    return prev