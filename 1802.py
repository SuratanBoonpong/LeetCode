# n = 1
# index = 0
# maxSum = 24
# left,right = 0,maxSum

# def fn(n, x): 
#     if n < x: return n*(2*x-n+1)//2
#     return x*(1+x)//2 + n - x

# while left < right:
#     mid = (left + right + 1) // 2
#     total = fn(index, mid - 1) + fn(n-index, mid)
#     if total <= maxSum:
#         left = mid
#     else:
#         right = mid - 1
#     print(total)
#     print(left)
#     print("----------")




# # def fn(n, x): 
# #             if n < x: return n*(2*x-n+1)//2
# #             return x*(1+x)//2 + n - x
        
# #         lo, hi = 0, maxSum
# #         while lo < hi: 
# #             mid = lo + hi + 1 >> 1
# #             sm = fn(index, mid-1) + fn(n-index, mid)
# #             if sm <= maxSum: lo = mid 
# #             else: hi = mid - 1
# #         return lo 