class TestFixtures(unittest.TestCase):
  def test_impares(self):
    self.assertEquals(impares(8), [1,3,5,7])
  def test_iimpares(self):
    self.assertEquals(impares(9), [1,3,5,7])
