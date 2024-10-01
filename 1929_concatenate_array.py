from typing import List

class Solution:
    def concatenate_array(self, nums: List[int]) -> List[int]:
        """Concatenates two arrays to each other.
        
        Time complexity: O(n)
            - It needs to traverse the array twice.
            - If n = len(nums), then it needs to traverse the array twice.
            - 2n operations -> O(n)
        Space complexity: O(n)
            - It needs to create a new array to store the concatenated array.
            - 2n space.
        """
        return nums + nums
    

    def concatenate_array_v2(self, nums: List[int]) -> List[int]:
        """Concatenates two arrays to each other.
        
        Approach appends to an existing array in-place.

        In theory, it's the same time and space complexity (O(n)) as
        before, but in practice it can possibly be more efficient. This is
        because lists in Python are dynamic arrays, and resizing them is an
        expensive operation. Therefore, Python overallocates memory for a given
        list. This means that when we append to a list, we first use any space
        that may have been overallocated, and then Python will go and resize
        the list.
        """
        len_nums = len(nums)
        for i in range(len_nums):
            nums.append(nums[i])
        return nums
