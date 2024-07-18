import unittest


class ConnectedGraphII:
    """
    Givennnodes in a graph labeled from1ton. There is no edges in the graph at beginning.

    You need to support the following method:
    1.connect(a, b), an edge to connect node a and node b
    2.query(a), Returns the number of connected component nodes which include node a
    """
    
    def __init__(self, n) -> None:
        self.count = [1 for _ in range(0, n)]
        self.parent = [i for i in range(0, n)]
    
    def connect(self, a, b):
        """ when connected a, add children's count to parent
        """

        
        roota = self._find(a)
        rootb = self._find(b)
        
        if roota != rootb:
            self.parent[rootb] = roota
            self.count[roota] += self.count[rootb]
            self.count[rootb] = self.count[roota]
            print(f"parent: {self.parent}")
            print(f"count: {self.count}")
            
    
    def query(self, a):
        """ iterate all node, count is_connected(a, i)
        """        
        return self.count[self._find(a)]
        
    def _find(self, a):
        if self.parent[a] == a:
            return a
        
        self.parent[a] = self._find(self.parent[a])
        return self.parent[a]
    
        

class TestUnionFind(unittest.TestCase):
    def test_connected_graph(self):
        cg = ConnectedGraphII(4)
        cg.connect(1, 2)
        cg.connect(2, 3)
        self.assertEqual(3, cg.query(1))
        self.assertEqual(3, cg.query(2))
        self.assertEqual(3, cg.query(3))
     
    
if __name__ == "__main__":
    t = TestUnionFind()
    t.run()
