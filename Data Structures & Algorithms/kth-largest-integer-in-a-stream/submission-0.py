class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums

    def add(self, val: int) -> int:
        
        self.heap.append(val)
        self.heap.sort()
        return self.heap[len(self.heap)-self.k]

        # cur = len(self.heap) - 1

        # while cur > 0 and self.heap[cur] > self.heap[]