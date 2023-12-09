import math
from day8.node import Node


def main():
    file_name = 'input.txt'
    nodes = {}
    instructions = []
    starting_nodes = []
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
                if destination[2:3] == 'A':
                    node_obj = Node(destination, left, right, left)
                    starting_nodes.append(node_obj)

                nodes[destination] = (left, right)


    except FileNotFoundError:
        print(f"File not found: {file_name}")
        return

    current_nodes = starting_nodes

    found_z_nodes = []
    steps_taken_list = []
    for destination in current_nodes:
        current_node = destination.node
        steps = 0
        instruction_index = 0

        while current_node[2] != 'Z' and current_node not in found_z_nodes:
            destination = nodes[current_node]
            left_right_index = instructions[instruction_index]
            current_node = destination[left_right_index]
            if instruction_index == len(instructions) - 1:
                instruction_index = 0
            else:
                instruction_index += 1

            steps += 1
        found_z_nodes.append(current_node)
        steps_taken_list.append(steps)

    lcm_result = math.lcm(*steps_taken_list)
    print(f"Using the least common multiple of all steps taken: {lcm_result}")


if __name__ == "__main__":
    main()
