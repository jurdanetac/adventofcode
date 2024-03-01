FILENAME: str = "1.txt"

lines: list = []

# Read problem input
with open(FILENAME, "r") as file:
    lines = [line.rstrip() for line in file]


# Returns the calibration number for each line
def extractNumbers(string) -> int:
    numbers: list = []

    # Extracts all the numbers from the string
    for character in string:
        if character.isdigit():
            numbers.append(character)

    # If there is only one number, it returns the number twice
    if len(numbers) == 1:
        return int(numbers[0] + numbers[0])
    # If there are more than one number, it returns the first and last number as an int
    else:
        return int(numbers[0] + numbers[-1])


# Extracts the numbers from each line
numbers_of_each_line = [extractNumbers(line) for line in lines]

print(sum(numbers_of_each_line))
