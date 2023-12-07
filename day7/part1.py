from day7.hand import Hand


def count_char_duplicates(chars):
    counter_list = []
    cards_checked_already = []
    for i in range(len(chars)):
        if chars[i] in cards_checked_already:
            continue
        cards_checked_already.append(chars[i])

        counter = chars.count(chars[i])
        if counter > 1:
            counter_list.append(counter)

    return counter_list


def get_hand_type(label_counts):
    if 5 in label_counts:
        return 0
    elif 4 in label_counts:
        return 1
    elif 3 in label_counts and 2 in label_counts:
        return 2
    elif 3 in label_counts:
        return 3
    elif label_counts.count(2) == 2:
        return 4
    elif 2 in label_counts:
        return 5
    else:
        return 6


def get_final_score_of_hand(hands, index):
    card_rank = 1
    current_hand = hands[index]
    for i in range(len(hands)):
        if i == index:
            continue
        compare_hand = hands[i]
        comparison = current_hand.compare_types(compare_hand)
        if comparison == 1:
            card_rank += 1
            continue
        elif comparison == 2:
            continue

        label_comparison = current_hand.compare_labels(compare_hand)

        if label_comparison == 1:
            card_rank += 1
            continue

    return current_hand.get_bid * card_rank


def main():
    file_name = 'input.txt'

    hands = []
    try:
        with open(file_name, 'r') as file:
            for line in file:
                cards = line[0:5]
                bid_amount = line[6:len(line)]

                if '\n' in bid_amount:
                    bid_amount = bid_amount[0:len(bid_amount) - 1]

                points = count_char_duplicates(list(cards))
                hand_type = get_hand_type(points)
                current_hand = Hand(cards, hand_type, bid_amount)

                hands.append(current_hand)
    except FileNotFoundError:
        print(f"File not found: {file_name}")
        return

    score = 0
    for index in range(len(hands)):
        score += get_final_score_of_hand(hands, index)

    print(score)


if __name__ == "__main__":
    main()
