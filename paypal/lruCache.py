class Node:
    def __init__(self,value,key):
        self.value = value
        self.key = key
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hm = {}
###dono ko alag alag define kar         
        self.tail = Node(-1,-1)
        self.head = Node(-1,-1)
        self.tail.next = self.head
        self.head.prev = self.tail    
        self.length = 0

        
    def get(self, key: int) -> int:
        if key in self.hm:
            pivot_node = self.hm[key]
            pivot_node.prev.next = pivot_node.next
            pivot_node.next.prev = pivot_node.prev

            pivot_node.next = self.head
            pivot_node.prev = self.head.prev
            pivot_node.prev.next = pivot_node
            self.head.prev = pivot_node

            return self.hm[key].value
        else:
            return -1    
        

    def put(self, key: int, value: int) -> None:
        if key in self.hm:
            pivot_node = self.hm[key]
            pivot_node.prev.next = pivot_node.next
            pivot_node.next.prev = pivot_node.prev

            pivot_node.next = self.head
            pivot_node.prev = self.head.prev
            pivot_node.prev.next = pivot_node
            self.head.prev = pivot_node
            
            self.hm[key].value = value
        else:
            pivot_node = Node(value,key)
            self.hm[key] = pivot_node
            pivot_node.next = self.head
            pivot_node.prev = self.head.prev
            pivot_node.prev.next = pivot_node
            self.head.prev = pivot_node
            self.length+=1
            if self.length>self.capacity:
                print (self.tail.next.key)
                del self.hm[self.tail.next.key]
                self.tail.next = self.tail.next.next
                self.tail.next.prev = self.tail

             
        

               



       

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)