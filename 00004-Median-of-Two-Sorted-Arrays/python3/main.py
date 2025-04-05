class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        # 子函式：找出兩個排序陣列中第 k 小的元素
        def find_kth(a, b, k):
            print(a, b, k)
            # 保證 a 是比較短的那個陣列，這樣不會越界
            if len(a) > len(b):
                return find_kth(b, a, k)
            
            # 如果 a 是空的，那第 k 小一定在 b 裡
            if not a:
                return b[k - 1]
            
            # 如果只要找第 1 小的元素，直接回傳兩者最小的，也是遞迴終止位置
            if k == 1:
                return min(a[0], b[0]) 

            # 取 k // 2 個元素，比較兩邊的分界值
            i = min(k // 2, len(a))  # a 中實際能取的元素數量
            j = k - i                # b 中要取剩下的元素
            print(i, j)
            print(a[i-1], b[j-1])

            # 比較 a[i - 1] 和 b[j - 1]，誰比較小代表誰前面那段不可能是第 k 小
            if a[i - 1] < b[j - 1]:
                # 把 a 的前 i 個元素丟掉，繼續找第 k - i 小
                return find_kth(a[i:], b, k - i)
            else:
                # 把 b 的前 j 個元素丟掉，繼續找第 k - j 小
                return find_kth(a, b[j:], k - j)

        # 主邏輯：計算總長度
        total_len = len(nums1) + len(nums2)

        # 如果總長度是奇數，直接找第 (n//2 + 1) 小的數
        if total_len % 2 == 1:
            return find_kth(nums1, nums2, total_len // 2 + 1)
        else:
            # 如果是偶數，找中間兩個數，取平均
            left = find_kth(nums1, nums2, total_len // 2)
            right = find_kth(nums1, nums2, total_len // 2 + 1)
            return (left + right) / 2


# 🔧 測試用例
if __name__ == '__main__':
    nums1 = [1, 3, 5, 7, 9]
    nums2 = [1, 2, 4, 6, 8, 9, 10, 12]
    sol = Solution()
    result = sol.findMedianSortedArrays(nums1, nums2)
    print(result)  # 應該輸出中位數
