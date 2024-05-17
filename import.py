import json
import os

class Graph:
    def __init__(self):
        self.vertices = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = {}
    
    def add_edge(self, from_vertex, to_vertex, distance, directed=False):
        self.add_vertex(from_vertex)
        self.add_vertex(to_vertex)
        self.vertices[from_vertex][to_vertex] = distance
        if not directed:
            self.vertices[to_vertex][from_vertex] = distance
    
    def get_edge_distance(self, from_vertex, to_vertex):
        if from_vertex in self.vertices and to_vertex in self.vertices[from_vertex]:
            return self.vertices[from_vertex][to_vertex]
        return None

def load_map_from_database():
    mapa = Graph()

    uzly = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    for uzel in uzly:
        mapa.add_vertex(uzel)
# zde se zapíšou všechny potřebné hodnoty

    mapa.add_edge('A', 'B', 10)
    mapa.add_edge('B', 'C', 15)
    mapa.add_edge('C', 'D', 5)
    mapa.add_edge('D', 'E', 20)
    mapa.add_edge('E', 'F', 10)
    mapa.add_edge('F', 'G', 10)
    mapa.add_edge('G', 'H', 5)
    mapa.add_edge('H', 'I', 5)
    mapa.add_edge('I', 'D', 15)
    mapa.add_edge('B', 'D', 10)
    mapa.add_edge('F', 'E', 3)
    mapa.add_edge('E', 'C', 7)
    mapa.add_edge('C', 'A', 8)
    mapa.add_edge('G', 'B', 12)
    
    return mapa

def save_graph_to_json(mapa, filename='graph.json'):
    try:
        with open(filename, 'w') as file:
            json.dump(mapa.vertices, file)
        print(f"Graph successfully saved to {filename}")
    except Exception as e:
        print(f"An error occurred while saving the graph: {e}")

mapa = load_map_from_database()
save_graph_to_json(mapa)
