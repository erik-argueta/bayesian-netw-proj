"""
Title: Programming Project 1 (Bayesian Networks)
Authors: Erik Argueta, Jerico Avila, Jose Cervantes
"""

from aima.probability import *

T, F = True, False

class Diagnostics:
    """ Use a Bayesian network to diagnose between three lung diseases """

    def __init__(self):
        '''
        Placing diagn_cancer within init so it can be shared with every instance of Diagnostics.  
        '''
        self.diagn_cancer = BayesNet([
        
                ('Asia', '', 0.01),                                             # P(+Asia) = 0.01
                ('Smoking', '', 0.5),                                           # P(+Smoking) = 0.5
                           
                ('TB', 'Asia', { (T): 0.05, (F): 0.01 }),                       # Var: TB; Parent: Asia; P(+TB | Asia) 
                ('Cancer', 'Smoking', {(T): 0.1, (F): 0.01}),                   # Var: Cancer; Parent: Smoking; P(+Cancer | Smoking)
                ('Bronchitis', 'Smoking', {(T): 0.6, (F): 0.3}),                # Var: Bronchitis; Parent: Smoking; P(+Bronchitis | Smoking)
                            
                ('TBorCancer', 'TB Cancer',                                     # Var: TBorCancer; Parents: TB & Cancer; P(+TBorCancer | TB, Cancer)
                    {
                        (T, T): 1.0,                                            # P(+TBorCancer | TB=True,  Cancer= True)
                        (T, F): 1.0,                                            # P(+TBorCancer | TB=True,  Cancer= False)
                        (F, T): 1.0,                                            # P(+TBorCancer | TB=False, Cancer= True)
                        (F, F): 0                                               # P(+TBorCancer | TB=False, Cancer= False)
                    }), 
        
                    ('Dyspnea', 'TBorCancer Bronchitis', 
                    {
                        (T, T): 0.9,                                            # P(+Dyspnea | TBorCancer = True, Bronchitis = True)
                        (T, F): 0.7,                                            # P(+Dyspnea | TBorCancer = True, Bronchitis = False)
                        (F, T): 0.8,                                            # P(+Dyspnea | TBorCancer = False, Bronchitis = True)
                        (F, F): 0.1                                             # P(+Dyspnea | TBorCancer = False, Bronchitis = False)
                    }),
                    
                    ('xray', 'TBorCancer', {(T): 0.99, (F): 0.05})              # Var: xray; Parent: TBorCancer; P(+xray | TBorCancer)
            ])
        

    def diagnose (self, asia, smoking, xray, dyspnea):
        # ===============================================================================
        # Conversions to T/F values based on the fields in diangostics_gui
        # ===============================================================================
        conversion = {
            "Abnormal" : T,
            "Normal" : F,
            "Present": T,
            "Absent": F,
            "Yes" : T,
            "No" : F
        }


        """
        ===============================================================================
        Creating a dictionary, evidence, based on the conversions; omitting "NA"
            { "Asia" : T/F
            "Smoking" : T/F
            "Xray" : T/F
            "Dyspnea": T/F }
        ===============================================================================
        """
        evidence = {}
        if asia != "NA":
            evidence["Asia"]  = conversion[asia]
        if smoking != "NA":
            evidence["Smoking"] = conversion[smoking]
        if xray != "NA":
            evidence["Xray"] = conversion[xray]
        if dyspnea != "NA":
            evidence["Dyspnea"] = conversion[dyspnea]


        """
        ===============================================================================
        * diagnose is called at line 15 withing diagnostics_gui.py
        * enumeration_asks(variable, evidence dictionary, bayes_network)
        * [T] extracts the truth probability
        * returns string and probability from dictionary
        ===============================================================================
        """
        cancer_prob = enumeration_ask('Cancer', evidence, self.diagn_cancer)[T]
        tb_prob = enumeration_ask('TB', evidence, self.diagn_cancer)[T]
        bronc_prob = enumeration_ask('Bronchitis', evidence, self.diagn_cancer)[T]

        results = { "Cancer" : cancer_prob, "TB" : tb_prob, "Bronchitis" : bronc_prob}
        most_likely = max(results, key=results.get)

        return [most_likely, results[most_likely]]
