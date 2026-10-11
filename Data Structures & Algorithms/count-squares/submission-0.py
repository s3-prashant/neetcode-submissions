class CountSquares:

    def __init__(self):
        
        self.square = []
        self.ptcount = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.ptcount[tuple(point)] += 1
        self.square.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        for x,y in self.square:
            if (abs(x-y)!= abs(px-py)) or x==px or y ==py:
                continue
            res+= self.ptcount[(x,py)] * self.ptcount[(px,y)]
        return res
