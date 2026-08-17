class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        returnList = []

        def recursiveDumping(numsList: List[int], returnList: List[List[int]]) -> List[List[int]]:
            if numsList not in returnList:
                returnList.append(numsList)

            if len(numsList) > 0:
                for i, i_value in enumerate(numsList):
                    if i > 0 and numsList[i] == numsList[i-1]:
                        continue
                    returnList = recursiveDumping(numsList[:i] + numsList[i+1:], returnList)

            return returnList

        returnList = recursiveDumping(nums, returnList)
        return returnList