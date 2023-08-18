# Write your code below:
import surfshop
import unittest
import datetime

class surfshopTests(unittest.TestCase):
  def setUp(self):
    self.cart = surfshop.ShoppingCart()

  def test_add_surfboards_one(self):
    for num in range (2, 5):
      with self.subTest():
        result = self.cart.add_surfboards(num)
        print('testing the add_surfboards function using ' + str(num) + ' as the parameter')
        self.assertEqual(result, 'Successfully added {} surfboards to cart!'.format(num))
        self.cart = surfshop.ShoppingCart()

  def test_add_surfboards_two(self):
    self.assertEqual(self.cart.add_surfboards(2), 'Successfully added 2 surfboards to cart!')

  @unittest.skip('off season')
  def test_add_surfboards_error(self):
    self.assertRaises(surfshop.TooManyBoardsError, self.cart.add_surfboards, 5)

  # @unittest.expectedFailure
  def test_apply_local_discount(self):
    self.cart.apply_locals_discount()
    self.assertTrue(self.cart.locals_discount)
  
  def test_set_checkout_date_error(self):
    today = datetime.date.today()
    tomorrow = today.replace(day = today.day + 1)
    dates = [today, tomorrow]
    for current_date in dates:
      print('testing the set_checkout_date function using ' + str(current_date) + ' as the parameter')
      with self.subTest(current_date):
        self.assertRaises(surfshop.CheckoutDateError, self.cart.set_checkout_date, current_date)

unittest.main()