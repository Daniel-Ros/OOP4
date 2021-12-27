from GUI.Drawer import Drawer
from DiGraph import DiGraph
from GraphAlgo import GraphAlgo


def main():
    g = DiGraph()
    ga = GraphAlgo(g)
    d = Drawer(ga)
    d.main()

if __name__=="__main__":
    main()