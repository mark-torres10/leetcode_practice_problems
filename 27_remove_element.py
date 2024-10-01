from typing import List

## My first attempt ##
# Logic: Traverse the array backwards and replace the value at the current index
# with the value at the next index.
# Doesn't work lol.
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        len_nums = len(nums)
        num_equal = 0
        k = 0
        for i in range(len_nums - 1, -1, -1):
            # traverse it backwards?
            if nums[i] == val:
                for j in range(i+1, len_nums - num_equal):
                    # replace the previous element with the element after it
                    nums[j-1] = nums[j]
                k += 1
        return k
    

# what if we try to do it in one forward pass?
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """We can use a pointer to keep track of the next position to replace.
        If the current value is not equal to val, we replace the value at the pointer
        with the current value and increment the pointer.

        The pointer will tell us where to put our next valid value. It should be
        equal to or behind the actual `i` index. 

        When we see a value that is not equal to val, we replace the value at the
        pointer with the current value and increment the pointer. If we see a value
        that is equal to val, we skip. This will increase the index `i` but then keep
        our pointer in the same place.

        Time complexity: O(n)
        Space complexity: O(1)
        """
        len_nums = len(nums)
        pointer = 0
        for i in range(len_nums):
            if nums[i] == val:
                # skip the value by passing it with the pointer.
                continue
            nums[pointer] = nums[i]
            pointer += 1
        return pointer

# video walkthrough solution: https://www.youtube.com/watch?v=Pcd1ii9P9ZI
