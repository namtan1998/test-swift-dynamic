"""
เขียบนโปรแกรมแปลงตัวเลยเป็นคำอ่านภาษาไทย

[Input]
number: positive number rang from 0 to 10_000_000

[Output]
num_text: string of thai number call

[Example 1]
input = 101
output = หนึ่งร้อยเอ็ด

[Example 2]
input = -1
output = number can not less than 0
"""

class Solution:

    def __init__(self):
        self.thai_number = ("ศูนย์", "หนึ่ง", "สอง", "สาม", "สี่", "ห้า", "หก", "เจ็ด", "แปด", "เก้า")
        self.unit = ("", "สิบ", "ร้อย", "พัน", "หมื่น", "แสน", "ล้าน")

    def unit_process(self, number: int):
        length = len(number) > 1
        result = ''

        for index, current in enumerate(map(int, number)):
            if current:
                if index:
                    result = self.unit[index] + result

                if length and current == 1 and index == 0:
                    result += 'เอ็ด'
                elif index == 1 and current == 2:
                    result = 'ยี่' + result
                elif index != 1 or current != 1:
                    result = self.thai_number[current] + result

        return result

    def number_to_thai(self, number):
        if number < 0:
            return "number can not less than 0"
        
        if number == 0:
            return "ศูนย์"

        s_number = str(number)[::-1]
        n_list = [s_number[i:i + 6].rstrip("0") for i in range(0, len(s_number), 6)]
        result = self.unit_process(n_list.pop(0))

        for i in n_list:
            result = self.unit_process(i) + 'ล้าน' + result

        return result

if __name__ == "__main__":
    solution = Solution()

    while True:
        number = int(input("input = "))
        thai_text = solution.number_to_thai(number)
        print(f"output = {thai_text}")
        