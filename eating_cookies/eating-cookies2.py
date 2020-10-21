# def eating_cookies(n):

#     if n == 1:
#         return 1
#     if n == 2:
#         return 2
#     if n == 3:
#         return 4

#     return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)


# dp = {1: 1, 2: 2, 3: 4}


# def eating_cookies(n):
#     if n not in dp:
#         dp[n] = eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)
#     return dp[n]
