def dijkstra(g):
    from collections import defaultdict
    visit = []
    shortestPath = defaultdict(int)
    for n in g:
        shortestPath[n] = float("inf")
    
    # starting point
    shortestPath["a"] = 0

    for n in g:
        origin = shortestPath[n]
        for node in g[n]:
            to, cost = node, g[n][node]
            if origin + cost < shortestPath[to]:
                shortestPath[to] = origin + cost

    print(shortestPath)





graph = {"a" :{"b" : 10, "c":3}, "b" :{"c":1, "d":2}, "c":{"b":4, "d":8,"e":2}, "d": {"e": 7}, "e":{"d":9}}
dijkstra(graph)