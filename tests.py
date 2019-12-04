import unittest
from collections import Counter

from servers import ListServer, Product, Client, MapServer,TooManyProductsFoundError

server_types = (ListServer, MapServer)


class ServerTest(unittest.TestCase):
    def test_exception(self):
        with self.assertRaises(TooManyProductsFoundError):
            max=ListServer.n_max_returned_entries
            p=Product('a12',1)
            ls=ListServer([p for i in range(max+1)])
            ls.get_entries(1)
    def test_get_entries_returns_proper_entries(self):
        products = [Product('P12', 1), Product('PP234', 2), Product('PP235', 1)]
        for server_type in server_types:
            server = server_type(products)
            entries = server.get_entries(2)
            self.assertEqual(Counter([products[2], products[1]]), Counter(entries))



class ClientTest(unittest.TestCase):
    def test_total_price_for_normal_execution(self):
        products = [Product('PP234', 2), Product('PP235', 3)]
        for server_type in server_types:
            server = server_type(products)
            client = Client(server)
            self.assertEqual(5, client.get_total_price(2))
    def test_catch_exception(self):
        max = ListServer.n_max_returned_entries
        p = Product('a12', 1)
        ls = ListServer([p for i in range(max + 1)])
        c=Client(ls)
        self.assertEqual(None,c.get_total_price(1))


if __name__ == '__main__':
    unittest.main()

