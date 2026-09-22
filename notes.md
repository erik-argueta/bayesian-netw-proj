# How to connect diagnose with diagnostics_gui.py

Where is `Diagnostics()` instantiated?  
    diagnostics_gui, Line 15  
    `disease, p_disease = bn.diagnose(asia_var.get(), smoking_var.get(), xray_var.get(), dyspnea_var.get()) diagnosis = f"{disease} with chance {p_disease*100:.2f}%"`  

Where does GUI gather the selected symptoms and call `diagnose`?  
    variables responsible: `asia_var`; `smoking_var`; `xray_var`; `dyspnea_var`  
    This matches the parameters to `diagnose(self, asia, smoking, xray, dyspnea)`  

What does `diagnose` return? How does the GUI utilize the return value. Ensure both sides agree on its structure.  
    diagnose: `return ["the disease", -1.0]`  a list to be modified by student  
    
    *Would there be multiple return statements depending on the outcome?*  
    *"the disease" could be replaced with a variable string?*  

    diagnostics_gui, `on_selection(): diagnosis = f"{disease} with chance {p_disease*100:.2f}%"`  

Note `enumeration_ask`:  
    probability variable: main variable?  
    evidence dict: probability parameters with T/F values  
    Bayes netw argument: name of network variable  
    How probabilities are retrieved from its result:   

How to translate GUI values into Bayes netw evidence; GUI's labels or values must match node names and Boolean representation used by `diagn_cancer`.  


HINT:  
A useful debugging technique is to temporarily print the arguments immediately before the GUI calls diagnose, then print the returned value immediately afterward. That will reveal whether the connection is working before you tackle the inference logic.