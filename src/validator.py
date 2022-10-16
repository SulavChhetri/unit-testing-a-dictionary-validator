class Validator:
    def __init__(self, input_dictionary, validation_dictionary):
        self.input_dictionary = input_dictionary
        self.validation_dictionary = validation_dictionary

    def type1(self,value, standard, input):
        if not (type(value) == standard):
            print(
                f'The type of {input} must be {standard} but is {type(value)}')
            return False

    def minlength(self,value, standard, input):
        if not (len(value) >= standard):
            print(
                f'The minimum length of {input} must be {standard} but is {len(value)}')
            return False

    def maxlength(self,value, standard, input):
        if not (len(value) <= standard):
            print(
                f'The maxmimum length of {input} must be {standard} but is {len(value)}')
            return False

    def minimum(self,value, standard, input):
        if not (value >= standard):
            print(
                f'The minimum value of {input} must be {standard} but is {value}')
            return False

    def maximum(self,value, standard, input):
        if not (value <= standard):
            print(
                f'The maximum value of {input} must be {standard} but is {value}')
            return False

    def nestedlist(self,value, standard):
        if (type(value) == list):
            for item in value:
                x = Validator.validator(item, standard)
                if x == False:
                    return False
        elif (type(value) == dict):
            x = Validator.validator(value, standard)
            if x == False:
                return False

    def validator(self):
        if not self.input_dictionary.keys() == self.validation_dictionary.keys():
            return False
        else:
            for key in self.validation_dictionary.keys():
                value = self.input_dictionary.get(key)
                rule = self.validation_dictionary.get(key)
                for function in rule.keys():
                    if (function == 'type' and Validator.type1(self,value, rule[function], key) == False):
                        return False
                    elif (function == 'minlength' and Validator.minlength(self,value, rule[function], key) == False):
                        return False
                    elif (function == 'maxlength' and Validator.maxlength(self,value, rule[function], key) == False):
                        return False
                    elif (function == 'minimum' and Validator.minimum(self,value, rule[function], key) == False):
                        return False
                    elif (function == 'maximum' and Validator.maximum(self,value, rule[function], key) == False):
                        return False
                    elif (function == 'item_nesteddict' and Validator.nestedfunction(self,value, rule[function]) == False):
                        return False
            return True


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
validator = Validator(input_dictionary, validation_dictionary)
print(validator.validator())
