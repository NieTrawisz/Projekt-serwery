#Michal Gorczyca 302846
# !/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Optional, List, Dict


class Product():
    def __init__(self, product_name, product_price):
        self.product_name = product_name
        self.product_price = product_price
    def get_product_name(self):
        return self.product_name
    def get_product_price(self):
        return self.product_price


class TooManyProductsFoundError:
    # Reprezentuje wyjątek związany ze znalezieniem zbyt dużej liczby produktów.
    pass



class ListServer():
    def __init__(self, product_list, n_max_returned_entries):
        self.product_list = product_list
        self.n_max_returned_entries = n_max_returned_entries

    def find(self, n: int) -> List[Product]:
        pass


class MapServer:
    def __init__(self, product_dict, n_max_returned_entries):
        self.product_dict = product_dict
        self.n_max_returned_entries = n_max_returned_entries

    def find(self, n: int) -> List[Product]:
        pass


class Client:
    def __init__(self, server):
        self.server = server

    def get_total_price(self, n_letters: Optional[int]) -> Optional[float]:
        raise NotImplementedError()


