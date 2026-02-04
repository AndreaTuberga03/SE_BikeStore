from UI.view import View
from model.model import Model
import flet as ft
import datetime

class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

        self._list_category = []

    def set_dates(self):
        first, last = self._model.get_date_range()

        self._view.dp1.first_date = datetime.date(first.year, first.month, first.day)
        self._view.dp1.last_date = datetime.date(last.year, last.month, last.day)
        self._view.dp1.current_date = datetime.date(first.year, first.month, first.day)

        self._view.dp2.first_date = datetime.date(first.year, first.month, first.day)
        self._view.dp2.last_date = datetime.date(last.year, last.month, last.day)
        self._view.dp2.current_date = datetime.date(last.year, last.month, last.day)

    def handle_crea_grafo(self, e):
        """ Handler per gestire creazione del grafo """

        # Prendo la categoria selezionata dal dropdown
        selected_category = self._view.dd_category.value
        # Controllo che abbia un valore
        if selected_category is None:
            self._view.show_alert("Categoria Invalida")
            return
        date1 = self._view.dp1.value
        date2 = self._view.dp2.value

        # Pulisce area risultato
        self._view.txt_risultato.controls.clear()

        # Costruisce grafo con i parametri selezionati
        self._model.build_graph(selected_category, date1, date2)

        # Mostra info grafo
        self._view.txt_risultato.controls.append(
            ft.Text(
                f"Numero di nodi: {self._model.get_num_of_nodes()} "
                f"Numero di archi: {self._model.get_num_of_edges()}"
            )
        )

        # Mostra somma pesi per nodo
        for node_info in self._model.get_sum_weight_per_node():
            self._view.lista_visualizzazione_1.controls.append(
                ft.Text(f"Nodo {node_info[0]}, somma pesi su archi = {node_info[1]}")
            )

        self._view.update()

    def handle_best_prodotti(self, e):
        """ Handler per gestire la ricerca dei prodotti migliori """
        # TODO

    def handle_cerca_cammino(self, e):
        """ Handler per gestire il problema ricorsivo di ricerca del cammino """
        # TODO

    def populate_dd (self):
        """ Metodo per popolare il dd """
        category_list = self._model.list_categories()

        # Popola lista anni unici
        for n in category_list:
            self._list_category.append(n.category_name)
        # Popola dropdown anni
        for categ in self._list_category:
            self._view.dd_category.options.append(ft.dropdown.Option(categ))
        self._view.update()