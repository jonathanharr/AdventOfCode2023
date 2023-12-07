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


def compare_types(cards_type, other_cards_type):
    if cards_type == other_cards_type:
        return cards_type
    if cards_type < other_cards_type:
        return cards_type

    return other_cards_type


def count_char_duplicates_with_joker(chars):
    cards_exc_joker = []
    cards_checked_already = []
    amount_of_jokers = chars.count('J')

    if amount_of_jokers == 5:
        return 0

    for i in range(len(chars)):
        if chars[i] in cards_checked_already:
            continue

        if chars[i] == 'J':
            continue

        cards_checked_already.append(chars[i])
        cards_exc_joker.append(chars[i])

    cards_checked_already = []

    best_hand_so_far = 6
    for i in range(len(cards_exc_joker)):
        if cards_exc_joker[i] in cards_checked_already:
            continue
        card = cards_exc_joker[i]

        modified_by_joker = ['J' if char == card else char for char in chars]
        points = count_char_duplicates(modified_by_joker)
        hand_type = get_hand_type(points)
        best_hand_so_far = compare_types(best_hand_so_far, hand_type)

    return best_hand_so_far


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
    a_card_hand = current_hand.cards
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

                hand_type = count_char_duplicates_with_joker(list(cards))
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
