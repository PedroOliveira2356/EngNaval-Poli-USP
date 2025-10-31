# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 15:13:26 2020

@author: andre
"""

import gurobipy as gp
from gurobipy import GRB

try:

    # Create a new model
    m = gp.Model("Transporte")

    # Create variables
    x11 = m.addVar(vtype=GRB.CONTINUOUS, name="x11")
    x12 = m.addVar(vtype=GRB.CONTINUOUS, name="x12")
    x13 = m.addVar(vtype=GRB.CONTINUOUS, name="x13")
    x21 = m.addVar(vtype=GRB.CONTINUOUS, name="x21")
    x22 = m.addVar(vtype=GRB.CONTINUOUS, name="x22")
    x23 = m.addVar(vtype=GRB.CONTINUOUS, name="x23")

    # Set objective
    m.setObjective(9 * x11 + 8 * x12 + 6 * x13 + 4 * x21 + 5 * x22 + 7 * x23, GRB.MINIMIZE)

    # Adiciona restrições de oferta
    m.addConstr(x11 + x12 + x13 == 40, "r1")
    m.addConstr(x21 + x22 + x23 == 70, "r2")

    # Adiciona restrições de demanda
    m.addConstr(x11 + x21 == 50, "r3")
    m.addConstr(x12 + x22 == 40, "r4")
    m.addConstr(x13 + x23 == 20, "r5")

    # Optimize model
    m.optimize()
    m.write("ModeloTransportes.lp")
    m.write("ModeloTransportes.sol")
    
    print(x11.varName, x11.x)
    print(x12.varName, x12.x)
    print(x13.varName, x13.x)
    print(x21.varName, x21.x)
    print(x22.varName, x22.x)
    print(x23.varName, x23.x)
    print('Funcao Objetivo: %g' % m.objVal)


except gp.GurobiError as e:
    print('Error code ' + str(e.errno) + ': ' + str(e))

except AttributeError:
    print('Encountered an attribute error')
