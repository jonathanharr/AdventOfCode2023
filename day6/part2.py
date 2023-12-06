def main():
    file_name = 'input.txt'

    try:
        with open(file_name, 'r') as file:
            file_contents = file.read()
            lines = file_contents.split('\n')

            time_values = [int(num) for num in lines[0].split()[1:]]
            distance_values = [int(num) for num in lines[1].split()[1:]]
            time = int("".join(map(str, time_values)))
            distance = int("".join(map(str, distance_values)))

            ways_to_win = 0
            for button_hold in range(time + 1):
                time_left = time - button_hold
                traveled = time_left * button_hold
                if traveled >= distance:
                    ways_to_win += 1

            print(f"result={ways_to_win}")
    except FileNotFoundError:
        print(f"File not found: {file_name}")
        return


if __name__ == "__main__":
    main()
