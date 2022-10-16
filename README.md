# unit-testing-a-dictionary-validator
Learning about python's unit testing and implementing it in a dictionary validator function


The lists of function and their job we may have :

validator() --> takes two dictionary as argument, one an input, and another validation rule containing dictionary
   This function compares the keys of the both dictionary to each other's. If both dictionaries don't contain exact 
   1 to 1 key same keys then it return False
   
   we then compare the value of the keys of both dictionaries, validation rule dictionary will have value of validation rules which is inside a dictionary and input dictionary contains the value which is to measured with the value of validation rules
   This function will only return True if the validation rules are satisfied

type1()--> This function takes the value of input dict, value of validation rule dict 's key's value and key of input dict as   argument
    It checks the type of value of input dict with 2nd parameter and return False if they're not same

minlength(),maxlength(), minimum(), maximum()--> all take the same argument as type1() function and return False if certain conditions are met like for minlength(): if the length of the string is less than threshold length the funtion returns False

item_nesteddict()--> This function also takes the same argument as the type1() function except, it is used especially to validate nested values in input dictionary. For e.g.: If the input dictionary contains nested list then it processes a for loop on each items of that list which are dictionary, and then calls the validator() function sending that item dictionary and the value of validation rule dict 's key's value as the parameter and returns False based on that validator() function's result.