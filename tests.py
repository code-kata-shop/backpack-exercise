import unittest

from main import Backpack


class BackpackTest(unittest.TestCase):

    def test_list_contents(self):
        self.assertEquals(Backpack().get_contents(), [])

    def test_add_item(self):
        b = Backpack()
        b.add('ax')
        self.assertEquals(b.get_contents(), ['ax'])

    def test_remove_item(self):
        b = Backpack()
        b.add('ax')
        self.assertEquals(b.get_contents(), ['ax'])
        b.remove('ax')
        self.assertEquals(b.get_contents(), [])

    def test_multiple_alphabetical(self):
        b = Backpack()
        b.add('ax')
        b.add('stick')
        b.add('Food')
        b.add('food')
        self.assertEquals(b.get_contents(), ['ax', 'Food', 'food', 'stick'])

    def test_get_counters(self):
        b = Backpack()
        b.add('ax')
        b.add('stick')
        b.add('Food')
        b.add('food')
        b.add('food')
        b.add('ax')
        self.assertEquals(b.get_counts(), {'ax': 2, 'stick': 1, 'Food': 1, 'food': 2})

    def test_most_popular(self):
        b = Backpack()
        b.add('ax')
        b.add('stick')
        b.add('Food')
        b.add('food')
        b.add('food')
        self.assertEquals(b.most_popular(), {'food': 2})


if __name__ == '__main__':
    unittest.main()
