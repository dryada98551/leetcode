class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_map = {}  # 用來存放 {數字: 索引}

        for i, num in enumerate(nums):
            complement = target - num  # 目標需要的另一個數字
            if complement in num_map:
                return [num_map[complement], i]  # 回傳組成 target 的兩個數字的索引
            num_map[num] = i  # 把當前的數字和它的索引存進 map
            print(i,num)
            print(num_map)
        
if __name__ == '__main__':
    nums = [3,2,4]
    target = 6
    sol = Solution()
    sol.twoSum(nums, target)