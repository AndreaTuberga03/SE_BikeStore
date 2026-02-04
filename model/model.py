from database.dao import DAO
import networkx as nx

class Model:
    def __init__(self):
        self.list_products = []

        self.G = nx.Graph()
        self._nodes = []
        self._edges = []
        self.id_map = {}
        self.sol_best = 0

    def get_date_range(self):
        return DAO.get_date_range()

    def get_products(self, categ):
        return DAO.get_prod(categ)

    def list_categories(self):
        return DAO.get_categories()

    def build_graph(self, c, d1, d2):
        self.G.clear()
        print(c)

        self.list_products = self.get_products(c)

        for p in self.list_products:  # per ogni prodotto nella lista
            self._nodes.append(p)  # lo aggiungo alla lista dei nodi

        self.G.add_nodes_from(self._nodes)  # aggiungo i nodi al grafo
        self.id_map = {}
        for n in self._nodes:  # per ogni nodo
            self.id_map[n.id] = n  # lo aggiungo al dizionario id_map con chiave l'id e valore il nodo

        tmp_edges = DAO.get_all_weighted_neigh(c, d1, d2)  # chiamo funz e passo forma e anni

        self._edges.clear()
        for e in tmp_edges:  # per ogni arco pesato
            self._edges.append((self.id_map[e[0]], self.id_map[e[1]], e[2]))
            # id_map[e[0]] è il primo nodo, e vado a prenderlo dentro id_map
            # id_map[e[1]] è il secondo nodo, e vado a prenderlo dentro id_map
            # e[2] è il peso dell'arco che unisce i due nodi

        self.G.add_weighted_edges_from(self._edges)