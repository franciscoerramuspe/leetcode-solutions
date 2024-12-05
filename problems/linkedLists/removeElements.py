'''
Given the head of a linked list and an integer val, 

remove all the nodes of the linked list that has Node.val == val, and return the new head.

input:
val = 3

head:
    1  ->  2 ->  3 -> 3 -> 3 -> 3 -> 5
          prev.next
                                    cur
output:
    1->2->5

val=3
head:
    1  ->  2 ->  3 -> 3 -> 3 -> 3 -> 3
         prev
                                         cur=None
output:
    1->2

input: # caso borde
    1->None
    val=1

Complejidad Espacial: O(1)
Complejidad tiempo: O(N)
'''
def removeElemnts(head, val):
    dummy=ListNode()
    dummy.next=head
    prev, cur= dummy, head

    while cur:
        if cur.val == val:
            cur=cur.next
            prev.next=prev.next.next  
        else:
            prev=cur
            cur=cur.next
    return dummy.next   

# intento 2: implementar eraseNext y luego resolver el problema. Esto está bueno pq demustra que tenés capacidad de descomponer el problema en subproblemas mas abstractos. 
def removeElements(head, val):
     def eraseNext(node):
            node.next=node.next.next
    if not head:
        return None
    cur = head

    while cur.next:
        if cur.next.val == val:
            eraseNext(cur)
        else:
            cur=cur.next
    if head.val == val:
        return head.next
    return head
        