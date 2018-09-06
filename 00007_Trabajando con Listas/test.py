class TestFixtures(unittest.TestCase):
   def test_248(self):
      self.assertEquals(suma(1, 2), 3)

   def test_suma_1_y_3(self):
      self.assertEquals(suma(1, 3), 4)

   def test_suma_5_y_100(self):
      self.assertEquals(suma(5, 100), 105)