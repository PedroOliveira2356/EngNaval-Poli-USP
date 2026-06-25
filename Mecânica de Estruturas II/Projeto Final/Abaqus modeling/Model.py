from part import *
from material import *
from section import *
from assembly import *
from step import *
from interaction import *
from load import *
from mesh import *
from optimization import *
from job import *
from sketch import *
from visualization import *
from connectorBehavior import *
from abaqus import *
from odbAccess import *

import os
# import numpy as np
# import matplotlib.pyplot as plt
import csv

# Change work directory
Basedir = r"C:\repos\EngNaval-Poli-USP\Mecânica de Estruturas II\Projeto Final\Abaqus modeling"
# os.makedirs(os.path.join(Basedir, "results"), exist_ok=True)
# os.chdir(os.path.join(Basedir, "results"))

# Read inputs csv file
with open(os.path.join(Basedir, "inputs.csv"), 'r', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=',')
    linhas = list(reader)


# Condicoes ambientais
g = 9.81
rho_mar = 1025.0

# Dimensões principais
h1 = float(linhas[1][1])
h2 = float(linhas[2][1])
h3 = float(linhas[3][1])
larg = float(linhas[4][1])
raio_canto = float(linhas[5][1])
comp_sm = float(linhas[6][1])
dist_cavernas = float(linhas[7][1])
calado = 7.5

# Longarinas
long_fundo = [float(linhas[9][1]), float(linhas[9][2])]
long_costado = [float(linhas[10][1]), float(linhas[10][2])]
long_teto = [float(linhas[11][1]), float(linhas[11][2])]
espessuras = [float(linhas[12][1]), float(linhas[12][2]), float(linhas[12][3]), float(linhas[12][4])]

# Propriedades do material (steel)
young_mod_st = float(linhas[1][5])
poiss = float(linhas[2][5])
density_st = float(linhas[3][5])

# Parametros do mesh
mesh_size = 0.1
