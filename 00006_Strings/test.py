class TestFixtures(unittest.TestCase):
   def test_concat(self):
      self.assertEquals(concat_lista([1, 5, 12, 2]), str(15122))