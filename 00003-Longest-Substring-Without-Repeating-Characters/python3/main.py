class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}  # 用來記錄字元上次出現的位置
        left = 0         # 滑動窗口左邊界
        max_length = 0

        for right in range(len(s)):
            if s[right] in char_index and char_index[s[right]] >= left:
                # 發現重複字元：更新左邊界，更新到前一個重複字元下一位
                left = char_index[s[right]] + 1
            
            # 更新當前字元的最新位置
            char_index[s[right]] = right

            # 計算目前窗口大小
            max_length = max(max_length, right - left + 1)
            print(char_index, left, right)

        return max_length


if __name__ == '__main__':
    s = "pwswkew"
    sol = Solution()
    result = sol.lengthOfLongestSubstring(s)
    print(result)