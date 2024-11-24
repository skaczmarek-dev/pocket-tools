import unittest
from pocket_tools.pocket import get_pocket_data
import os

class TestPocketAPI(unittest.TestCase):

    def test_get_pocket_data(self):
        # Test fetching data from Pocket with valid settings file
        get_pocket_data('config/settings.json', 'test_output.json')
        self.assertTrue(os.path.exists('test_output.json'))

        # Cleanup
        os.remove('test_output.json')

if __name__ == '__main__':
    unittest.main()
