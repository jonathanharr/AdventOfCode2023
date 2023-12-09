import numpy as np
import operator


def get_from_sequence(sequence, condition, chosen_operator, index):
    differences = np.diff(sequence)
    difference_list = list(differences)

    if condition(difference_list):
        return sequence[index]

    return chosen_operator(sequence[index], get_from_sequence(difference_list, condition,
                                                              chosen_operator, index))


def main():
    file_name = 'input.txt'

    added_previous_sequences = 0
    added_next_sequences = 0
    try:
        with open(file_name, 'r') as file:
            for line in file:
                sequence = [int(x) for x in line.split()]
                prev_in_sequence = get_from_sequence(sequence, lambda lst: all(x == 0 for x in lst), operator.sub, 0)
                added_previous_sequences += prev_in_sequence
                next_in_sequence = get_from_sequence(sequence, lambda lst: all(x == 0 for x in lst), operator.add, -1)
                added_next_sequences += next_in_sequence
    except FileNotFoundError:
        print(f"File not found: {file_name}")
        return

    print(f"Part 1: {added_next_sequences}")
    print(f"Part 2: {added_previous_sequences}")


if __name__ == "__main__":
    main()
