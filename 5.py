n = int(input())
tree = {}

for _ in range(n):
    parent, child = input().split()
    if parent not in tree:
        tree[parent] = []
    tree[parent].append(child)

name = input()


def descendants(person):
    if person not in tree:
        return 0
    count = 0
    for child in tree[person]:
        count += 1 + descendants(child)

    return count


print(descendants(name))