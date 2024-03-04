# Измените алгоритм Дейкстры таким образом, чтобы он просто возвращал
# путь от начальной вершины к другой вершине, которую вы передаете.
import heapq


def dijkstra(graph, starting_vertex, ending_vertex):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[starting_vertex] = 0
    previous_vertices = {vertex: None for vertex in graph}
    pq = [(0, starting_vertex)]

    while len(pq) > 0:
        current_distance, current_vertex = heapq.heappop(pq)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_vertices[neighbor] = current_vertex
                heapq.heappush(pq, (distance, neighbor))

    # Восстановление пути
    path = []
    current_vertex = ending_vertex
    while previous_vertices[current_vertex] is not None:
        path.insert(0, current_vertex)
        current_vertex = previous_vertices[current_vertex]

    if distances[ending_vertex] != float('infinity'):
        path.insert(0, starting_vertex)
    else:
        return f"Нет пути из {starting_vertex} в {ending_vertex}"
    return path