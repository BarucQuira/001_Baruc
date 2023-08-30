
"""
Modus Tollens

Baruc Gutiérrez Quirarte - 7F1 
Sistemas Expertos
"""

# Premisas

ProsicionA = True #Si hubo fuego
ProsicionB = True #hay cenizas

Premisa1 = ProsicionA and ProsicionB # Si hubo fuego, hay cenizas
Premisa2 = not ProposicionB # No hay cenizas

#Modus Ponens

if Premisa2 == False:
    ProsicionA = False
    conclusion = "No hubo fuego"
    print(conclusion)
