




'''Name: SWAPNIL ARYAN SINHA'''



'''Problem 1'''



# Given a time represented in the format "HH:MM",
# form the next closest time by reusing the current digits.
# There is no limit on how many times a digit can be reused.
# You may assume the given input string is always valid.
# For example, "01:34", "12:09" are all valid. "1:34", "12:9" are all invalid.

def next_closest_time(time_) -> str:
    current = 60 * int(time_[:2]) + int(time_[3:])
    # 24*60 = 1440 (hrs*mins)
    for i in range(current + 1, current + 1440):
        minutes = i % 1440
        h, m = minutes // 60, minutes % 60
        result = "{:02d}:{:02d}".format(h, m)
        if set(result) <= set(time_):
            break

    return result


'''Problem 2'''


# Given n pairs of parentheses,
# write a function to generate all combinations of well-formed parentheses.

def generateParenthesis(n):
    def generate(A=[]):
        if len(A) == 2 * n:
            if valid(A):
                ans.append("".join(A))
        else:
            A.append('(')
            generate(A)
            A.pop()
            A.append(')')
            generate(A)
            A.pop()

    def valid(A):
        bal = 0
        for c in A:
            if c == '(':
                bal += 1
            else:
                bal -= 1
            if bal < 0: return False
        return bal == 0

    ans = []
    generate()
    return ans


'''Problem 3'''


# You are given an array of non-overlapping
# intervals intervals where intervals[i] = [start, end]
# represent the start and the end of the ith interval and intervals is sorted in ascending order by start.
# You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
#
# Insert newInterval into intervals such that intervals is still sorted in ascending order by
# start and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
#
# Return intervals after the insertion.

def insert(intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
    curr_position = 0
    res = []
    while curr_position < len(intervals):
        # smaller than current
        if intervals[curr_position][0] > newInterval[0] and newInterval[1] < intervals[curr_position][0]:
            res.append(newInterval)
            return res + intervals[curr_position:]
        # larger than current
        elif intervals[curr_position][1] < newInterval[0]:
            res.append(intervals[curr_position])
            curr_position += 1
            # merge with current
        elif intervals[curr_position][1] >= newInterval[0]:
            merged_interval = [min(intervals[curr_position][0], newInterval[0]),
                               max(intervals[curr_position][1], newInterval[1])]
            newInterval = merged_interval
            # print(newInterval)
            curr_position += 1
    res.append(newInterval)
    return res


'''Problem 4'''


# Given two sorted arrays nums1 and nums2 of size m and n respectively,
# return the median of the two sorted arrays.
#
# The overall run time complexity should be O(log (m+n)).

def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    a, b = sorted((nums1, nums2), key=len)
    m, n = len(a), len(b)
    low, high = 0, m
    after = int((m + n - 1) / 2)
    while low < high:
        i = int((low + high) / 2)
        if after - i - 1 < 0 or a[i] >= b[after - i - 1]:
            high = i
        else:
            low = i + 1
    i = low
    nextfew = sorted(a[i:i + 2] + b[after - i:after - i + 2])
    return (nextfew[0] + nextfew[1 - (m + n) % 2]) / 2


'''Problem 5'''


# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

def checkInclusion(s1: str, s2: str) -> bool:
    # If the second string is longer or non-existent there can be nor possible permutations
    # of the first string in it.
    if len(s1) > len(s2) or len(s2) == 0:
        return False

    # Set the left and right pointers of our sliding window.
    l, r = 0, 0

    # Declare our frequency hashmaps. We can initialize the second map with our first character
    # from the second string.
    s1_freq, window_freq = {}, {s2[l]: 1}

    # Find the frequencies of all characters in the first string.
    for c in s1:
        if c not in s1_freq:
            s1_freq[c] = 0
        s1_freq[c] += 1

    # Loop through string two.
    while r < len(s2):
        # If our window doesn't have the length of the first string, widen it.
        if r - l + 1 < len(s1):
            r += 1
            # In case we reached the end without a match.
            if r >= len(s2):
                return False

            # If the new character is not in our frequency map, add it.
            if s2[r] not in window_freq:
                window_freq[s2[r]] = 0
            # By now it is in our map and we can increment the frequency.
            window_freq[s2[r]] += 1

        # If our window and the string length match we can compare them.
        if r - l + 1 == len(s1):
            # If the frequencies match, without caring for order (permutations), we can stop.
            if s1_freq == window_freq:
                return True
            # If not we have to move forward.
            else:
                # First decrease the frequency of the left most character in our window.
                window_freq[s2[l]] -= 1
                # If this was the only one we can remove it.
                # This is important or our frequency maps will not match even if they should.
                if window_freq[s2[l]] == 0:
                    window_freq.pop(s2[l])
                # And finally step one to the right.
                # Now window length and s1 length should be out of sync, but we will
                # take care of that in the next iteration.
                l += 1
        # If we find nothing return False.

    return False


'''Problem 6'''


# Given two strings s and t, return true if they are both one edit distance apart, otherwise return false.
# A string s is said to be one distance apart from a string t if you can:
# Insert exactly one character into s to get t.
# Delete exactly one character from s to get t.
# Replace exactly one character of s with a different character to get t.

# time: O(n)
# space: O(n)

def levenshteinDistance(s1, s2):
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    distances = range(len(s1) + 1)
    for i2, c2 in enumerate(s2):
        distances_ = [i2+1]
        for i1, c1 in enumerate(s1):
            if c1 == c2:
                distances_.append(distances[i1])
            else:
                distances_.append(1 + min((distances[i1], distances[i1 + 1], distances_[-1])))
        distances = distances_
    return distances[-1]

'''Main Function'''

if __name__ != '__main__':
    pass
else:
    # 1
    print(next_closest_time("23:59"))
    # 2
    print(generateParenthesis(3))
    # 3
    intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    newInterval = [4, 8]
    print(insert(intervals, newInterval))
    # 4
    print(findMedianSortedArrays(nums1=[1, 2], nums2=[3, 4]))
    # 5
    s1 = 'ab'
    s2 = 'eidbaooo'
    print(checkInclusion(s1, s2))
    #6
    s1 = 'ab'
    s2 = 'aabc'
    print(levenshteinDistance(s1,s2))
