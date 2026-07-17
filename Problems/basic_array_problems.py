# ============================================================
# ARRAY PRACTICE QUESTIONS (DSA WITH PYTHON)
# Solve without using built-in functions like max(), min(), sum()
# unless the question specifically allows them.
# ============================================================


# ------------------------------------------------------------
# Question 1: Find the Largest Element
#
# Write a function that returns the largest element in the array.
#
# Example:
# Input:  [4, 2, 9, 1, 7]
# Output: 9
# ------------------------------------------------------------

# def find_largest(list):
#     largest = list[0]
#     for i in list:
#         if i > largest:
#             largest = i
#         else:
#             continue
#     return largest

# ------------------------------------------------------------
# Question 2: Find the Smallest Element
#
# Write a function that returns the smallest element in the array.
#
# Example:
# Input:  [4, 2, 9, 1, 7]
# Output: 1
# ------------------------------------------------------------

# def find_smallest(list):
#     smallest = list[0]
#     for i in list:
#         if i < smallest:
#             smallest = i
#         else:
#             continue
#     return smallest

# ------------------------------------------------------------
# Question 3: Find the Sum of All Elements
#
# Write a function that returns the sum of all elements.
#
# Example:
# Input:  [1, 2, 3, 4, 5]
# Output: 15
# ------------------------------------------------------------

# def sum(list):
#     sum = 0
#     for i in list:
#         sum += i
#     return sum

# ------------------------------------------------------------
# Question 4: Find the Average of the Array
#
# Write a function that returns the average of all elements.
#
# Example:
# Input:  [10, 20, 30]
# Output: 20
# ------------------------------------------------------------

# def average(list):
#     sum = 0
#     for i in list:
#         sum += i
#     return int(sum/len(list))

# ------------------------------------------------------------
# Question 5: Count Even and Odd Numbers
#
# Count how many even and odd numbers are present.
#
# Example:
# Input:  [1, 2, 3, 4, 5, 6]
# Output:
# Even = 3
# Odd = 3
# ------------------------------------------------------------

# def odd_even(list):
#     odd = 0
#     even = 0
#     for i in list:
#         if i%2==0:
#             odd += 1
#         else:
#             even += 1
#     return f"odd = {odd}, even = {even}"

# ------------------------------------------------------------
# Question 6: Linear Search
#
# Search for the target element and return its index.
# If not found, return -1.
#
# Example:
# Input:
# arr = [10, 20, 30, 40]
# target = 30
#
# Output:
# 2
# ------------------------------------------------------------

# def search(list, target):
#     for i in range(len(list)):
#         if list[i] == target:
#             return i

# ------------------------------------------------------------
# Question 7: Count Occurrences
#
# Count how many times the target element appears.
#
# Example:
# Input:
# arr = [1, 2, 2, 3, 2, 5]
# target = 2
#
# Output:
# 3
# ------------------------------------------------------------

# def count_occur(list, target):
#     count = 0
#     for i in list:
#         if i == target:
#             count += 1
#     return count

# ------------------------------------------------------------
# Question 8: Find the First Occurrence
#
# Return the index of the first occurrence of the target.
# Return -1 if not found.
#
# Example:
# Input:
# arr = [5, 7, 7, 8, 8]
# target = 8
#
# Output:
# 3
# ------------------------------------------------------------

# def find_first_occur(list, target):
#     for i in range(len(list)):
#         if list[i] == target:
#             return i
        
# ------------------------------------------------------------
# Question 9: Find the Last Occurrence
#
# Return the index of the last occurrence of the target.
# Return -1 if not found.
#
# Example:
# Input:
# arr = [5, 7, 7, 8, 8]
# target = 8
#
# Output:
# 4
# ------------------------------------------------------------

# def last_occur(list, target):
#     for i in range(len(list)-1, -1, -1):
#         if list[i] == target:
#             return i

# ------------------------------------------------------------
# Question 10: Check if an Element Exists
#
# Return True if the target exists in the array,
# otherwise return False.
#
# Example:
# Input:
# arr = [3, 5, 7, 9]
# target = 5
#
# Output:
# True
# ------------------------------------------------------------

# def check(list, target):
#     for i in list:
#         if i == target:
#             return True

# ------------------------------------------------------------
# Question 11: Reverse an Array
#
# Reverse the array without using reverse().
#
# Example:
# Input:  [1, 2, 3, 4]
# Output: [4, 3, 2, 1]
# ------------------------------------------------------------

