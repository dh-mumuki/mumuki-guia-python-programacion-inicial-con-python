class TestFixtures(unittest.TestCase):
  def test_True(self):
    self.assertTrue(estar_en_lista([1, 5, 8, 3], 5))

  def test_False(self):
    self.assertFalse(estar_en_lista([1, 5, 8, 3], 2))