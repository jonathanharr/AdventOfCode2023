
def main():
    file_name = 'input.txt'
    # file_name = 'sample.txt'
    nodes = {}
    instructions = []
    try:
        with open(file_name, 'r') as file:
            file_contents = file.read()
            lines = file_contents.split('\n')
            ins_line = lines[0]
            for i in range(len(ins_line)):
                if ins_line[i] == 'L':
                    instructions.append(0)
                else:
                    instructions.append(1)
            for i, line in enumerate(lines):
                if i < 2:
                    continue
                destination = line[0:3]
                left = line[7:10]
                right = line[12:15]
                nodes[destination] = (left, right)

    except FileNotFoundError:
        print(f"File not found: {file_name}")
        return

    current_node_key = 'AAA'
    steps = 0
    instruction_index = 0

    while current_node_key != 'ZZZ':
        node = nodes[current_node_key]


        left_right_index = instructions[instruction_index]
        current_node_key = node[left_right_index]
        if instruction_index == len(instructions) - 1:
            instruction_index = 0
        else:
            instruction_index += 1
        steps += 1

    print(steps)


if __name__ == "__main__":
    main()
