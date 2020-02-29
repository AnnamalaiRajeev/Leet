

class Node:
    def __init__(self, data):
        self.data = data
        self.vertices = []
        self.color = None


class GraphTree:
    Graph = []

    def __init__(self, data):
        if isinstance(data,list):
            self.graph_data = data
            self.make_graph()

    def make_graph(self):
        for i,node in enumerate(self.graph_data):
            node = Node(node)
            self.Graph.append(node)
        for node in self.Graph:
            for vertice in self.Graph:
                count = 0
                for k, char in enumerate(node.data):
                    # print(char,self.graph_data[j][k])
                    if char != vertice.data[k]:
                        count += 1
                    else:
                        pass
                if count == 1:
                    node.vertices.append(vertice)

    def __str__(self):
        for node in self.Graph:
            print((node.data, node.vertices))

    @staticmethod
    def Depth_first_search(starting_node, find_data):
        stack = [starting_node]
        visited_nodes = {}
        while stack:
            current = stack.pop()
            for vertice in current.vertices:
                if vertice not in visited_nodes:
                    stack.append(vertice)
            if current.data == find_data:
                print("dfs", current.data)
                return True
            print("dfs", current.data)
            visited_nodes[current] = 1
        return False

    @staticmethod
    def breadth_first_search(starting_node, find_data):
        stack = [starting_node]
        visited_nodes = {}
        while stack:
            current = stack.pop(0)
            for vertice in current.vertices:
                if vertice not in visited_nodes:
                    stack.append(vertice)
            if current.data == find_data:
                print("bfs", current.data)
                return True
            print("bfs", current.data)
            visited_nodes[current] = 1
        return False


if __name__ == '__main__':
    start = 'dog'
    end = 'hag'
    dictionary = ['dog', 'cat', 'hot', 'hog', 'eat']
    dictionary.append(end)
    GraphTree_1 = GraphTree(dictionary)
    for node in GraphTree_1.Graph:
        print(node.data, [vertice.data for vertice in node.vertices])

    assert(GraphTree_1.Depth_first_search(GraphTree_1.Graph[0], end))
    assert (GraphTree_1.breadth_first_search(GraphTree_1.Graph[0], end))
















