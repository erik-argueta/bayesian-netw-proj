from aima.probability import *

T, F = True, False

class Diagnostics:
    """ Use a Bayesian network to diagnose between three lung diseases """

    def __init__(self):
        ... # placeholder for the student's code, to be replaced by the student

    def diagnose (self, asia, smoking, xray, dyspnea):
        '''
        Hints: 
            - Class should make use of either 'BayesNet' or 'DiscreteBayesNet'
                - DiscreteBayesNet handles multiple variables that can be named anything
            - Use the 'enumeration inference' algo to calculate the probability of each disease 
                - This algo is implemented as 'enumeration_ask_function' in textbook
        '''
        # To be implemented by the student
        return ["the disease", -1.0] # placeholder return value, to be replaced by the student
