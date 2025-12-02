import re


def repeating_number(int):  # part1
    # if odd number of digits, return false
    if len(str(int)) % 2 != 0:
        return False

    s = str(int)
    s1, s2 = s[: len(s) // 2], s[len(s) // 2 :]
    return s1 == s2


def repeating_number_part2(int):  # part2
    s = str(int)
    length = len(s)

    for times in range(2, length + 1):
        if length % times == 0:  # if "times" is a multiple of the length
            segment = s[: length // times]
            if segment * times == s:
                return True

    return False


cumsum = 0

with open("day2.txt") as f:
    data = f.read().split(",")

    for string in data:
        # parse numbers
        nums = re.findall(r"(?<!\d)-?\d+", string)
        if len(nums) >= 2:
            start, end = map(int, nums[:2])
            print(start, end)
        else:
            raise ValueError(f"expected two integers in: {string!r}")

        for number in range(start, end + 1):
            if repeating_number_part2(number):
                print(f"Found repeating number: {number}")
                cumsum += number

print(f"Total sum of repeating numbers: {cumsum}")
