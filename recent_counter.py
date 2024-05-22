class RecentCounter:

    def __init__(self):
        self.queue = deque() # O(1) append and delete ops
        
    def ping(self, t: int) -> int:
        self.queue.append(t) # appends t to end of queue
        while self.queue[0] < t - 3000:
            self.queue.popleft() # removes from front of queue
        
        return len(self.queue)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
