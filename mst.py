# %%
INF = float('inf')

verticies = [chr(i) for i in range(ord('A'), ord('G') + 1)]
weights = [
    [None,   29, None, None, None,   10, None],
    [  29, None,   16, None, None, None,   15],
    [None,   16, None,   12, None, None, None],
    [None, None,   12, None,   22, None,   18],
    [None, None, None,   22, None,   27,   25],
    [  10, None, None, None,   27, None, None],
    [None,   15, None,   18,   25, None, None]
]

# %%
def get_min_vertex(dist, selected):
    min_vertex_index = -1
    min_dist = INF

    for v_index in range(len(dist)):
        if not selected[v_index] and dist[v_index] < min_dist: 
            min_dist = dist[v_index]
            min_vertex_index = v_index

    return min_vertex_index

def mst_prim(verticies, adjacent):
    dist = [INF for _ in range(len(verticies))]
    selected = [False for _ in range(len(verticies))]
    
    dist[0] = 0

    for _ in range(len(verticies)):
        current_vertex_index = get_min_vertex(dist, selected)
        selected[current_vertex_index] = True

        print(f'{verticies[current_vertex_index]}: {dist}')

        for next_vertex_index in range(len(verticies)):
            if adjacent[current_vertex_index][next_vertex_index] != None and selected[next_vertex_index] == False and adjacent[current_vertex_index][next_vertex_index] < dist[next_vertex_index]:
                dist[next_vertex_index] = adjacent[current_vertex_index][next_vertex_index]

# %%
from functools import reduce

def test(current_vertex_index, verticies, weights, selected):
    if reduce(lambda acc, e: acc and e, selected):
        return

    print(verticies[current_vertex_index])
    selected[current_vertex_index] = True

    min_index = current_vertex_index
    for i in range(len(verticies)):
        if selected[i] == False and weights[current_vertex_index][i] < weights[current_vertex_index][min_index]:
            min_index = i

    test(min_index, verticies, weights, selected)

# %%
mst_prim(verticies, weights)
calculated_weights = weights.copy()
for i in range(len(calculated_weights)):
    for j in range(len(calculated_weights[i])):
        if calculated_weights[i][j] == None:
            calculated_weights[i][j] = INF

test(0, verticies, calculated_weights, [False for _ in range(len(verticies))])
