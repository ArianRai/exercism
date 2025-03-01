"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#TODO: define the 'EXPECTED_BAKE_TIME' constant below.
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

#TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time in minutes.

    :param number_of_layers: int - number of layers of the lasagna.
    :return: int - the total number of minutes of preparation'.

    Function that takes the number of layers of the lasagna and returns the total
     of preparation needed based on the `PREPARATION_TIME` that each layer takes.
    """
    return number_of_layers * PREPARATION_TIME

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed time.

    :param number_of_layers: int - number of layers of the lasagna.
    :param elapsed_bake_time: int - time that the lasagna has been in the oven.
    :return: int - the total number of minutes of preparation + baking'.

    Function that takes the number of layers of the lasagna and the time the
     lasagna have been in the oven and returns the total time of preparation.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time 
