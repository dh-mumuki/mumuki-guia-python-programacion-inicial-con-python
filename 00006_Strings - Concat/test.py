class TestFixtures(unittest.TestCase):
   def test_concat(self):
      self.assertEqual(concat_lista(['1', '5', '4']), '154' ) 
      