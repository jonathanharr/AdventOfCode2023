import numpy as np



def get_next_from_sequence(sequence, condition):
    differences = np.diff(sequence)
    difference_list = list(differences)

    if condition(difference_list):
        return sequence[-1]

    return sequence[-1] + get_next_from_sequence(difference_list, condition)


def check_all_zeros(lst):
    return all(x == 0 for x in lst)


def main():
    file_name = 'input.txt'

    added_sequences = 0
    try:
        with open(file_name, 'r') as file:
            for line in file:
                integer_list = [int(x) for x in line.split()]
                next_in_sequence = get_next_from_sequence(integer_list, check_all_zeros)
                added_sequences += next_in_sequence
    except FileNotFoundError:
        print(f"File not found: {file_name}")
        return

    print(f"Total of all next_sequences: {added_sequences}")


if __name__ == "__main__":
    main()
