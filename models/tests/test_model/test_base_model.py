#!/usr/bin/env python3

'''

'''
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def test_init(self):
          my_model = BaseModel()
          self.assertIsNone(my_model.id)
          self.assertIsNone(my_model.created_at)
          self.assertIsNone(my_model.updated_at)

    def test_save(self):
         my_model = BaseModel()
         
         initial_updated_at = my_model.updated_at
         current_updated_at = my_model.save()

         self.assertNotEqual(initial_updated_at, current_updated_at)

    def test_to_dict(self):
         my_model = BaseModel()

         my_model_dict = my_model.to_dict()

         self.assertIsInstance(my_model_dict, dict)

         self.assertEqual(my_model_dict["__class__"], 'BaseModel')
         self.assertEqual(my_model_dict['id'], my_model.id)
         self.assertEqual(my_model_dict['created_at'], my_model.created_at.isoformat())
         self.assertEqual(my_model_dict['updated_at'], my_model.updated_at.isoformat())
         
    