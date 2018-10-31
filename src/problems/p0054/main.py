import itertools, operator, re

def does_p1_win(p1hand, p2hand):
    p1grade, p1groups = grade_hand(p1hand)
    p2grade, p2groups = grade_hand(p2hand)

    if p1grade > p2grade:
        return True
    elif p1grade == p2grade:
        for p1rank, p2rank in reversed(list(zip(p1groups, p2groups))):
            if p1rank > p2rank:
                return True
            elif p1rank < p2rank:
                break
    return False

def sort_hand(hand):
    # Works using built-in sort, with tweak to input/output
    hand = re.sub(r'([AKQJT])(.)',
                  lambda m: 'F'+str('TJQKA'.index(m.group(1)))+m.group(2),
                  hand)
    hand = ' '.join(sorted(hand.split(' ')))
    hand = re.sub(r'F(\d)(.)',
                  lambda m: 'TJQKA'[int(m.group(1))]+m.group(2),
                  hand)
    return hand

def grade_hand(hand):
    """
    Returns the following grades for each kind of hand:
    10 Royal Flush
    09 Straight Flush
    08 Four of a Kind
    07 Full House
    06 Flush
    05 Straight
    04 Three of a Kind
    03 Two Pair
    02 One Pair
    01 High Card

    ... in addition to the flattened list of card groups
    (see comment for groups below for example)
    """
    # ##############################################
    # Some variables used for the logic
    # ###########

    # Card hierarchy
    order = '23456789TJQKA'

    # Sorted list of cards in hand
    # e.g. ['2H', '4C', '4H', 'TH', 'AD']
    handlist = hand.split(' ')

    # List of only card ranks in hand
    # e.g. [0, 2, 2, 8, 12] for the hand above
    ranks = [order.index(c[0]) for c in handlist]

    # ##############################################
    # All logic
    # ###########

    #         Singletons Pairs Triples Quads
    groups = [[],        [],   [],     []]
    # e.g. [[0, 8, 12], [2], [], []] for the hand earlier
    # Note that this list is [0, 8, 12, 2] when flattened (used for tiebreaking)
    for rank, count in [(rank, ranks.count(rank)) for rank in set(ranks)]:
        groups[count-1].append(rank)
    # Sort groups afterwards
    map(lambda group: group.sort(), groups)

    # Whether or not the hand is a FLUSH
    flush = len(set([c[1] for c in handlist])) == 1

    # Whether or not the hand is a STRAIGHT
    _diffs = set(map(lambda t: operator.sub(*t), zip(ranks[:-1], ranks[1:])))
    straight = len(_diffs) == 1 and -1 in _diffs

    # Whether or not the hand has FOUR OF A KIND
    fourofakind = len(groups[3]) > 0

    # Whether or not the hand has THREE OF A KIND
    threeofakind = len(groups[2]) > 0

    # Whether or not the hand has TWO PAIRS
    twopair = len(groups[1]) > 1

    # Whether or not the hand has a PAIR
    pair = len(groups[1]) > 0

    # ##############################################
    # Assign the grades
    # ###########

    # Default grade is for a High Card
    grade = 1

    if flush and straight:
        if ranks[-1] == 12:
            # Royal Flush
            grade = 10
        else:
            # Straight Flush
            grade = 9
    elif fourofakind:
        # Four of a Kind
        grade = 8
    elif threeofakind and pair:
        # Full House
        grade = 7
    elif flush:
        # Flush
        grade = 6
    elif straight:
        # Straight
        grade = 5
    elif threeofakind:
        # Three of a Kind
        grade = 4
    elif twopair:
        # Two Pairs
        grade = 3
    elif pair:
        # One Pair
        grade = 2

    # Return grade and flattened list of groups
    return grade, itertools.chain(*groups)

def main():
    with open('poker.txt', 'r') as fh:
        hands = [hand.strip() for hand in fh.readlines() if len(hand.strip()) > 0]  # omit empty lines
    ret = 0
    for hand in hands:
        p1hand = sort_hand(hand[:14])
        p2hand = sort_hand(hand[15:])
        if does_p1_win(p1hand, p2hand):
            ret += 1
    return ret
