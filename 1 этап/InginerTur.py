from collections import defaultdict

def chi_squared(observed, expected):
    return sum((o - e) ** 2 / e for o, e in zip(observed, expected))

N = int(input())

lines = [input().strip() for _ in range(N)]

frequencies = []
all_chars = set()
for line in lines:
    freq = defaultdict(int)
    for char in line:
        freq[char] += 1
        all_chars.add(char)
    frequencies.append(freq)

expected_frequencies = defaultdict(int)
for char in all_chars:
    expected_frequencies[char] = sum(freq[char] for freq in frequencies) / N

chi_values = []
for freq in frequencies:
    observed = [freq[char] for char in all_chars]
    expected = [expected_frequencies[char] for char in all_chars]
    chi_values.append(chi_squared(observed, expected))

marsian_index = chi_values.index(max(chi_values)) + 1

print(marsian_index)
