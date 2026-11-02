class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        #block = blocks[0:k]
        whites = 0
        min_whites = 0
        i = 0
        for j, value in enumerate(blocks):
            if j < k:
                if value == "W":
                    whites += 1
                    min_whites += 1
                continue
            else:
                if blocks[i] == "W":
                    whites -= 1
                if blocks[j] == "W":
                    whites += 1
                i += 1
                min_whites = min(min_whites, whites)
        return min_whites