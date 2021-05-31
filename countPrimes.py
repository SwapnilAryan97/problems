"""
1 <= n <= 5*10^6
for n=0,1 -> return 0

Complexity: O(n^(0.5) + (n-i^2))
"""

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        prime = [True] * n
        i = 2
        while i * i < n:
            if prime[i]:
                for j in range(i * i, n, i):
                    prime[j] = False
            i += 1
        return prime.count(True) - 2


def main():
    prime = Solution()
    n = 5 * (10 ** 6)
    print('There are', prime.countPrimes(n),'prime numbers from 0 to',n)


if __name__ == '__main__':
    main()