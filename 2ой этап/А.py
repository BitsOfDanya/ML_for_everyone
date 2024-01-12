import bisect

def calculate_vitality(positions, vitality, queries):
    reptiles = sorted(zip(positions, vitality))
    results = []

    for xq, kq in queries:
        index = bisect.bisect_left(reptiles, (xq,))

        neighbors = []
        left, right = index - 1, index
        while len(neighbors) < kq and (left >= 0 or right < len(reptiles)):
            left_dist = abs(reptiles[left][0] - xq) if left >= 0 else float('inf')
            right_dist = abs(reptiles[right][0] - xq) if right < len(reptiles) else float('inf')

            if left_dist < right_dist:
                neighbors.append(reptiles[left])
                left -= 1
            elif right_dist < left_dist:
                neighbors.append(reptiles[right])
                right += 1
            else:
                if len(neighbors) + (right - left - 1) < kq:
                    results.append(0)
                    break
                else:
                    while len(neighbors) < kq:
                        neighbors.append(reptiles[left])
                        left -= 1

        if len(neighbors) == kq:
            results.append(sum(v[1] for v in neighbors))

    return results


import bisect

def process_input():
    n = int(input().strip())

    positions = []
    vitality = []
    for _ in range(n):
        x, p = map(int, input().strip().split())
        positions.append(x)
        vitality.append(p)

    m = int(input().strip())

    queries = []
    for _ in range(m):
        xq, kq = map(int, input().strip().split())
        queries.append((xq, kq))

    return positions, vitality, queries

def main():
    positions, vitality, queries = process_input()
    results = calculate_vitality(positions, vitality, queries)

    for result in results:
        print(result)

if __name__ == "__main__":
    main()
