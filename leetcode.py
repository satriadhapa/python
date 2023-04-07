# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         seen = {}
#         for i, num in enumerate(nums):
#             complement = target - num
#             if complement in seen:
#                 return [seen[complement], i]
#             seen[num] = i

# class Solution:
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#         carry = 0
#         dummy = ListNode(0)
#         curr = dummy
#         while l1 or l2 or carry:
#             sum = carry
#             if l1:
#                 sum += l1.val
#                 l1 = l1.next
#             if l2:
#                 sum += l2.val
#                 l2 = l2.next
#             carry = sum // 10
#             curr.next = ListNode(sum % 10)
#             curr = curr.next
#         return dummy.next

# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         m, n = len(nums1), len(nums2)
#         if m > n:
#             nums1, nums2, m, n = nums2, nums1, n, m
#         i_min, i_max, half_len = 0, m, (m + n + 1) // 2
#         while i_min <= i_max:
#             i = (i_min + i_max) // 2
#             j = half_len - i
#             if i < m and nums2[j-1] > nums1[i]:
#                 i_min = i + 1
#             elif i > 0 and nums1[i-1] > nums2[j]:
#                 i_max = i - 1
#             else:
#                 if i == 0:
#                     max_left = nums2[j-1]
#                 elif j == 0:
#                     max_left = nums1[i-1]
#                 else:
#                     max_left = max(nums1[i-1], nums2[j-1])
#                 if (m + n) % 2 == 1:
#                     return max_left
#                 if i == m:
#                     min_right = nums2[j]
#                 elif j == n:
#                     min_right = nums1[i]
#                 else:
#                     min_right = min(nums1[i], nums2[j])
#                 return (max_left + min_right) / 2.0

# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         n = len(s)
#         dp = [[False] * n for _ in range(n)]
#         res = ""
#         for i in range(n):
#             dp[i][i] = True
#             res = s[i]

#         for i in range(n-1):
#             if s[i] == s[i+1]:
#                 dp[i][i+1] = True
#                 res = s[i:i+2]

#         for i in range(n-3, -1, -1):
#             for j in range(i+2, n):
#                 if dp[i+1][j-1] and s[i] == s[j]:
#                     dp[i][j] = True
#                     if j-i+1 > len(res):
#                         res = s[i:j+1]

#         return res


