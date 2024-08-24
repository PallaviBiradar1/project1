import unittest
from client3 import getDataPoint

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    # Testing for the first quote (ABC)
    stock, bid_price, ask_price, price = getDataPoint(quotes[0])
    expected_price_abc = (120.48 + 121.2) / 2
    self.assertAlmostEqual(price, expected_price_abc, places=2)

    # Testing for the second quote (DEF)
    stock, bid_price, ask_price, price = getDataPoint(quotes[1])
    expected_price_def = (117.87 + 121.68) / 2
    self.assertAlmostEqual(price, expected_price_def, places=2)

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    # Testing for the first quote (ABC)
    stock, bid_price, ask_price, price = getDataPoint(quotes[0])
    expected_price_abc = (120.48 + 119.2) / 2
    self.assertAlmostEqual(price, expected_price_abc, places=2)


  def test_getDataPoint_calculatePriceWithZeroBid(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 0, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'}
        ]

        # Testing for the quote (ABC)
        stock, bid_price, ask_price, price = getDataPoint(quotes[0])
        expected_price_abc = (0 + 121.2) / 2
        self.assertAlmostEqual(price, expected_price_abc, places=2)



if __name__ == '__main__':
    unittest.main()
