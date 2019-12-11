# Paweł Kolendo 302860
# Michał Gorczyca 302846
# Michał Kasperek 302857
# !/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Optional, List, Dict
import re
from abc import ABC, abstractmethod


class Product:
    def __init__(self, product_name, product_price):
        self.name = product_name
        self.price = product_price

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
    n_max_returned_entries = 6
    @abstractmethod
    def get_entries(self, n_letters):
        raise NotImplementedError()


class ListServer(Server):
    #n_max_returned_entries = 3

    def __init__(self, products):
        self.product_list = products

    def get_entries(self, n_letters) -> List[Product]:
        list = []
        for el in self.product_list:
            a = re.match('^[a-zA-Z]{{{}}}\\d{{2,3}}$'.format(n_letters), el.name)
            if a != None:
                list.append(el)
        if len(list) > self.n_max_returned_entries:
            raise TooManyProductsFoundError()
        return sorted(list, key=lambda p:p.price)


class MapServer(Server):
    #n_max_returned_entries = 3

    def __init__(self, products):
        self.product_dict = {}
        for el in products:
            self.product_dict[el.name] = el

    def get_entries(self, n_letters: int) -> List[Product]:
        list = []
        for el in self.product_dict:
            a = re.match('^[a-zA-Z]{{{}}}\\d{{2,3}}$'.format(n_letters), el)
            if a != None:
                list.append(self.product_dict[el])
        if len(list) > self.n_max_returned_entries:
            raise TooManyProductsFoundError()

        return sorted(list, key = lambda p:p.price)


class Client:
    def __init__(self, server):
        self.server = server

    def get_total_price(self, n_letters: Optional[int]) -> Optional[float]:
        try:
            lst = self.server.get_entries(n_letters)
        except TooManyProductsFoundError:
            return None
        if len(lst)==0:
            return None
        total = 0
        for x in lst:
            total += x.price
        return total
