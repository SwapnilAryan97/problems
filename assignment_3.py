'''Problem 1'''

# Given two strings s and t, return true if they are both one edit distance apart, otherwise return false.
# A string s is said to be one distance apart from a string t if you can:
# Insert exactly one character into s to get t.
# Delete exactly one character from s to get t.
# Replace exactly one character of s with a different character to get t.

def one_edit(s1, s2):
    if len(s2) > len(s1):
        temp = s1
        s1 = s2
        s2 = temp
    n1 = len(s1)
    n2 = len(s2)
    if abs(n1 - n2) > 1: return False
    if n1 == 0 and n2 == 0:
        return False
    dict = {}
    count = 0
    for val in s1:
        if val not in dict:
            dict[val] = 1
            count += 1
        else:
            dict[val] += 1
            count += 1
    for val in s2:
        if val in dict and dict[val] != 0:
            dict[val] -= 1
            count -= 1
    if count == 1:
        return True
    else:
        return False


'''Problem 2'''

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.

def anagram(s1, s2):
    import collections
    return collections.Counter(s1) == collections.Counter(s2)


'''Problem 3'''

# Given a sorted array of distinct integers and a target value,
# return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.

def find_index(arr, start, end, target):
    if end > start:
        mid = end - start // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return find_index(arr, mid + 1, end, target)
        else:
            return find_index(arr, start, mid - 1, target)
    else:
        return start


'''Problem 4'''

# Given two sparse matrices mat1 of size m x k and mat2 of size k x n, return the result of mat1 x mat2.
# You may assume that multiplication is always possible.

def matrix_mul(l1, l2):
    res = [[0 for x in range(len(l2))] for y in range(len(l1))]
    # print(res)
    for i in range(len(l1)):
        for j in range(len(l1[0])):
            for k in range(len(l2)):
                res[i][j] += l1[i][k]*l2[k][j]

    return res




'''Main Function'''

if __name__ == '__main__':
    # 1
    print(one_edit('', 'a'))
    # 2
    print(anagram('rat', 'car'))
    # 3
    arr = [1, 2, 3, 4, 6, 8, 9]
    target = 7
    print(find_index(arr, 0, len(arr) - 1, target))
    # # 4
    l1 = [[1,0,0],[-1,0,3]]
    l2 = [[7,0,0],[0,0,0],[0,0,1]]
    print(matrix_mul( l1, l2))
