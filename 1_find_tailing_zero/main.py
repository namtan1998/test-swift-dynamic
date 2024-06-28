"""
เขียบนโปรแกรมหาจำนวนเลข 0 ที่ออยู่ติดกันหลังสุดของค่า factorial โดยห้ามใช้ function from math

[Input]
number: as an integer

[Output]
count: count of tailing zero as an integer

[Example 1]
input = 7
output = 1

[Example 2]
input = -10
output = number can not be negative
"""


class Solution:     
    def find_trailing_zeros(self, number: int) -> int:
        
        if number < 0:
            return "number can not be negative"

        count_zeros = 0
        while number >= 5:
            number //= 5
            count_zeros += number

        return count_zeros

if __name__ == "__main__":
    solution = Solution()

    while True:
        number = int(input("input = "))
        count_zeros = solution.find_trailing_zeros(number)
        print(f"output = {count_zeros}")
        
        while True:
            user_choice = input("Continue (y/n)? ").lower()
            if user_choice in ("y", "yes"):
                break
            elif user_choice in ("n", "no"):
                exit()
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

        