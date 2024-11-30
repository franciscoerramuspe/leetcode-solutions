'''
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. 

If the two linked lists have no intersection at all, return null.

The test cases are generated such that there are no cycles anywhere in the entire linked structure.

Note that the linked lists must retain their original structure after the function returns.

Custom Judge:

The inputs to the judge are given as follows (your program is not given these inputs):

intersectVal - The value of the node where the intersection occurs. This is 0 if there is no intersected node.
listA - The first linked list.
listB - The second linked list.
skipA - The number of nodes to skip ahead in listA (starting from the head) to get to the intersected node.
skipB - The number of nodes to skip ahead in listB (starting from the head) to get to the intersected node.
The judge will then create the linked structure based on these inputs and pass the two heads, headA and headB to your program. If you correctly return the intersected node, then your solution will be accepted.

assuming both lists can have the same values
we can traverse one list first, and have a visited set to store all the nodes
then we traverse the remaining list
as soon as we find a node that we already visited, we return that one
if we never find a node where they intersect and we finish traversing both of them, return None
Time:O(n+m)
Space:O(n+m)
'''
def intersectionOfTwoLinkedLists(headA, headB):
        if not headA or not headB:
            return None

        visited=set()
        curA, curB=headA, headB
        while curA:
            if curA in visited:
                return curA
            visited.add(curA)
            curA=curA.next
        while curB:
            if curB in visited:
                return curB
            visited.add(curB)
            curB=curB.next
        return None