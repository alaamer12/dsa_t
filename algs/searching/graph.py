from collections import deque
import sys


class Graph:
    @staticmethod
    def bfs(start_node, adj_list, num_nodes):
        visited = [False] * num_nodes
        queue = deque([start_node])

        visited[start_node] = True

        while queue:
            node = queue.popleft()
            print(node, end=" ")

            # Iterate over the adjacency list for the current node
            for i in range(num_nodes):
                if adj_list[node][i] == 1 and not visited[i]:
                    visited[i] = True
                    queue.append(i)

    @staticmethod
    def dfs(start_node, adj_list, num_nodes):
        visited = [False] * num_nodes
        stack = [start_node]

        while stack:
            node = stack.pop()
            if not visited[node]:
                print(node, end=" ")
                visited[node] = True

                # Get all adjacent vertices of the popped vertex
                for i in range(num_nodes - 1, -1, -1):
                    if adj_list[node][i] == 1 and not visited[i]:
                        stack.append(i)

    @staticmethod
    def dijkstra(start_node, adj_matrix, num_nodes):
        INF = sys.maxsize
        dist = [INF] * num_nodes
        visited = [False] * num_nodes

        dist[start_node] = 0

        for _ in range(num_nodes - 1):
            u = Graph.min_distance(dist, visited)
            visited[u] = True

            for v in range(num_nodes):
                if not visited[v] and adj_matrix[u][v] and dist[u] != INF and dist[u] + adj_matrix[u][v] < dist[v]:
                    dist[v] = dist[u] + adj_matrix[u][v]

        print("Vertex Distance from Source")
        for i in range(num_nodes):
            print(f"{i}\t\t{dist[i]}")

    @staticmethod
    def min_distance(dist, visited):
        min_dist = sys.maxsize
        min_index = -1

        for v in range(len(dist)):
            if not visited[v] and dist[v] <= min_dist:
                min_dist = dist[v]
                min_index = v

        return min_index


if __name__ == "__main__":
    g = Graph()
    num_nodes = 5
    adj_list = [
        [0, 1, 1, 0, 0],
        [1, 0, 1, 1, 0],
        [1, 1, 0, 1, 0],
        [0, 1, 1, 0, 1],
        [0, 0, 0, 1, 0]
    ]

    adj_matrix = [
        [0, 1, 1, 0, 0],
        [1, 0, 1, 1, 0],
        [1, 1, 0, 1, 0],
        [0, 1, 1, 0, 1],
        [0, 0, 0, 1, 0]
    ]

    g.bfs(0, adj_list, num_nodes)
    print()
    g.dfs(0, adj_list, num_nodes)
    print()
    g.dijkstra(0, adj_matrix, num_nodes)
