class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        for num1 in nums1:
            flag_found = False
            for num2 in nums2:
                if num1 == num2:
                    flag_found = True
                elif flag_found and num2 > num1:
                    stack.append(num2)
                    break
            else:
                stack.append(-1)
        return stack