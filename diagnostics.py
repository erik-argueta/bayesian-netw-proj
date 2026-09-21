from aima.probability import *

T, F = True, False

class Diagnostics:
    """ Use a Bayesian network to diagnose between three lung diseases """

    diagn_cancer = BayesNet([

        ('Asia', '', 0.01),                                             # P(+Asia) = 0.01
        ('Smoking', '', 0.5),                                           # P(+Smoking) = 0.5
                   
        ('TB', 'Asia', { (T): 0.05, (F): 0.01 }),                       # Var: TB; Parent: Asia; P(+TB | Asia) 
        ('LCancer', 'Smoking', {(T): 0.1, (F): 0.01}),                  # Var: LCancer; Parent: Smoking; P(+LCancer | Smoking)
        ('Bronchitis', 'Smoking', {(T): 0.6, (F): 0.3}),                # Var: Bronchitis; Parent: Smoking; P(+Bronchitis | Smoking)
                    
        ('TBorCancer', 'TB LCancer',                                    # Var: TBorCancer; Parents: TB & LCancer; P(+TBorCancer | TB, LCancer)
            {
                (T, T): 1.0,                                            # P(+TBorCancer | TB=True,  LCancer= True)
                (T, F): 1.0,                                            # P(+TBorCancer | TB=True,  LCancer= False)
                (F, T): 1.0,                                            # P(+TBorCancer | TB=False, LCancer= True)
                (F, F): 0                                               # P(+TBorCancer | TB=False, LCancer= False)
            }), 

            ('Dyspnea', 'TBorCancer Bronchitis', 
            {
            (T, T): 0.9,
            (T, F): 0.7,
            (F, T): 0.8,
            (F, F): 0.1
            }),
            
            ('xray', 'TBorCancer', {(T): 0.99, (F): 0.05})

    ])

    def __init__(self):
        # placeholder for the student's code, to be replaced by the student
        ...
        

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
