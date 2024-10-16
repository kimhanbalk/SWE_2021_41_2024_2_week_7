from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    
    numDict = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in numDict:
            return [numDict[complement], i]
        numDict[num] = i
    return []

