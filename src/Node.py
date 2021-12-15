

class Node:

    def __init__(self, nid: int, loc: tuple):
        self.id = nid
        self.loc = loc
        self.edges_to = {}
        self.edges_from = {}

    # {0: 0: |edges out| 1 |edges in| 1
    def __repr__(self):
        return F"{self.id}: |edges out| {len(self.edges_to)} |edges in| {len(self.edges_from)}"
