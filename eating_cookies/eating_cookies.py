'''

Understand the problem:
    What is the main goal?
        Implement a fx that counts the number of possible
        ways a Cookie Monster can eat all of the cookies in 
        the jar
        
    What data do I have ?
        Cookie monster can eat 1,2 or 3 cookies at a time
        The fx recieves an N number of cookies
    
    What data or input should the fx return ?
        should return an interger representing 
        the numbers of ways the Cookie Monster 
        can eat given N cookies in Jar

Analysis:
    How can I determine X given N number of cookies ?
    What am I passing into the function?
    What kind of data structures could I use or learn from ?
    Is there any built-in python fx I could use?
    What kind of similar problems are out there?
    Is there a specific formula for this ?
    

High Level Algorithm:
    Take in N number of cookies
    Determine how many different ways N could be eaten
    return the value with answer
    
More details:
    Take in N number of cookies
        N = 5
    Determine how many different ways N could be eaten
       3 + 2 = 5
       3 + 1 + 1 = 5
       1 + 1 + 1 + 1 + 1 = 5
       2 + 2 + 1
       2 + 1 + 1 + 1
       
    return the value with answer
            return ways
    
'''

'''
Input: an integer
Returns: an integer

_ _ _ _

1 2 3 4

F(1)=1
F(2)=2
F(3)=4

F(4) = F(3) +  F(2) + F(1) = 4 + 2+ 1 = 7
F(5) = F(4) + F(3) + F(2) = 7 + 4 + 2 = 13
F(6) = F(5) + F(4) + F(3)

F(n) = F(n-1) + F(n-2) + F(n-3)

F(5) = 1 + 1+ 1+ 1+ 1
    = 1 + 1 + 1+  2 = 1+ 1 + 2+ 1 = 1+2+ 1+ 1 = 2+1+1+1 = 2+2+1 = 1+ 2 +2 = 2+1+2
    = 1+1+3 = 3+1+1 = 1+3+1
    = 2+3 = 3+2


 '''

# For example, for a jar of cookies with `n = 3` (the jar has 3 cookies inside it), there are 4 possible ways for Cookie Monster to eat all the cookies inside it:

#  1. He can eat 1 cookie at a time 3 times
#  2. He can eat 1 cookie, then 2 cookies
#  3. He can eat 2 cookies, then 1 cookie
#  4. He can eat 3 cookies all at once.

# dp = {1: 1, 2: 2, 3: 4}


# def eating_cookies(n):
#     if n not in dp:
#         dp[n] = eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)
#     return dp[n]


import sys
sys.setrecursionlimit(100)


def eating_cookies(n):

    if n <= 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4

    return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)

# def eating_cookies(n):
#     print(n)
#     if n < 0:
#         return 0
#     if n == 0:
#         return 1
#     return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(
        f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
