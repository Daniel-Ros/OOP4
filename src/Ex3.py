from src.GUI.Drawer import Drawer
from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo


def main():
    g = DiGraph()
    ga = GraphAlgo(g)
    d = Drawer(ga)
    d.main()

if __name__=="__main__":
    main()