# def reverse(list):
#     reverse = []
#     for i in range(len(list)-1, -1, -1):
#         reverse.append(list[i])
#     return reverse

# ------------------------------------------------------------
# Question 12: Rotate Array Left by One Position
#
# Move every element one position to the left.
#
# Example:
# Input:  [1, 2, 3, 4, 5]
# Output: [2, 3, 4, 5, 1]
# ------------------------------------------------------------

# def left_shift(list):
#     first = list[0]
#     for i in range(len(list)):
#         if i < len(list) - 1:
#             list[i] = list[i+1]
#     list[-1] = first
#     return list

# ------------------------------------------------------------
# Question 13: Rotate Array Right by One Position
#
# Move every element one position to the right.
#
# Example:
# Input:  [1, 2, 3, 4, 5]
# Output: [5, 1, 2, 3, 4]
# ------------------------------------------------------------

# def right_shift(list):
#     last = list[-1]
#     for i in range(len(list)-1,-1,-1):
#         list[i] = list[i-1]
#     list[0] = last
#     return list

# ------------------------------------------------------------
# Question 14: Remove Duplicate Elements
#
# Remove duplicate elements while preserving the original order.
#
# Example:
# Input:  [1, 2, 2, 3, 1, 4]
# Output: [1, 2, 3, 4]
# ------------------------------------------------------------

# def remove_dup(list):
#     result = []
#     for i in list:
#         if i not in result:
#             result.append(i)
#     return result

# ------------------------------------------------------------
# Question 15: Merge Two Arrays
#
# Combine two arrays into one.
#
# Example:
# Input:
# arr1 = [1, 2, 3]
# arr2 = [4, 5, 6]
#
# Output:
# [1, 2, 3, 4, 5, 6]
# ------------------------------------------------------------

# def combine(list1, list2):
#     result = []
#     for i in list1:
#         result.append(i)
#     for i in list2:
#         result.append(i)
#     return result

# ------------------------------------------------------------
# Question 16: Find the Second Largest Element
#
# Return the second largest unique element.
#
# Example:
# Input:  [10, 4, 8, 20, 15]
# Output: 15
# ------------------------------------------------------------

# def find_second_largest(list):
#     largest = list[0]
#     second_large = 0
#     for i in list:
#         if i >= largest:
#             second_large = largest
#             largest = i
#         elif i>second_large and i!=largest:
#             second_large = i

#     return second_large, largest

# ------------------------------------------------------------
# Question 17: Find the Missing Number
#
# The array contains numbers from 1 to n with one number missing.
# Find the missing number.
#
# Example:
# Input:  [1, 2, 4, 5]
# Output: 3
# ------------------------------------------------------------

# def find(list):
#     for i in range(len(list)):
#         if i+1 != list[i]:
#             return i+1

# ------------------------------------------------------------
# Question 18: Move All Zeros to the End
#
# Move every zero to the end while maintaining
# the order of the remaining elements.
#
# Example:
# Input:  [0, 1, 0, 3, 12]
# Output: [1, 3, 12, 0, 0]
# ------------------------------------------------------------

# def move_zero(list):
#     write_index = 0
#     for i in range(len(list)):
#         if list[i] != 0:
#             list[write_index], list[i] = list[i], list[write_index]
#             write_index += 1

#     return list

# ------------------------------------------------------------
# Question 19: Check if the Array is Sorted
#
# Return True if the array is sorted in ascending order,
# otherwise return False.
#
# Example:
# Input:  [1, 2, 3, 5]
# Output: True
#
# Input:  [3, 1, 2]
# Output: False
# ------------------------------------------------------------

# def check_sort(list):
#     pointer = 0
#     for i in range(1,len(list)):
#         if list[i] < list[pointer]:
#             return False
#         pointer += 1
#     return True

# ------------------------------------------------------------
# Question 20: Find the Majority Element
#
# A majority element appears more than n // 2 times.
# Return the majority element.
#
# Example:
# Input:  [2, 2, 1, 2, 3, 2, 2]
# Output: 2
# ------------------------------------------------------------

def find_maj_element(list):
    half_array = len(list)//2
    c = 0
    for i in list:
        for j in list:
            if i == j:
                c += 1
        if c > half_array:
            return i
        c = 1
    return False

l = [2, 2, 1, 3, 3, 4]
print(find_maj_element(l))