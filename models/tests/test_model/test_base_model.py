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
         


    