import json

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

def load_graph_from_json(filename='graph.json'):
    with open(filename, 'r') as file:
        vertices = json.load(file)
    
    mapa = Graph()
    mapa.vertices = vertices
    return mapa

# zobrazení mapy
def display_map(mapa):
    print("Mapa:")
    for uzel in mapa.vertices:
        print(f"Uzel {uzel}:")
        for soused, vzdalenost in mapa.vertices[uzel].items():
            print(f"  -> {soused} (vzdálenost: {vzdalenost})")

#  spojení mezi dvěma uzly a jejich délky
def find_connection(mapa, from_vertex, to_vertex):
    distance = mapa.get_edge_distance(from_vertex, to_vertex)
    if distance:
        print(f"Mezi uzly {from_vertex} a {to_vertex} existuje spojení o délce {distance}.")
    else:
        print(f"Mezi uzly {from_vertex} a {to_vertex} neexistuje spojení.")

# nalezení všech spojení mezi dvěma uzly
def find_all_connections(mapa):
    print("Všechna spojení mezi uzly:")
    for uzel in mapa.vertices:
        for soused, vzdalenost in mapa.vertices[uzel].items():
            print(f"{uzel} -> {soused} (vzdálenost: {vzdalenost})")

#  mapy z databáze
mapa = load_graph_from_json()

# Zobrazení  mapy
display_map(mapa)

#  spojení mezi dvěma libovolnými uzly
find_connection(mapa, 'G', 'F')

#  všechna spojení mezi dvěma uzly
find_all_connections(mapa)
