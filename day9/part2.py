import numpy as np


def get_prev_from_sequence(sequence, condition):
    differences = np.diff(sequence)
    difference_list = list(differences)

    if condition(difference_list):
        return sequence[0]

    return sequence[0] - get_prev_from_sequence(difference_list, condition)


def check_all_zeros(lst):
    return all(x == 0 for x in lst)


def main():
    file_name = 'input.txt'

    added_sequences = 0
    try:
        with open(file_name, 'r') as file:
            for line in file:
                integer_list = [int(x) for x in line.split()]
                prev_in_sequence = get_prev_from_sequence(integer_list, check_all_zeros)
                added_sequences += prev_in_sequence
    except FileNotFoundError:
        print(f"File not found: {file_name}")
        return

    print(f"Total of all previous_sequences: {added_sequences}")


if __name__ == "__main__":
    main()
