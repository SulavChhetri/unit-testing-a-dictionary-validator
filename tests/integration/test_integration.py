import unittest
from unittest import TestCase
from src.validator import Validator


class TestValidator(TestCase):
    def setUp(self):
        input_dictionary = {
            "name": "Sulav",
            "age": 22,
            "city": "Syangja",
            "isEngineer": True
        }
        validation_dictionary = {
            "name": {
                "type": str,
                'minlength': 4,
                'maxlength': 10
            },
            'age': {
                'type': int,
                'minimum': 0,
                'maximum': 150
            },
            'city': {
                'type': str
            },
            'isEngineer': {
                'type': bool
            }
        }
        self.validator = Validator(input_dictionary, validation_dictionary)

    def test_initialization(self):
        self.assertEqual(isinstance(self.validator, Validator), True)

        self.assertEqual(self.validator.input_dictionary, {
            "name": "Sulav",
            "age": 22,
            "city": "Syangja",
            "isEngineer": True
        })

        # edge case for the dictionaries
        self.assertTrue(type(self.validator.validation_dictionary),
                        type(self.validator.input_dictionary))

    def test_type(self):
        test_value = 'Sulav'
        test_rule = str
        input = "name"
        # check if the type of the input is acc to the standard
        self.assertEqual(self.validator.type1(test_value,test_rule,input), None)

    def test_minlength(self):
        test_value = "Putalibazar"
        test_min_length = 5
        input = 'city'
        # Check if the length of the value is greater than or equal to test_min_length
        self.assertGreaterEqual(self.validator.minlength(test_value,test_min_length,input), None)

    def test_maxlength(self):
        test_value = "Putalibazar"
        test_max_length = 25
        input = 'city'
        # check if the length of the value is less than or equal to the test_max_length
        self.assertLessEqual(self.validator.minlength(test_value,test_max_length,input), None)

    def test_minimum(self):
        test_value = 22
        test_min = 0
        input = "age"
        # check if the test_value is greater than or equal to the test_min
        self.assertGreaterEqual(self.validator.minimum(test_value,test_min,input),None)

    def test_maxmimum(self):
        test_value = 22
        test_max = 150
        input = 'age'
        # check if the test_value is less than or equal to the test_min
        self.assertLessEqual(self.validator.minimum(test_value,test_max,input),None)


    def test_validator(self):
        # Checking if the keys of both dictionaries are equal or not
        self.assertEqual(self.validator.input_dictionary.keys(),
                         self.validator.validation_dictionary.keys(), True)

        self.assertEqual(self.validator.type1("Sulav",str,'name'), None,"Should be None, because the function only returns false if the inputs are incorrect")
        self.assertEqual(self.validator.minlength("Sulav",4,'name'), None,"Should be None, because the function only returns false if the inputs are incorrect")
        self.assertEqual(self.validator.maxlength("Sulav",14,'name'), None,"Should be None, because the function only returns false if the inputs are incorrect")
        self.assertEqual(self.validator.minimum(22,0,'age'), None,"Should be None, because the function only returns false if the inputs are incorrect")
        self.assertEqual(self.validator.maximum(22,150,'age'), None,"Should be None, because the function only returns false if the inputs are incorrect")
    