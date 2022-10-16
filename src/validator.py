class Validator:
    def __init__(self,input_dictionary,validation_dictionary):
        self.input_dictionary = input_dictionary
        self.validation_dictionary = validation_dictionary

#     def type1(value,standard,input):
#     if not type(value)==standard:
#         print(f"The type of a {input} must be {standard} but is {type(value)}")
#         return False

# def minlength(value,standard,input):
#     if not len(value)>=standard:
#         print(f'The minimum length of a {input} must be {standard} but is {len(value)}')
#         return False

# def maxlength(value,standard,input):
#     if not len(value)<= standard:
#         print(f'The maximum length of a {input} must be {standard} but is {len(value)}')
#         return False

# def isGreaterthan(value,standard,input):
#     if not value>=standard:
#         print(f'The {input} must be greater than {standard} but is {value}')
#         return False

# def isLessthan(value,standard,input):
#     if not value<=standard:
#         print(f'The {input} must be less than {standard} but is {value}')
#         return False

# def nestedfunction(value,standard,input):
#     if(type(value)==list):
#         for item in value:
#             x = validator(item,standard)
#             if x==False:
#                 return False
#     elif(type(value)==dict):
#         x = validator(value,standard)
#         if x==False:
#             return False

# def validator(dictionary, validationrule):
#     if dictionary.keys()!=validationrule.keys():
#        print("The keys in dictionary and Validation dictionary are different!")
#        return False
#     else:
#         for key in validationrule:
#             value = dictionary[key]
#             rule = validationrule[key]
#             for function in rule.keys():
#                 if(function=='type' and type1(value,rule[function],key)==False):
#                     return False
#                 elif(function=='minlength' and minlength(value,rule[function],key)==False):
#                     return False
#                 elif(function=='maxlength' and maxlength(value,rule[function],key)==False):
#                     return False
#                 elif(function=='minimum' and isGreaterthan(value,rule[function],key)==False):
#                     return False
#                 elif(function=='max' and isLessthan(value,rule[function],key)==False):
#                     return False
#                 elif(function=='item_nesteddict' and nestedfunction(value,rule[function],key)==False):
#                     return False
#         return True
