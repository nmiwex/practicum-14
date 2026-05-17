n = int(input())
m = int(input())
graph = {}

for _ in range(m):
    city1, city2, dist = input().split()
    dist = int(dist)

    if city1 not in graph:
        graph[city1] = []
    if city2 not in graph:
        graph[city2] = []

    graph[city1].append((city2, dist))
    graph[city2].append((city1, dist))

start, end = input().split()


def shortest(current, finish, visited):
    """
    looking for the shortest path
    """
    if current == finish:
        return 0

    visited.add(current)
    min_dist = float('inf')

    for next_city, distance in graph[current]:
        if next_city not in visited:
            result = shortest(next_city, finish, visited.copy())

            if result != float('inf'):
                total = distance + result
                if total < min_dist:
                    min_dist = total

    return min_dist


print(shortest(start, end, set()))