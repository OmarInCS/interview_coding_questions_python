"""

5. Prime or Not?
In this challenge, determine whether a number is prime. If it is not, partially factor the number to determine its lowest value divisor greater than 1.


For example, the number n = 24 is not prime. Its divisors are [1, 2, 3, 4, 6, 8, 12, 24].  The smallest divisor greater than 1 is 2.


Function Description

Complete the function isPrime in the editor below. The function must return the integer 1 if the number is prime. Otherwise, return the smallest divisor greater than 1.

isPrime has the following parameter(s):

    n:  a long integer to test


Constraints

2 ≤ n ≤ 1012
Input Format for Custom Testing
Input from stdin will be processed as follows and passed to the function.


The only line of input contains the long integer to analyze, n.

Sample Case 0
Sample Input 0
2
Sample Output 0
1

Explanation 0
As 2 is a prime number, the function returns 1.


Sample Case 1
Sample Input 1
4
Sample Output 1
2

Explanation 1
Since 4 is not a prime number, and the factors of 4 are [1, 2, 4], the function returns the smallest factor of 4 greater than 1.

"""


def is_prime(n: int):
    factors = [1]

    for div in range(2, n + 1):
        if n % div == 0:
            factors.append(div)

    return 1 if len(factors) == 2 else factors[1]


print(is_prime(int(input())))

