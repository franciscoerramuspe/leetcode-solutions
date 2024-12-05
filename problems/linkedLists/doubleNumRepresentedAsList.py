'''
You are given the head of a non-empty linked list representing a non-negative integer without leading zeroes.

Return the head of the linked list after doubling it.



if list is 1->2->4
num=124
output=124x2=248
2->4->8

traverse the list, get all the digits and merge them into an int
multiply this int by 2
split each digit in an array

traverse the list again, assign the new values in the order of the array.
If more digits were added to the new number compared to the prev one, create a new node and assign the respective val

time: O(2N)
Space: O(n)
'''
import sys
sys.set_int_max_str_digits(1000000)
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        numToDouble=''
        cur=head
        
        while cur:
            numToDouble+=str(cur.val)
            cur=cur.next
        
        numToDouble=int(numToDouble)*2
        digits=[int(i) for i in str(numToDouble)]
        cur=head
        i=0
        
        while cur:
            if not cur.next and i<len(digits)-1:
                cur.val=digits[i]
                i+=1
                cur.next=ListNode(val=digits[i])
                cur=cur.next
            else:
                cur.val=digits[i]
                i+=1
                cur=cur.next
        return head

#intento 2: hacer la misma implementacion pero usando una implementacion de List que tenga pushright, 
# TAREA 2: hacerlo en O(1) de memoria auxiliar (vas a usar O(n) para el output, pero sin tener en cuenta eso, o sea sin usar la lista digits)
def doubleNumRepresentedAsLl(head):
    def pushVal(curNode, val):
            if not curNode.next and i==len(number)-2:
                print('here')
                curNode.next=ListNode()
            
            curNode.val=val

        
    cur=head
    number=''

    while cur:
        number+=str(cur.val)
        cur=cur.next

    number=str(int(number) *2)
    cur=head
    i=0

    print(number)
    while i<len(number):
        pushVal(cur, int(number[i]))
        cur=cur.next
        i+=1
    return head