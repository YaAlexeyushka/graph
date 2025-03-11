from graph import Graph  

def test_add_edge():
    g = Graph()
    g.add_edge('A', 'B', 10)
    g.add_edge('A', 'C', 20)
    
    assert 'A' in g.graph
    assert 'B' in g.graph
    assert 'C' in g.graph
    assert g.get_weight('A', 'B') == 10
    assert g.get_weight('A', 'C') == 20

def test_get_accessible_vertices():
    g = Graph()
    g.add_edge('A', 'B', 10)
    g.add_edge('A', 'C', 20)
    
    accessible_vertices = g.get_accessible_vertices('A')
    assert 'B' in accessible_vertices
    assert 'C' in accessible_vertices
    assert len(accessible_vertices) == 2

def test_calculate_way_weight():
    g = Graph()
    g.add_edge('A', 'B', 10)
    g.add_edge('B', 'C', 15)
    g.add_edge('C', 'D', 20)
    
    way = ['A', 'B', 'C', 'D']
    weight = g.calculate_way_weight(way)
    
    assert weight == 45 

def test_get_vertices():
    g = Graph()
    g.add_edge('A', 'B', 10)
    g.add_edge('A', 'C', 20)
    
    vertices = g.get_vertices()
    assert 'A' in vertices
    assert 'B' in vertices
    assert 'C' in vertices
    assert len(vertices) == 3
