"""
เขียบนโปรแกรมหา index ของตัวเลขที่มีค่ามากที่สุดใน list

[Input]
numbers: list of numbers

[Output]
index: index of maximum number in list

[Example 1]
input = [1,2,1,3,5,6,4]
output = 4

[Example 2]
input = []
output = list can not blank
"""


class Solution:

    def find_max_index(self, numbers):
        print(f"input = {numbers}")
        if not numbers:
            return "list can not blank"
        
        max_value = max(numbers)
        return numbers.index(max_value)

numbers = [1,2,1,3,5,6,4]
max_index = Solution().find_max_index(numbers)
print(f"output = {max_index}")