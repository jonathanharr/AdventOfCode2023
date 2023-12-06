from functools import reduce


def main():
    file_name = 'input.txt'

    try:
        with open(file_name, 'r') as file:
            file_contents = file.read()
            lines = file_contents.split('\n')

            time = [int(num) for num in lines[0].split()[1:]]
            distance = [int(num) for num in lines[1].split()[1:]]

            multipliers = []
            for i in range(len(distance)):
                multiplier = 0
                for button_hold in range(time[i] + 1):
                    time_left = time[i] - button_hold
                    traveled = time_left * button_hold
                    if traveled >= distance[i]:
                        multiplier += 1
                multipliers.append(multiplier)

            result = reduce(lambda x, y: x * y, multipliers)
            print(f"result={result}")
    except FileNotFoundError:
        print(f"File not found: {file_name}")
        return


if __name__ == "__main__":
    main()
