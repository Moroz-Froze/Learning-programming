def find_pairs(number):
    pairs = []
    for i in range(1, number // 2 + 1):
        j = number - i
        pair = (i, j)
        if pair not in pairs:
            pairs.append(pair)
    return pairs
print(find_pairs(3))

def password (min_value, max_value):
    for num in range(min_value, max_value + 1):
        pairs = find_pairs(num)
        if pairs:
            pairs_str = "".join([f"{pair[0]}{pair[1]}" for pair in pairs])
            print(f"{num} - {pairs_str}")
password(3, 20)

