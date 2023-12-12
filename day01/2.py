# --- Day 1: Trebuchet?! ---
# --- Part Two ---

# s[1:] - updates the variable s by slicing the first character
# s = "example"
# s = s[1:]  # After this line, s becomes "xample"


# Function to extract digits from a string and return them as a list
def get_digits(line):
    """ Extract digits from a string and return them as a list. """
    return [char for char in line.strip() if char.isdigit()]

# Function to calculate calibration from the first and last digits of a list
def calculate_calibration(digits):
    """ Calculate calibration from the first and last digits. """
    return int(digits[0] + digits[-1])

# Dictionary to map words to their numeric equivalents
digit_words = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
               'six': '6', 'seven': '7', 'eight': '8', 'nine': '9', 'zero': '0'}

def main():
    sum_1 = 0
    sum_2 = 0

    with open('input.txt', 'r') as f:
        for line in f.readlines():
            # Part 1: Extract digits from the line and calculate calibration
            digits = get_digits(line)
            calibration = calculate_calibration(digits)
            sum_1 += calibration

            # Part 2: Convert words to digits and calculate calibration
            digits = []
            s = line.strip()
            while s:
                # If the first character is a digit, append it to digits
                if s[0].isdigit():
                    digits.append(s[0])
                    s = s[1:]
                    continue

                # Check the dictionary for a match and append the corresponding digit
                for word in digit_words:
                    if s.startswith(word):
                        digits.append(digit_words[word])
                        s = s[1:]
                        break
                else:
                    # If no match is found, iterate
                    s = s[1:]

            calibration = calculate_calibration(digits)
            sum_2 += calibration

    print(sum_1)
    print(sum_2)

if __name__ == "__main__":
    main()
