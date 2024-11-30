'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list.

The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

input:
list1: 1 -> 2 -> 5
list2: 2 -> 3 -> 4

        1 -> 2 -> 5
        prev l1
        2 -> 3 -> 4
             l2


output: 1 -> 2 -> 2 -> 3 -> 4 -> 5

start at the head of both lists
compare each value
whichever value is smaller would go in the next pointer
we create a dummy node and a prev ptr that will point to dummy
while both lists are not empty, make prev.next point to the smallest value
then move that smallest value forward
then move prev to prev.next
repeat until one pf them is empty
attach the remaining of the nonempty list to prev.next
return dummy.next

Time: O(n+m) where n and m are the lengths of each list
Space: O(1)
'''
class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next
    
def mergeTwoSortedLists(list1, list2):
    dummy=Node()
    prev=dummy
    l1, l2 = list1, list2

    while l1 and l2:
        if l1.val<l2.val:
            prev.next=l1
            l1=l1.next
            prev=prev.next
        else:
            prev.next=l2
            l2=l2.next
            prev=prev.next
    prev.next=l1 or l2
    return dummy.next
