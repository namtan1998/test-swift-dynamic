"""
เขียบนโปรแกรมแปลงตัวเลยเป็นตัวเลข roman

[Input]
number: list of numbers

[Output]
roman_text: roman number

[Example 1]
input = 101
output = CI

[Example 2]
input = -1
output = number can not less than 0
"""


# class Solution:

#     def number_to_roman(self, number: int) -> str:
#         pass

class Solution:
  
  def __init__(self):
    self.roman_map = {
      1000: "M",
      900: "CM",
      500: "D",
      400: "CD",
      100: "C",
      90: "XC",
      50: "L",
      40: "XL",
      10: "X",
      9: "IX",
      5: "V",
      4: "IV",
      1: "I",
    }

  def number_to_roman(self, number: int) -> str:

    if number < 0:
      return "number can not less than 0"
    
    if number == 0:
      return "NULLA"

    roman_numeral = ""
    for value, roman in self.roman_map.items():
      while number >= value:
        number -= value
        roman_numeral += roman

    return roman_numeral

if __name__ == "__main__":
    solution = Solution()

    while True:
        number = int(input("input = "))
        roman_number = solution.number_to_roman(number)
        print(f"output = {roman_number}")