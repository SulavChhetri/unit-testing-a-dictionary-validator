from typing import Type
from unittest import TestCase
from src.validator import Validator


class TestValidator(TestCase):

    def setUp(self):
        self.input_dictionary = {
            "name": "Sulav",
            "age": 22,
            "city": "Syangja",
            "isEngineer": True
        }
        self.validation_dictionary = {
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
        self.validator = Validator(self.input_dictionary, self.validation_dictionary)

    def test_initialization(self):
        self.assertEqual(isinstance(self.validator, Validator), True)

        self.assertEqual(self.validator.input_dictionary, self.input_dictionary)
        self.assertEqual(self.validator.validation_dictionary,self.validation_dictionary)

        # edge case for the dictionaries
        self.assertRaises(TypeError, Validator,['name', 'age', 'city'] ,self.validation_dictionary)
        self.assertRaises(TypeError, Validator,self.input_dictionary, (1,2,"int") )
    

    def test_validator(self):
        #Checking if the keys of both dictionaries are equal or not
        self.assertEqual(self.input_dictionary.keys(),self.validation_dictionary.keys())
    

    def test_type1(self):
        test_value_inputdict = "Sulav"
        test_value_valdict_key_value = str
        test_x = "Hari"
        test_y = int
        #Checking the type of the input value with the validation
        self.assertEqual(type(test_value_inputdict),test_value_valdict_key_value,"Should be a String")
        #edge cases that may occur
        # self.assertRaises(TypeError,lambda test_x,test_y: False if type(test_x)!= test_y else True,test_x,test_y)

    def test_minlength(self):
        test_value_inputdict = "Sulav"
        test_value_valdict_key_value = 4
        self.assertGreaterEqual(len(test_value_inputdict),test_value_valdict_key_value)

    def test_maxlength(self):
        test_value_inputdict = "Sulav"
        test_value_valdict_key_value = 10
        self.assertLessEqual(len(test_value_inputdict),test_value_valdict_key_value)

    def test_minimum(self):
        test_value_inputdict = 22
        test_value_valdict_key_value = 0
        self.assertGreaterEqual(test_value_inputdict,test_value_valdict_key_value)

    def test_maximum(self):
        test_value_inputdict = 22
        test_value_valdict_key_value = 150
        self.assertLessEqual(test_value_inputdict,test_value_valdict_key_value)

    def test_item_nesteddict(self):
        test_value_inputdict = [{}]
        