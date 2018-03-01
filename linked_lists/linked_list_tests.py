import unittest
from linked_list import *

class LinkedListTests(unittest.TestCase):

    def test_empty_list_should_have_no_head(self):
        list = LinkedList()
        self.assertIsNone(list.head)

    def test_adding_one_value_should_create_head(self):
        list = LinkedList()
        list.insert("First")
        self.assertIsNotNone(list.head)
        self.assertEqual(list.head.data, "First")

    def test_inserting_second_value_should_replace_head(self):
        list = LinkedList()
        list.insert("First")
        list.insert("Second")
        self.assertEqual(list.head.data, "Second")

    def test_inserting_second_value_should_move_existing_head_to_next(self):
        list = LinkedList()
        list.insert("First")
        list.insert("Second")
        self.assertEqual(list.head.next.data, "First")

    def test_appending_first_value_should_set_head(self):
        list = LinkedList()
        list.append("First")
        self.assertEqual(list.head.data, "First")

    def test_appending_second_value_should_set_head_next(self):
        list = LinkedList()
        list.append("First")
        list.append("Second")
        self.assertEqual(list.head.next.data, "Second")

    def test_is_empty_should_be_true_if_no_head(self):
        list = LinkedList()
        self.assertTrue(list.is_empty())

if __name__ == '__main__':
    unittest.main()