from unittest import TestCase
from src.validator import Validator
from unittest.mock import patch

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
        # check if the type of the input is acc to the standard
        self.assertEqual(type(test_value), test_rule, True)

    def test_minlength(self):
        test_value = "Putalibazar"
        test_min_length = 5
        # Check if the length of the value is greater than or equal to test_min_length
        self.assertGreaterEqual(len(test_value), test_min_length, True)

    def test_maxlength(self):
        test_value = "Putalibazar"
        test_max_length = 25
        # check if the length of the value is less than or equal to the test_max_length
        self.assertLessEqual(len(test_value), test_max_length, True)

    def test_minimum(self):
        test_value = 22
        test_min = 0
        # check if the test_value is greater than or equal to the test_min
        self.assertGreaterEqual(test_value, test_min, True)

    def test_maxmimum(self):
        test_value = 22
        test_max = 150
        # check if the test_value is less than or equal to the test_min
        self.assertLessEqual(test_value, test_max, True)


    @patch('src.validator.Validator.validator')
    def test_nestedlist(self,mock_validator):
        test_value = [
            {'name': 'Faketown', 'population': 3},
            {'name': 'Evergreen', 'population': 4}
        ]
        test_rule = {
            'name': {
                'type': str,
                'minlength': 4,
                'maxlength': 10
            },
            'population': {
                'type': int,
                'minimum': 0,
            },
        }
        mock_validator.return_value = [False, True]
        #Check whether the input value is of type list or dict ; if list, send the item of that list+ test_value as argument to the validator function
        self.assertEqual(type(test_value), list,True)
        self.assertEqual(self.validator.validator()[0],False)
        self.assertEqual(self.validator.validator()[1],True)
    
    @patch('src.validator.Validator.type1', return_value = False)
    @patch('src.validator.Validator.minlength', return_value = False)
    @patch('src.validator.Validator.maxlength', return_value = False)
    @patch('src.validator.Validator.minimum', return_value = False)
    @patch('src.validator.Validator.maximum', return_value = False)
    @patch('src.validator.Validator.nestedlist', return_value = False)
    def test_validator(self,mock_type1,mock_minlength,mock_maxlength,mock_minimum,mock_maximum,mock_nestedlist):
        # Checking if the keys of both dictionaries are equal or not
        self.assertEqual(self.validator.input_dictionary.keys(),
                         self.validator.validation_dictionary.keys(), True)

        self.assertEqual(self.validator.type1(), False,"Should be False")
        self.assertEqual(self.validator.minlength(), False,"Should be False")
        self.assertEqual(self.validator.maxlength(), False,"Should be False")
        self.assertEqual(self.validator.minimum(), False,"Should be False")
        self.assertEqual(self.validator.maximum(), False,"Should be False")
        self.assertEqual(self.validator.nestedlist(), False,"Should be False")
    
    