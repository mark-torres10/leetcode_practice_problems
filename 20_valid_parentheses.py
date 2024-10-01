class Solution:
    def isValid(self, s: str) -> bool:
        """
        Time complexity: O(n)
            - We traverse the string once.
        Space complexity: O(n)
            - We use a stack to store the unclosed characters.
        """
        if len(s) == 0:
            return False
        matching_chars = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        unclosed_chars = []
        for char in s:
            if char in matching_chars.keys():
                unclosed_chars.append(char)
            else:
                # if there is a right-char and there are no left chars
                if len(unclosed_chars) == 0:
                    return False
                latest_unclosed_char = unclosed_chars.pop()
                if char != matching_chars[latest_unclosed_char]:
                    return False
        return len(unclosed_chars) == 0

    def isValid_v2(self, s: str) -> bool:
        """
        Optimized version of the above solution.

        Time complexity: O(n)
            - We traverse the string once.
        Space complexity: O(n)
            - We use a stack to store the unclosed characters.
        """
        stack = []
        matching_chars = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in matching_chars:
                if not stack or stack[-1] != matching_chars[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        return len(stack) == 0
