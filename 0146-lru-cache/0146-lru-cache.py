class LRUCache:

    class Node:
        
        def __init__(self, key: int, value: int):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None


    def __init__(self, capacity: int):
            self.capacity = capacity
            self.cache = {}
            self.head = self.Node(-1,-1)
            self.tail = self.Node(-1,-1)
            self.head.next = self.tail
            self.tail.prev = self.head
            
    def remove_node(self, node: 'Node') -> None:
        curr = node
        curr.prev.next = curr.next
        curr.next.prev = curr.prev
    
    def insertat_head(self, node: 'Node') -> None:
        curr = node
        curr.next = self.head.next
        curr.prev = self.head
        curr.next.prev = curr
        self.head.next = curr
        
        

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove_node(node)
            self.insertat_head(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.remove_node(node)
            self.insertat_head(node)
        else:
            if len(self.cache) >= self.capacity:
                lru = self.tail.prev
                self.remove_node(lru)
                del self.cache[lru.key]
        
            new_node = self.Node(key, value)
            self.insertat_head(new_node)
            self.cache[key] = new_node
        
            
            
            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)