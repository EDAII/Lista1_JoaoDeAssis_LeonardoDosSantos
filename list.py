class Node:
    def __init__(self,data):
        self.next= None
        self.prev = None
        self.data = Item(data)
class Item:
    def __init__(self,name):
        self.name = name
        self.nSearch = 0

class List:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_front(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head = new_node

    def search(self, name):
        current = self.head
        while True:
            if current.data.name == name:
                current.data.nSearch +=1
                return True
            elif current != self.tail:
                current = current.next
            else:
                return False
    
    #TODO implementar a autoorganização


    def autoSort(self,i): #método para organizar a lista de acordo com o numero de pesqu
                          #i é o valor inicial a ser ordenado e percorre a lista até chegar ao topo
        while i.data.nSearch > i.next.data.nSearch and i!=self.head:
            print(i.data.name)
            self.swap(i,i.prev)
        return i


    def print(self):
        current = self.head
        while(True):
            print(current.data.name + " " + str(current.data.nSearch))
            if(current == self.tail):
                break
            current=current.next
            
            
            
    def swap(self,a,b): ##Método para trocar dois nodes de lugar
        temp = a
        a.next = b.next
        a.prev = b.prev
        b.next = temp.next
        b.prev = temp.prev

        if a == self.head:
            self.head=b
        elif b==self.head:
            self.head=a
        
        if b==self.tail:
            self.tail = a
        elif a==self.tail:
            self.tail = b