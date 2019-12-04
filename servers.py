# Paweł Kolendo 302860
# !/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Optional, List, Dict
import re
from abc import ABC, abstractmethod


class Product:
    def __init__(self, product_name, product_price):
        self.product_name = product_name
        self.product_price = product_price

        def __hash__(self):
            return hash((self.name, self.price))

        def __eq__(self, other):
            return self.name == other.name and self.price == other.price



class TooManyProductsFoundError(Exception):
    def __init__(self, msg=None):
        if msg == None:
            msg = "Too many products found"
        super().__init__(msg)


class Server(ABC):
    n_max_returned_entries = 3
    @abstractmethod
    def get_entries(self, n):
        raise NotImplementedError()


class ListServer(Server):
    #n_max_returned_entries = 3

    def __init__(self, product_list):
        self.product_list = product_list

    def get_entries(self, n) -> List[Product]:
        list = []
        for el in self.product_list:
            a = re.match('^[a-zA-Z]{{{}}}\\d{{2,3}}$'.format(n), el.product_name)
            if a != None:
                list.append(el)
        if len(list) > self.n_max_returned_entries:
            raise TooManyProductsFoundError()


        return sorted(list, key = lambda p:p.product_price)


class MapServer(Server):
    #n_max_returned_entries = 3

    def __init__(self, product_list):
        self.product_dict = {}
        for el in product_list:
            self.product_dict[el.product_name] = el

    def get_entries(self, n: int) -> List[Product]:
        list = []
        for el in self.product_dict:
            a = re.match('^[a-zA-Z]{{{}}}\\d{{2,3}}$'.format(n), el)
            if a != None:
                list.append(self.product_dict[el])
        if len(list) > self.n_max_returned_entries:
            raise TooManyProductsFoundError()

        return sorted(list, key = lambda p:p.product_price)


class Client:
    def __init__(self, server):
        self.server = server

    def get_total_price(self, n_letters: Optional[int]) -> Optional[float]:
        try:
            lst = self.server.get_entries(n_letters)
        except TooManyProductsFoundError:
            return None

        total = 0
        for x in lst:
            total += x.product_price
        return total


p = Product('xd126', 4)
p2 = Product('xg12', 2)
p3= Product('es164', 6)
x = MapServer([p,p2,p3])
c = Client(x)

print(c.get_total_price(2))
