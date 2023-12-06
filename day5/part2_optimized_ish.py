import queue


INPUT = []


def get_map_range_instructions(line_to_look_for):
    map_range_instructions = []
    index = INPUT.index(line_to_look_for)
    for i in range(index + 1, len(INPUT)):
        if INPUT[i] == '':
            break
        line = INPUT[i]
        numbers_list = [int(num) for part in line.split(' ') for num in part.split()]
        map_range_instructions.append(numbers_list)

    return map_range_instructions


def map_range(source_range, target_range, overlapping):
    overlapping_start = overlapping[0]
    overlapping_end = overlapping[1]

    source_range_start = source_range[0]

    index_in_source_range = overlapping_start - source_range_start
    target_range_start = target_range[0]

    new_range_start = target_range_start + index_in_source_range
    new_range_end = new_range_start + (overlapping_end - overlapping_start)
    return new_range_start, new_range_end


def get_overlapping_and_non_overlapping(range1, range2):
    start1, end1 = range1
    start2, end2 = range2

    overlap_start = max(start1, start2)
    overlap_end = min(end1, end2)
    overlapping_part = (overlap_start, overlap_end) if overlap_start <= overlap_end else None

    non_overlap1 = (start1, overlap_start) if start1 < overlap_start else None
    non_overlap2_start = overlap_end
    non_overlap2_end = end2
    non_overlap2 = (non_overlap2_start, non_overlap2_end) if non_overlap2_start < non_overlap2_end else None

    check_ranges_next = []
    if overlapping_part is not None:
        if non_overlap1 is not None:
            if non_overlap1[0] >= range2[0] and non_overlap1[1] <= range2[1]:
                check_ranges_next.append(non_overlap1)

        if non_overlap2 is not None:
            if non_overlap2[0] >= range2[0] and non_overlap2[1] <= range2[1]:
                check_ranges_next.append(non_overlap2)
    else:
        check_ranges_next.append(range2)

    return overlapping_part, check_ranges_next


def get_new_range(destination_source_range_as_list, range_pair):
    seed_queue = queue.Queue()
    seed_queue.put(range_pair)
    ranges = []

    while not seed_queue.empty():
        current_seed_range = seed_queue.get()

        seed_start = current_seed_range[0]
        seed_end = current_seed_range[1]

        found_matching_range = False
        for i in range(len(destination_source_range_as_list)):
            source_start = destination_source_range_as_list[i][1]
            source_end = source_start + destination_source_range_as_list[i][2]

            map_to_range_source = (source_start, source_end)
            overlapping, range_to_check = get_overlapping_and_non_overlapping(map_to_range_source,
                                                                                         current_seed_range)
            for j in range(len(range_to_check)):
                check_new_range = list(range_to_check[j])
                if check_new_range[0] != seed_start or check_new_range[1] != seed_end:

                    if check_new_range[0] == overlapping[1]:
                        check_new_range[0] += 1

                    if check_new_range[1] == overlapping[0]:
                        check_new_range[1] -= 1

                    seed_queue.put(tuple(check_new_range))

            if overlapping is None or len(overlapping) == 0:
                continue

            found_matching_range = True
            target_range = destination_source_range_as_list[i][0], destination_source_range_as_list[i][0] \
                                                                   + destination_source_range_as_list[i][2]
            mapped_range = map_range(map_to_range_source, target_range, overlapping)
            ranges.append(mapped_range)

        if not found_matching_range:
            ranges.append(current_seed_range)
    return ranges


def main():
    global INPUT
    file_name = 'input.txt'

    try:
        with open(file_name, 'r') as file:
            file_contents = file.read()
            lines = file_contents.split('\n')
            INPUT = lines

            seed_to_soil = get_map_range_instructions("seed-to-soil map:")
            soil_to_fertilizer = get_map_range_instructions("soil-to-fertilizer map:")
            fertilizer_to_water = get_map_range_instructions("fertilizer-to-water map:")
            water_to_light = get_map_range_instructions("water-to-light map:")
            light_to_temperature = get_map_range_instructions("light-to-temperature map:")
            temperature_to_humidity = get_map_range_instructions("temperature-to-humidity map:")
            humidity_to_location = get_map_range_instructions("humidity-to-location map:")

            instructions = [soil_to_fertilizer, fertilizer_to_water, water_to_light,
                            light_to_temperature, temperature_to_humidity, humidity_to_location]
    except FileNotFoundError:
        print(f"File not found: {file_name}")
        return

    numbers = [int(num) for num in INPUT[0].split()[1:]]
    pairs = list(zip(numbers[::2], numbers[1::2]))

    new_ranges = []
    for i in range(len(pairs)):
        seed_start_end = pairs[i][0], pairs[i][0] + pairs[i][1]
        new_range = get_new_range(seed_to_soil, seed_start_end)
        new_ranges.extend(new_range)

    for instruction in instructions:
        tempmap = []
        for i in range(len(new_ranges)):
            seed_start_end = new_ranges[i][0], new_ranges[i][1]
            new_range = get_new_range(instruction, seed_start_end)
            tempmap.extend(new_range)
        new_ranges = tempmap

    all_values = [value for tup in new_ranges for value in tup]
    lowest_value = min(all_values)
    print("Lowest value:", lowest_value)


if __name__ == "__main__":
    main()