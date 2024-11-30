'''
Given the head of a linked list, return the list after sorting it in ascending order.

input:
    2 -> 1 -> 4 -> -2 -> 5

output:
    -2 -> 1 -> 2 -> 4 -> 5

my first idea is to have a list where we keep track of all the values, we sort them
and then we traverse again the new list and assign the respective value

Time: O(2n)
Space: O(n)
'''
def sortList(head):
    tmp=head
    values=[]

    while tmp:
        values.append(tmp.val)
        tmp=tmp.next
    
    values.sort()
    cur=head
    i=0
    while cur:
        cur.val=values[i]
        cur = cur.next
        i+=1
    return head