'''
ENV_LIB

This is the environment library, containing
different dm_acme environments for testing and
RL algorithms.

Started 4/13/2021
'''
import dm_env
import numpy as np
import pandas as pd

class Yahtzee(dm_env.Environment):
    def __init__(self):
        return True