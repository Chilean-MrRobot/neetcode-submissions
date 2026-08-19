class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        setOranges = set()
        setRotten = set()
        counter = 0
        for i, row in enumerate(grid):
            for j, value in enumerate(row):
                if value == 1:
                    setOranges.add((i,j))
                elif value == 2:
                    setRotten.add((i,j))
        print(setOranges)
        print(setRotten)
        print("-")
        if setOranges == setRotten:
            return 0
        setRottenPrevious = set()
        while (setRotten != setRottenPrevious) and (len(setOranges) != 0):
            setRottenPrevious = setRotten.copy()
            for rottenElement in setRottenPrevious:
                i, j = rottenElement
                setRotten.add((i-1,j))
                setRotten.add((i,j-1))
                setRotten.add((i+1,j))
                setRotten.add((i,j+1))
            setRotten = setRotten.intersection(setOranges).union(setRottenPrevious)
            print(setRotten)
            setOranges = setOranges - setRotten
            print(setOranges)
            counter += 1
            print(counter)
        if setRotten == setRottenPrevious:
            return -1
        return counter
        