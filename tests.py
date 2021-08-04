import unittest

from main import Backpack


class BackpackTest(unittest.TestCase):

    def test_list_contents(self):
        self.assertEqual(Backpack().get_contents(), [])

    def test_add_item(self):
        b = Backpack()
        b.add('ax')
        self.assertEqual(b.get_contents(), ['ax'])

    def test_remove_item(self):
        b = Backpack()
        b.add('ax')
        self.assertEqual(b.get_contents(), ['ax'])
        b.remove('ax')
        self.assertEqual(b.get_contents(), [])

    def test_multiple_alphabetical(self):
        b = Backpack()
        b.add('ax')
        b.add('stick')
        b.add('Food')
        b.add('food')
        self.assertEqual(b.get_contents(), ['ax', 'Food', 'food', 'stick'])

    def test_get_counters(self):
        b = Backpack()
        b.add('ax')
        b.add('stick')
        b.add('Food')
        b.add('food')
        b.add('food')
        b.add('ax')
        self.assertEqual(b.get_counts(), {'ax': 2, 'stick': 1, 'Food': 1, 'food': 2})

    def test_most_popular(self):
        b = Backpack()
        b.add('ax')
        b.add('stick')
        b.add('Food')
        b.add('food')
        b.add('food')
        self.assertEqual(b.most_popular(), {'food': 2})

    def test_at_size(self):
        b = Backpack(size=5)
        b.add('ax')
        b.add('stick')
        b.add('Food')
        b.add('food')
        b.add('food')
        b.add('food')
        self.assertEqual(b.most_popular(), {'food': 3})
        self.assertEqual(b.get_counts(), {'stick': 1, 'Food': 1, 'food': 3})


if __name__ == '__main__':
    unittest.main()
