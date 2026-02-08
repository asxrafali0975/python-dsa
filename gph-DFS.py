def adjlistf(edges, v):

    adjlist = [[] for _ in range(v + 1)]
    for x in edges:
        a, b = x
        adjlist[a].append(b)
        adjlist[b].append(a)
    return adjlist


def dfs(adjlist, target, hash, answer):

    hash.add(target)
    answer.append(target)

    for x in adjlist[target]:
        if x not in hash:
            dfs(adjlist, x, hash, answer)


if __name__ == "__main__":
    edges = [[1, 2], [1, 3], [2, 4], [3, 5], [3, 4], [4, 5]]
    v = 5
    adjlist = adjlistf(edges, v)

    hash = set()
    answer = []

    dfs(adjlist, 1, hash, answer)
    print(answer)
