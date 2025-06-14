class Node:
    def __init__(self,value,):
        self.value = value
        self.next=None


class Queue:
    def __init__(self,value):
        new_node=Node(value)
        self.first=new_node
        self.last=new_node
        self.lenght=1


    def print_queue(self):
        temp=self.first
        while temp is not None:
            print(temp.value)
            temp=temp.next


    def enqueue(self,value):
        new_node=Node(value)
        if self.first is None or self.last is None:
            self.first=new_node
            self.last=new_node
        else:

                self.last.next=new_node
                self.last=new_node
                self.lenght+=1

        self.lenght+=1


    def dequeue(self):
        temp=self.first
        if self.lenght==0:
            return None

        if self.lenght==1:
            self.first=None
            self.last=None
        else:
            self.first=self.first.next
            temp.next=None
        self.lenght-=1

        return temp

        








queue=Queue(3)
queue.enqueue(2)
queue.print_queue()

