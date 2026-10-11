class MedianFinder:

    def __init__(self):
        self.data = []

    def addNum(self, num: int) -> None:
        
        obj  = MedianFinder()
        self.data.append(num)

    def findMedian(self) -> float:
        self.data.sort()
        n = len(self.data) 
        if n &1:
            return float(self.data[n//2])
        return (self.data[n//2] + self.data[n//2-1]) / 2 
        