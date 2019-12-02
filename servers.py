#Michal Gorczyca 302846
# !/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Optional, List, Dict


class Product:
    def __init__(self, product_name, product_price):
        self.__product_name = product_name
        self.__product_price = product_price
    def get_product_name(self):
        return self.__product_name
    def get_product_price(self):
        return self.__product_price


class TooManyProductsFoundError:
    # Reprezentuje wyjątek związany ze znalezieniem zbyt dużej liczby produktów.
    pass



class ListServer:
    def __init__(self, product_list):
        self.__product_list = product_list

    def find(self, n: int) -> List[Product]:
        pass


class MapServer:
    def __init__(self, product_dict):
        self.__product_dict = product_dict

    def find(self, n: int) -> List[Product]:
        pass


class Client:
    def __init__(self, server):
        self.server = server

    def get_total_price(self, n_letters: Optional[int]) -> Optional[float]:
        raise NotImplementedError()
