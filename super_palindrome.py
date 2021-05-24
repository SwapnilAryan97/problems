'''
super palindrome = a palindromic number whose square root is also a palindrome
left and right are range inputs, and 1<=left<=right<=(10^18)-1

Using DP, we create our own palindromes and check if their squares are
palindromes and if they lie between left and right.
Complexity: 10^18 is not needed to be traversed we go only half of those digits:
hence (10^18)^1/2 = 10^9
Since we're traversing only through the square roots, we need half of the digits,
hence (10^9)^1/2 = 10^(4.5) so we need to only traverse through only 10^5 numbers.
'''


class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        count = 0
        left, right = int(left), int(right)
        '''Odd integers'''
        for i in range(10 ** 5):
            s = str(i)
            s = s + s[-2::-1]  # palindrome
            y = int(s) ** 2  # palindrome square
            if y > right:
                break
            if y >= left and y == int(str(y)[::-1]):
                count = count + 1
        '''Even integers'''
        for i in range(10 ** 5):
            s = str(i)
            s = s + s[::-1]  # palindrome
            y = int(s) ** 2  # palindrome square
            if y > right:
                break
            if y >= left and y == int(str(y)[::-1]):
                count = count + 1
        return count


def main():
    value = Solution()
    print(value.superpalindromesInRange('1','10')) # [1,4,9] -> 3
    print(value.superpalindromesInRange('40000000000000000', '50000000000000000'))


if __name__ == '__main__':
    main()