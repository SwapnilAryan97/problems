'''Problem 1'''
# Given an integer array nums, move all 0's to the end of it while maintaining
# the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.

# Time = O(n)
# Space = O(1)

def order(nums):
    location = 0
    n = len(nums)
    for i in range(n):
        if nums[i] != 0:
            nums[location] = nums[i]
            location += 1
    for i in range(location, n):
        nums[i] = 0
    return nums


'''Problem 2'''
# Given an array nums containing n distinct numbers
# in the range [0, n], return the only number in the range
# that is missing from the array.

# Time = O(n)
# Space = O(1)


def find_number(nums):
    # start = time.time()
    n = len(nums)
    if n < 2: return nums
    mini = float('inf')
    maxi = float('-inf')
    for val in nums:
        if val < mini: mini = val
        if val > maxi: maxi = val
    if mini == 0:
        mini = 1
    target = n * (mini + maxi) // 2
    for val in nums:
        # print(target)
        target = target - val
    # print(time.time() - start)
    return target


'''Problem 3'''
# Given a string s and an integer k,
# return the length of the longest substring of s that
# contains at most k distinct characters.

def kUnique(s, k):
    u = 0  # number of unique characters
    n = len(s)
    # storing the count of every letter
    count = [0] * 26
    # traverse the string and store the values
    for i in range(n):
        if count[ord(s[i]) - ord('a')] == 0:
            u += 1
        count[ord(s[i]) - ord('a')] += 1

    # if not enough unique characters
    if u < k:
        print('Not enough unique characters')
        return

    # make a window with first element in it
    # start and end variables
    curr_start = 0
    curr_end = 0

    # initialize values for longest window
    max_window_size = 1
    # max_window_start = 0

    # Initialize associative array count[] again
    count = [0] * 26

    count[ord(s[0]) - ord('a')] += 1  # put first character

    for i in range(1, n):
        # Add the character 's[i]' to current window
        count[ord(s[i]) - ord('a')] += 1
        curr_end += 1

        # if there are more than k unique values in the window, remove from left side
        while not isValid(count, k):
            count[ord(s[curr_start]) - ord('a')] -= 1
            curr_start += 1

        # update max window size when required
        if curr_end - curr_start + 1 > max_window_size:
            max_window_size = curr_end - curr_start + 1

    return max_window_size


def isValid(count, k):
    val = 0
    for i in range(26):
        if count[i] > 0:
            val += 1

    # Return true if k is greater than or equal to val
    return k >= val


'''Problem 4'''
# A peak element is an element that is strictly greater than its neighbors.
#
# Given an integer array nums, find a peak element, and return its index.
# If the array contains multiple peaks, return the index to any of the peaks.

# Time = O(n)
# Space = O(1)

def peak(nums):
    n = len(nums)
    if n < 3: return 'array too short'

    for i in range(1, n - 1):
        if nums[i - 1] < nums[i] > nums[i + 1]:
            return i


if __name__ == '__main__':
    import time

    # 1
    print(order([0, 1, 0, 3, 12, 13, 0, 6, 0, 7]))
    # 2
    print(find_number([9, 6, 4, 2, 3, 5, 7, 0, 1]))
    # 3
    print(kUnique("echhebbabaabb", 1))
    # 4
    print(peak([1, 2, 1, 3, 5, 6, 4]))
