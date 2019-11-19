class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 

def display(head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next
class Solution: 
    def insert(self,head,data):
            p = Node(data)           
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head  
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next
        

    def removeDuplicates(self,head):
        copyHead = head
        values = [head.data]
        while copyHead.next != None:
            if copyHead.next.data not in values:
                values.append(copyHead.next.data)
                copyHead = copyHead.next
            else:
                copyHead.next = copyHead.next.next
           
        return head

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
head=mylist.removeDuplicates(head)
mylist.display(head); 