# --- Day 1: Trebuchet?! ---
# --- Part One ---

def get_digits(line):
    """ Extract digits from a string and return them as a list. """
    return [char for char in line.strip() if char.isdigit()]

def calculate_calibration(digits):
    """ Calculate calibration from the first and last digits. """
    return int(digits[0] + digits[-1])

def main():
    sum = 0

    with open('input.txt', 'r') as f:
        for line in f.readlines():
            digits = get_digits(line)
            calibration = calculate_calibration(digits)
            sum += calibration

    print(sum)

if __name__ == "__main__":
    main()
