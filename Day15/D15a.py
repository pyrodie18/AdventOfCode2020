starting_nums = [0,3,6]

sequence = []

for i in starting_nums:
    sequence.append(i)

for i in range(len(starting_nums), 30000000):
    current_num = sequence[i-1]
    sequence.append('')
    k = 1
    for j in range(len(sequence) - 3, -1, -1):
        if sequence[j] == current_num:
            sequence[-1] = k
            break
        k += 1
    if sequence[-1] == '':
        sequence[-1] = 0

print(sequence[-1])