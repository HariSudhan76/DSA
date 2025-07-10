class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i=0
        j=len(numbers)-1
        while i<j:
            sol = numbers[i]+numbers[j]
            if sol == target:
                return [i+1,j+1]
            if sol>target:
                j-=1
            else:
                i+=1