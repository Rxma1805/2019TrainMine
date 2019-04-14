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

graph = connection
g = nx.Graph(graph)
nx.draw_networkx(g)


# plt.show()

def nagivator(start, destionation, connection_graph):
    pathes = [[start]]
    seen = set()

    while pathes:
        # path = pathes.pop()
        for path in pathes:
            froniter = path[-1]
            print('I am standing at:{}'.format(froniter))
            if froniter in seen:
                continue
            successor = connection_graph[froniter]
            for city in successor:
                print('I am look forward :{}'.format(city))
                if city == destionation:
                    return path + [city]
                else:
                    pathes.append(path + [city])
                    print(pathes)
            #pathes = sorted(pathes,key=len)
            seen.add(froniter)
        return "None"


def draw(route):
    return '->'.join(route)


print(draw(nagivator(MULUMUQI, BANGKOK, connection)))
# print(draw(nagivator(WUHAN,SHENZHEN,connection)))
# print(draw(nagivator(BEIJING,BANGKOK,connection)))