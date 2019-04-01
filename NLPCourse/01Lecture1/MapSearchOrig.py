import matplotlib
import networkx as nx
import matplotlib.pyplot as plt

BEIJING, CHANGCHUN, MULUMUQI, WUHAN, GUNAGHZOU, SHENZHEN, BANGKOK, SHANGHAI, NEWYORK = """
BEIJING CHANGCHUN MULUMUQI WUHAN GUANGZHOU SHENZHEN BANGKOK SHANGHAI NEWYORK
""".split()
dictionary = {}
connection = {
    CHANGCHUN: [BEIJING],
    MULUMUQI: [BEIJING],
    BEIJING: [MULUMUQI, CHANGCHUN, WUHAN, SHENZHEN, NEWYORK],
    NEWYORK: [BEIJING, SHANGHAI],
    SHANGHAI: [NEWYORK, WUHAN],
    WUHAN: [SHANGHAI, BEIJING, GUNAGHZOU],
    GUNAGHZOU: [WUHAN, BANGKOK],
    SHENZHEN: [WUHAN, BANGKOK],
    BANGKOK: [SHENZHEN, GUNAGHZOU]
}

# graph = connection
# g = nx.Graph(graph)
# nx.draw_networkx(g)


# plt.show()

def nagivator(start, destionation, connection_graph):
    pathes = [[start]]
    seen = set()

    while pathes:
        path = pathes.pop(0)
        froniter = path[-1]
        if froniter in seen: continue
        successors = connection_graph[froniter]
        for s in successors:
            if s == destionation:
                path.append(s)
                return path
            else:
                pathes.append(path + [s])
                print('before')
                print(pathes)
        pathes = sorted(pathes, key=len)  # 最小换成
        print('after sort')
        print(pathes)
        seen.add(froniter)

def draw(route):
    return '->'.join(route)


#print(draw(nagivator(MULUMUQI, BANGKOK, connection)))
# print(draw(nagivator(WUHAN,SHENZHEN,connection)))
# print(draw(nagivator(BEIJING,BANGKOK,connection)))

def nagivator_Dfs(start, destination, connection_graph):
    pathes = [start]
    seen = set()

    while pathes:
        froniter = pathes.pop()
        if froniter in seen:
            continue
        successors = connection_graph[froniter]
        print('standing on {} Looking forward {}'.format(froniter, successors))
        pathes = pathes + successors
        seen.add(froniter)


connection_2 = {
    0: [1,5],
    1: [0, 2],
    2: [1, 3],
    3: [2, 4],
    4: [3],
    5: [0, 6],
    6: [5, 7],
    7: [6]
}

g = nx.Graph(connection_2)
nx.draw_networkx(g)
plt.show()

def nagivator_bfs(start, destination, connection_graph):
    pathes = [start]
    seen = set()

    while pathes:
        froniter = pathes.pop(0)
        if froniter in seen: continue
        successors = connection_graph[froniter]
        print('standing on {} Looking forward {}'.format(froniter, successors))
        pathes = pathes + successors
        seen.add(froniter)


def nagivator_dfs(start, destination, connection_graph):
    pathes = [start]
    seen = set()

    while pathes:
        froniter = pathes.pop(0)

        if froniter in seen: continue

        successors = connection_graph[froniter]
        print('standing on {} Looking forward {}'.format(froniter, successors))
        pathes = successors + pathes

        seen.add(froniter)

nagivator_bfs(0, 7, connection_2)
print("____-----_____-----")
nagivator_dfs(0, 7, connection_2)