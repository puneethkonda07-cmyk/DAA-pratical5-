
def hamiltonian_cycle(graph):
    n = len(graph)
    path = [0] + [-1] * (n - 1)

    def solve(pos):
        if pos == n:
            return graph[path[-1]][path[0]] == 1

        for v in range(1, n):
            if v not in path[:pos] and graph[path[pos - 1]][v] == 1:
                path[pos] = v

                if solve(pos + 1):
                    return True

                path[pos] = -1

        return False

    if solve(1):
        print("Hamiltonian Circuit:", path + [path[0]])
    else:
        print("No Hamiltonian Circuit exists")


graph = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 1, 1],
    [0, 1, 0, 0, 1],
    [1, 1, 0, 0, 1],
    [0, 1, 1, 1, 0]
]

hamiltonian_cycle(graph)
print(92460118292)
