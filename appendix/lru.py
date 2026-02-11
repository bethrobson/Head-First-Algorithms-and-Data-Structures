class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}  # key -> Node

        # Dummy head and tail nodes
        self.head = Node(None, None)  # Most recent side
        self.tail = Node(None, None)  # Least recent side
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def _add_to_front(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    # Cache operations

    def get(self, key):
        if key not in self.cache:
            return None

        node = self.cache[key]
        self._remove(node)
        self._add_to_front(node)
        return node.value

    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._remove(node)
            self._add_to_front(node)
        else:
            if len(self.cache) >= self.capacity:
                # Evict LRU (node before tail)
                lru = self.tail.prev
                self._remove(lru)
                del self.cache[lru.key]

            node = Node(key, value)
            self.cache[key] = node
            self._add_to_front(node)

    # Print cache from most recent -> least recent
    def __repr__(self):
        result = []
        curr = self.head.next
        while curr != self.tail:
            result.append(f"{curr.key}:{curr.value}")
            curr = curr.next
        return " <- ".join(result)

cache = LRUCache(3)

cache.put("a", 1)
cache.put("b", 2)
cache.put("c", 3)
print(cache)  # c <- b <- a

cache.get("a")
print(cache)  # a <- c <- b

cache.put("d", 4)  # evicts b
print(cache)  # d <- a <- c


