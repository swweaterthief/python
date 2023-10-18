def letter_statistics(input_file, output_file):
    letter_counts = {}

    with open(input_file, 'r') as f:
        for line in f:
            for char in line:
                if char.isalpha():
                    if char not in letter_counts():
                        letter_counts[char] = 0
                    letter_counts[char] += 1

    sorted_statistics = sorted(letter_counts.items(), key=lambda x: x[1])

    with open(output_file, 'w') as f:
        for letter, count in sorted_statistics:
            f.write(f'{letter}: {count}\n')