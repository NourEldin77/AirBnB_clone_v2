#!/usr/bin/python3
""" Tests For Base model """

import unittest
from models.base_model import BaseModel
import datetime


class TestBaseModel(unittest.TestCase):
    def test_init(self):
        """Test initialization of BaseModel instance"""
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)
        self.assertTrue(hasattr(model, 'id'))
        self.assertTrue(hasattr(model, 'created_at'))
        self.assertTrue(hasattr(model, 'updated_at'))
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime.datetime)
        self.assertIsInstance(model.updated_at, datetime.datetime)

    def test_save(self):
        """Test saving BaseModel instance"""
        model = BaseModel()
        created_at_before = model.created_at
        updated_at_before = model.updated_at
        model.save()
        self.assertNotEqual(updated_at_before, model.updated_at)
        self.assertEqual(created_at_before, model.created_at)

    def test_to_dict(self):
        """Test converting BaseModel instance to dictionary"""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertIn('__class__', model_dict)
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], model.id)
        self.assertEqual(model_dict['created_at'], model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], model.updated_at.isoformat())

    if __name__ == '__main__':
        unittest.main()
