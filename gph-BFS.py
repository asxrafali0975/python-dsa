
from collections import deque
def adjlistf(edges,v):

    adjlist = [[] for _ in range(v+1)]
    for x in edges:

        adjlist[x[0]].append(x[1])
        adjlist[x[1]].append(x[0])
    return adjlist


def bfs(adjlist ,target):
    dq = deque()
    hash = set()

    dq.append(target)
    hash.add(target)

    answer = []
    answer.append(target)


    while len(dq):
        front = dq.popleft()
        for x in adjlist[front]:
            if x not in hash:
                hash.add(x)
                answer.append(x)

    return answer






if __name__=="__main__":
    edges = [[1,2] , [1,3] , [2,4], [3,5] , [3,4],[4,5]]
    v=5
    adjlist = adjlistf(edges,v)
    

    answer = bfs(adjlist , 1)
    print(answer)

