import unittest
from doubly_linked_list import *

class DoublyLinkedListTests(unittest.TestCase):
    def test_empty_list_should_have_no_head(self):
        list = DoublyLinkedList()
        self.assertIsNone(list.head)

    def test_empty_list_should_have_no_length(self):
        list = DoublyLinkedList()
        self.assertEqual(len(list), 0)

    def test_inserting_one_value_should_create_head(self):
        list = DoublyLinkedList()
        list.insert("First")
        self.assertIsNotNone(list.head)
        self.assertEqual(list.head.data, "First")

    def test_inserting_one_value_should_update_length(self):
        list = DoublyLinkedList()
        list.insert("First")
        self.assertIsNotNone(list.head)
        self.assertEqual(len(list), 1)

    def test_inserting_second_value_should_replace_head(self):
        list = DoublyLinkedList()
        list.insert("First")
        list.insert("Second")
        self.assertEqual(list.head.data, "Second")

    def test_inserting_second_value_should_move_existing_head_to_next(self):
        list = DoublyLinkedList()
        list.insert("First")
        list.insert("Second")
        self.assertEqual(list.head.next.data, "First")

    def test_appending_first_value_should_set_head(self):
        list = DoublyLinkedList()
        list.append("First")
        self.assertEqual(list.head.data, "First")

    def test_appending_first_value_should_update_length(self):
        list = DoublyLinkedList()
        list.append("First")
        self.assertEqual(len(list), 1)

    def test_appending_second_value_should_set_head_next(self):
        list = DoublyLinkedList()
        list.append("First")
        list.append("Second")
        self.assertEqual(list.head.next.data, "Second")

    def test_appending_second_value_should_have_valid_previous_in_second_node(self):
        list = DoublyLinkedList()
        list.append("First")
        list.append("Second")
        second_added_node = list.head.next
        self.assertEqual(second_added_node.previous.data, "First")

    def test_find_on_empty_list_should_return_none(self):
        list = DoublyLinkedList()
        self.assertIsNone(list.find("First"))

    def test_find_should_match_valid_node_in_one_value_list(self):
        list = DoublyLinkedList()
        list.append("First")
        self.assertIsNotNone(list.find("First"))

    def test_find_should_match_valid_node_in_multi_value_list(self):
        list = DoublyLinkedList()
        list.append("First")
        list.append("Second")
        self.assertIsNotNone(list.find("Second"))

    def test_is_empty_should_be_true_if_no_head(self):
        list = DoublyLinkedList()
        self.assertTrue(list.is_empty())

    def test_get_on_empty_list_should_return_index_error(self):
        list = DoublyLinkedList()
        self.assertRaises(IndexError, list.get, 0)
    
    def test_get_with_negative_index_should_raise_index_error(self):
        list = DoublyLinkedList()
        self.assertRaises(IndexError, list.get, -1)

    def test_get_should_return_correct_node(self):
        list = DoublyLinkedList()
        list.append("First")
        list.append("Second")
        
        node = list.get(1)
        self.assertEqual(node.data, "Second")


if __name__ == '__main__':
    unittest.main()