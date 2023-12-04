import re

AMOUNT_OF_COPIES = {}


def update_deck(line, i):
    pattern = re.compile(r'Card\s+\d+:\s*(\d+(?:\s+\d+)*)\s*\|\s*(\d+(?:\s+\d+)*)')
    match = pattern.match(line)

    list_1 = list(map(int, match.group(1).split()))
    list_2 = list(map(int, match.group(2).split()))

    points_from_row = 0
    for num in list_2:
        if num in list_1:
            points_from_row += 1

    for j in range(i + 1, i + points_from_row + 1):
        if j > len(AMOUNT_OF_COPIES) - 1:
            break
        AMOUNT_OF_COPIES[j] += AMOUNT_OF_COPIES[i]


def main():
    file_name = 'input.txt'

    try:
        with open(file_name, 'r') as file:

            file_contents = file.read()
            lines = file_contents.split('\n')

            for i in range(len(lines)):
                AMOUNT_OF_COPIES[i] = 1

            for i, line in enumerate(lines):
                update_deck(line, i)
    except FileNotFoundError:
        print(f"File not found: {file_name}")
        return

    amount_of_cards = 0
    for val in AMOUNT_OF_COPIES.values():
        amount_of_cards += val

    print(f"total_sum={amount_of_cards}")


if __name__ == "__main__":
    main()
