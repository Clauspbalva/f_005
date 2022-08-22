"""
f_005.py | Claus Pagano | Last update: 2022-8-19

Algorithms and Data Structures practice with Python

"""


# --------------------------------------------------------------------------------------------------
# Imports
# --------------------------------------------------------------------------------------------------

from f_000 import function_test

# --------------------------------------------------------------------------------------------------
# VARIABLE DECLARATION
# --------------------------------------------------------------------------------------------------

SCALES = ['CELSIUS', 'FAHRENHEIT', 'KELVIN']


# --------------------------------------------------------------------------------------------------
# FUNCTION DECLARATION 
# --------------------------------------------------------------------------------------------------

def convert_temperature(t_i, s_i, s_o):
    """Description: 
            Temperature converter 
            with three different scales 'Celsius', 'Fahrenheit' and 'Kelvin' 
            that changes an input temperature 
            and returns an output temperature or None if a problem arises.

        Parameters:
            t_i (float): temperature input
            s_i (str): scale input
            s_o (str): scale output
        
        Return:
            t_o (float): temperature output
    """

    # Validates parameters
    if type(t_i) != float:
        if type(t_i) == int:
            t_i = float(t_i)
        else:
            return None 
    elif s_i not in SCALES or s_o not in SCALES:
        return None 

    # Conversion computation
    # Celsius to fahrenheit
    if s_i == SCALES[0] and s_o == SCALES[1]:
        t_o = t_i * 1.8 + 32    
    # Celsius to kelvin
    elif s_i == SCALES[0] and s_o == SCALES[2]:
        t_o = t_i + 273.15      
    # Fahrenheit to celsius
    elif s_i == SCALES[1] and s_o == SCALES[0]:
        t_o = ((t_i - 32) * 5) / 9    
    # Fahrenheit to kelvin
    elif s_i == SCALES[1] and s_o == SCALES[2]:
        t_o = ((t_i - 32) / 1.8) + 273.15    
    # Kelvin to celsius
    elif s_i == SCALES[2] and s_o == SCALES[0]:
        t_o = t_i - 273.15   
    # Kelvin to fahrenheit
    elif s_i == SCALES[2] and s_o == SCALES[1]:
        t_o = 1.8 * (t_i - 273) + 32   
    # Convert the same scale
    elif s_i == s_o and s_i in SCALES:
        t_o = t_i
    else:
        return None
    return t_o


# --------------------------------------------------------------------------------------------------
# TESTING
# -------------------------------------------------------------------------------------------------- 

# Dictionary with test cases   
test_config = {
    'function': convert_temperature,
    'input_names': ['t_i', 's_i', 's_o'],
    'num_precision': [0.5],
    'tests': [
        {'id': 1, 'input_values': [None, None, None], 'output_expected': None},
        {'id': 2, 'input_values': [25, 'CELSIUS', 'FAHRENHEIT'], 'output_expected': 77.0},
        {'id': 3, 'input_values': [25, 'CELSIUS', 'FAHRENHEITT'], 'output_expected': None},
        {'id': 4, 'input_values': [25, 'CELSIUS', None], 'output_expected': None},
        {'id': 5, 'input_values': [-273, 'CELSIUS', 'KELVIN'], 'output_expected': 0.15}
    ],
    'print_details': True  
}


# --------------------------------------------------------------------------------------------------
# MAIN PROCEDURE
# --------------------------------------------------------------------------------------------------

if __name__ == "__main__":   
    function_test(test_config)