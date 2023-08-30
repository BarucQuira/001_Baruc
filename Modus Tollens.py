
"""
Modus Tollens

Baruc Gutiérrez Quirarte - 7F1 
Sistemas Expertos
"""

# Premisas

ProposicionA = True #Si hubo fuego
ProposicionB = True #hay cenizas

Premisa1 = ProposicionA and ProposicionB # Si hubo fuego, hay cenizas
Premisa2 = not ProposicionB # No hay cenizas

#Modus Ponens

if Premisa2 == False:
    ProposicionA = False
    conclusion = "No hubo fuego"
    print(conclusion)
