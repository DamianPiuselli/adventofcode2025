# --- Day 3: Lobby ---


def largest_two_digit_subsequence(string):
    # Given "ABCDEFGH", find ints X and Y such that XY is the largest two-digit number in the string.

    # strategy. Find the largest first digit, then find the largest second digit in the substring at the right.

    digits = [9, 8, 7, 6, 5, 4, 3, 2, 1]

    for digit in digits:
        if str(digit) in string:
            first_index = string.index(str(digit))
            substring = string[first_index + 1 :]
            for digit2 in digits:
                if str(digit2) in substring:
                    return int(str(digit) + str(digit2))


def largest_twelve_digit_subsequence(string):
    # Given "ABCDEFGH", find ints J to Z such that JY..XZ is the largest twelve-digit number in the string.
    # strategy. Build it backward! start with the last twelve digits
    # Then move the first digit to the leftmost highest value, then the second digit to the second highest value, etc.

    k = 12
    if len(string) <= k:
        return int(string)

    start = 0
    digits = []
    for remaining in range(k, 0, -1):
        end = len(string) - remaining
        segment = string[start : end + 1]
        max_digit = max(segment)
        idx = segment.index(max_digit) + start
        digits.append(max_digit)
        start = idx + 1

    return int("".join(digits))


cumsum_two_digits = 0
cumsum_twelve_digits = 0

with open("day3.txt") as f:
    banks = f.read().splitlines()
    for bank in banks:
        result_two_digits = largest_two_digit_subsequence(bank)
        cumsum_two_digits += result_two_digits

        result_twelve_digits = largest_twelve_digit_subsequence(bank)
        cumsum_twelve_digits += result_twelve_digits
        print(f"largest twelve digits {bank} is {result_twelve_digits}")


print(f"Cumulative sum of largest two-digit subsequences is {cumsum_two_digits}")
print(f"Cumulative sum of largest twelve-digit subsequences is {cumsum_twelve_digits}")
