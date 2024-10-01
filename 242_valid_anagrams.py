"""242. Valid anagrams:

https://leetcode.com/problems/valid-anagram/description/
https://www.youtube.com/watch?v=9UtInBqnCgA
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """Given two strings s and t, return true if t is an anagram of s,
        and false otherwise.

        Complexity:
            Time: O(n)
            Space: O(n)
        
        Where n = len(s) = len(t) (if it is an anagram)

        Else if the strings are not anagrams, then the time complexity is O(n + m)
        """
        letter_counts = {}

        # iterate through first string, add the letters.
        for letter in s:
            if letter in letter_counts:
                letter_counts[letter] += 1
            else:
                letter_counts[letter] = 1

        # iterate through the second string, subtract the letters
        for letter in t:
            if letter in letter_counts:
                letter_counts[letter] -= 1
            # if there is a letter
            else:
                return False
        for letter in letter_counts:
            # If the letter count is not zero, then the strings are not anagrams
            # since there are extra letters in one of the strings
            if letter_counts[letter] != 0:
                return False
        return True


def test_case_1():
    s = "anagram"
    t = "nagaram"
    assert Solution().isAnagram(s, t) == True


def test_case_2():
    s = "rat"
    t = "car"
    assert Solution().isAnagram(s, t) == False


def test_case_3():
    s = "a"
    t = "ab"
    assert Solution().isAnagram(s, t) == False

if __name__ == "__main__":
    test_case_1()
    test_case_2()
    test_case_3()
    print("All test cases pass")
