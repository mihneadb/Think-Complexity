__author__ = 'Mihnea'

class Graph(dict):
    def __init__(self, vs=[], es=[]):
        """Create a new graph. vs is a list of vertices,
        es is a list of edges"""
        for v in vs:
            self.add_vertex(v)

        for e in es:
            self.add_edge(e)

    def add_vertex(self, v):
        """ adds v to the graph. If it already is present, nothing changes
        """
        self[v] = {} if v not in self else self[v]

    def add_edge(self, e):
        """ adds e to the graph (both directions). Replaces an existing edge
        """
        # obtain the vertices
        u, v = e

        # add them to the inner dict
        self[u][v] = e
        self[v][u] = e

    def get_edge(self, u, v):
        """ returns the Edge between u and v, if it exists. None otherwise
        """
        if u in self:
            edges = self[u]
            if v in edges:
                return edges[v]
        return None

    def remove_edge(self, e):
        """ remove all references of e from the graph
        """
        # obtain the vertices
        u, v = e
        if u in self:
            edges = self[u]
            if v in edges:
                del edges[v]
                del self[v][u]

class Vertex(object):
    def __init__(self, label=''):
        self.label = label

    def __repr__(self):
        return 'Vertex(%s)' % repr(self.label)

    __str__ = __repr__


class Edge(tuple):
    def __new__(cls, u, v):
        return tuple.__new__(cls, (u, v))

    def __repr__(self):
        return 'Edge(%s, %s)' % (repr(self[0]), repr(self[1]))

    def vertices(self):
        return (self[0], self[1])

    __str__ = __repr__



if __name__ == '__main__':
    v = Vertex('v')
    w = Vertex('w')
    e = Edge(v, w)
    print e
    g = Graph([v, w], [e])
    print g
    print g.get_edge(w, v)
    print g.get_edge(w, Vertex('lulu'))
    g.remove_edge(e)
    print g
