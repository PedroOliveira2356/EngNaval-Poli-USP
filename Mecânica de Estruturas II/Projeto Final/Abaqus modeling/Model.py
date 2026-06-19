# from part import *
# from material import *
# from section import *
# from assembly import *
# from step import *
# from interaction import *
# from load import *
# from mesh import *
# from optimization import *
# from job import *
# from sketch import *
# from visualization import *
# from connectorBehavior import *

import os
# import numpy as np
# import matplotlib.pyplot as plt
import csv

# Change work directory
Basedir = "C:\\repos\\EngNaval-Poli-USP\\Mecânica de Estruturas II\\Projeto Final\\Abaqus modeling"
# os.makedirs(os.path.join(Basedir, "results"), exist_ok=True)
# os.chdir(os.path.join(Basedir, "results"))

# Read inputs csv file
with open(os.path.join(Basedir, "inputs.csv"), 'r', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=',')
    linhas = list(reader)

# Dimensões principais
h1 = float(linhas[1][1])
h2 = float(linhas[2][1])
h3 = float(linhas[3][1])
larg = float(linhas[4][1])
raio_canto = float(linhas[5][1])
comp_sm = float(linhas[6][1])
dist_cavernas = float(linhas[7][1])

# Longarinas
long_fundo = [float(linhas[9][1]), float(linhas[9][2])]
long_costado = [float(linhas[10][1]), float(linhas[10][2])]
long_teto = [float(linhas[11][1]), float(linhas[11][2])]

# Propriedades do material
young_mod_st = float(linhas[1][5])
poiss = float(linhas[2][5])
density_st = float(linhas[3][5])

# Parametros do mesh
mesh_size = 0.1

# utils
orig = 0.0
octlarg = larg/8
ht = h1+h2+h3
hi = h1+h2


# Create new model
Mdb()
MyModel = mdb.models['Model-1']


def conves():
    # Create new part: conves
    MyModel.ConstrainedSketch(name='__profile__', sheetSize=20.0)

    # Fundo
    MyModel.sketches['__profile__'].Line(point1=(orig, orig), point2=(orig, h1))
    MyModel.sketches['__profile__'].Line(point1=(orig, h1), point2=(-larg, h1))
    MyModel.sketches['__profile__'].Line(point1=(orig, orig), point2=(-(larg-raio_canto), orig))
    MyModel.sketches['__profile__'].Line(point1=(-larg, h1), point2=(-larg, raio_canto))
    MyModel.sketches['__profile__'].Line(point1=(-octlarg*7, orig), point2=(-octlarg*7, h1))
    MyModel.sketches['__profile__'].Line(point1=(-octlarg*4, orig), point2=(-octlarg*4, h1))
    MyModel.sketches['__profile__'].ArcByCenterEnds(center=(-(larg-raio_canto), raio_canto),
        direction=COUNTERCLOCKWISE, point1=(-larg, raio_canto), point2=(-(larg-raio_canto), orig))
    # Reforçadores do fundo
    MyModel.sketches['__profile__'].Line(point1=(-octlarg, h1), point2=(-octlarg, h1-long_fundo[0]))
    MyModel.sketches['__profile__'].Line(point1=(-octlarg, h1-long_fundo[0]), point2=(-(octlarg-long_fundo[1]), h1-long_fundo[0]))
    MyModel.sketches['__profile__'].Line(point1=(-octlarg, orig), point2=(-octlarg, long_fundo[0]))
    MyModel.sketches['__profile__'].Line(point1=(-octlarg, long_fundo[0]), point2=(-(octlarg-long_fundo[1]), long_fundo[0]))
    MyModel.sketches['__profile__'].Line(point1=(-octlarg*2, h1), point2=(-octlarg*2, h1-long_fundo[0]))
    MyModel.sketches['__profile__'].Line(point1=(-octlarg*2, h1-long_fundo[0]), point2=(-(octlarg*2-long_fundo[1]), h1-long_fundo[0]))
    MyModel.sketches['__profile__'].Line(point1=(-octlarg*2, orig), point2=(-octlarg*2, long_fundo[0]))
    MyModel.sketches['__profile__'].Line(point1=(-octlarg*2, long_fundo[0]), point2=(-(octlarg*2-long_fundo[1]), long_fundo[0]))
    MyModel.sketches['__profile__'].Line(point1=(-octlarg*3, h1), point2=(-octlarg*3, h1-long_fundo[0]))
    MyModel.sketches['__profile__'].Line(point1=(-octlarg*3, h1-long_fundo[0]), point2=(-(octlarg*3-long_fundo[1]), h1-long_fundo[0]))
    MyModel.sketches['__profile__'].Line(point1=(-octlarg*3, orig), point2=(-octlarg*3, long_fundo[0]))
    MyModel.sketches['__profile__'].Line(point1=(-octlarg*3, long_fundo[0]), point2=(-(octlarg*3-long_fundo[1]), long_fundo[0]))
    MyModel.sketches['__profile__'].Line(point1=(-octlarg*5, h1), point2=(-octlarg*5, h1-long_fundo[0]))
    MyModel.sketches['__profile__'].Line(point1=(-octlarg*5, h1-long_fundo[0]), point2=(-(octlarg*5-long_fundo[1]), h1-long_fundo[0]))
    MyModel.sketches['__profile__'].Line(point1=(-octlarg*5, orig), point2=(-octlarg*5, long_fundo[0]))
    MyModel.sketches['__profile__'].Line(point1=(-octlarg*5, long_fundo[0]), point2=(-(octlarg*5-long_fundo[1]), long_fundo[0]))
    MyModel.sketches['__profile__'].Line(point1=(-octlarg*6, h1), point2=(-octlarg*6, h1-long_fundo[0]))
    MyModel.sketches['__profile__'].Line(point1=(-octlarg*6, h1-long_fundo[0]), point2=(-(octlarg*6-long_fundo[1]), h1-long_fundo[0]))
    MyModel.sketches['__profile__'].Line(point1=(-octlarg*6, orig), point2=(-octlarg*6, long_fundo[0]))
    MyModel.sketches['__profile__'].Line(point1=(-octlarg*6, long_fundo[0]), point2=(-(octlarg*6-long_fundo[1]), long_fundo[0]))

    # Costado
    MyModel.sketches['__profile__'].Line(point1=(-larg, h1), point2=(-larg, ht))
    # Reforçadores do costado
    MyModel.sketches['__profile__'].Line(point1=(-larg, h1+h2*1/4), point2=(-(larg-long_costado[0]), h1+h2*1/4))
    MyModel.sketches['__profile__'].Line(point1=(-(larg-long_costado[0]), h1+h2*1/4), point2=(-(larg-long_costado[0]), h1+h2*1/4-long_costado[1]))
    MyModel.sketches['__profile__'].Line(point1=(-larg, h1+h2*2/4), point2=(-(larg-long_costado[0]), h1+h2*2/4))
    MyModel.sketches['__profile__'].Line(point1=(-(larg-long_costado[0]), h1+h2*2/4), point2=(-(larg-long_costado[0]), h1+h2*2/4-long_costado[1]))
    MyModel.sketches['__profile__'].Line(point1=(-larg, h1+h2*3/4), point2=(-(larg-long_costado[0]), h1+h2*3/4))
    MyModel.sketches['__profile__'].Line(point1=(-(larg-long_costado[0]), h1+h2*3/4), point2=(-(larg-long_costado[0]), h1+h2*3/4-long_costado[1]))

    MyModel.sketches['__profile__'].Line(point1=(-larg, hi+h3*1/3), point2=(-(larg-long_costado[0]), hi+h3*1/3))
    MyModel.sketches['__profile__'].Line(point1=(-(larg-long_costado[0]), hi+h3*1/3), point2=(-(larg-long_costado[0]), hi+h3*1/3-long_costado[1]))
    MyModel.sketches['__profile__'].Line(point1=(-larg, hi+h3*2/3), point2=(-(larg-long_costado[0]), hi+h3*2/3))
    MyModel.sketches['__profile__'].Line(point1=(-(larg-long_costado[0]), hi+h3*2/3), point2=(-(larg-long_costado[0]), hi+h3*2/3-long_costado[1]))

    # Teto
    MyModel.sketches['__profile__'].Line(point1=(-larg, ht), point2=(-octlarg*4, ht))
    MyModel.sketches['__profile__'].Line(point1=(-octlarg*4, ht), point2=(-octlarg*4, ht-0.5))
    MyModel.sketches['__profile__'].Line(point1=(-octlarg*4, ht-0.5), point2=(-(octlarg*4+0.4), ht-0.5))       # TODO: parametros dos cantos
    # Reforçadores do teto
    MyModel.sketches['__profile__'].Line(point1=(-octlarg*7, ht), point2=(-octlarg*7, ht-long_teto[0]))
    MyModel.sketches['__profile__'].Line(point1=(-octlarg*7, ht-long_teto[0]), point2=(-(octlarg*7-long_teto[1]), ht-long_teto[0]))
    MyModel.sketches['__profile__'].Line(point1=(-octlarg*6, ht), point2=(-octlarg*6, ht-long_teto[0]))
    MyModel.sketches['__profile__'].Line(point1=(-octlarg*6, ht-long_teto[0]), point2=(-(octlarg*6-long_teto[1]), ht-long_teto[0]))
    MyModel.sketches['__profile__'].Line(point1=(-octlarg*5, ht), point2=(-octlarg*5, ht-long_teto[0]))
    MyModel.sketches['__profile__'].Line(point1=(-octlarg*5, ht-long_teto[0]), point2=(-(octlarg*5-long_teto[1]), ht-long_teto[0]))

    # Secao intermediaria
    MyModel.sketches['__profile__'].Line(point1=(-larg, hi), point2=(-octlarg*4, hi))
    MyModel.sketches['__profile__'].Line(point1=(-octlarg*4, hi), point2=(-octlarg*4, hi-0.5))
    MyModel.sketches['__profile__'].Line(point1=(-octlarg*4, hi-0.5), point2=(-(octlarg*4+0.4), hi-0.5))       # TODO: parametros dos cantos
    # Reforçadores intermediarios
    MyModel.sketches['__profile__'].Line(point1=(-octlarg*7, hi), point2=(-octlarg*7, hi-long_teto[0]))     # diminuir 3.5 do y
    MyModel.sketches['__profile__'].Line(point1=(-octlarg*7, hi-long_teto[0]), point2=(-(octlarg*7-long_teto[1]), hi-long_teto[0]))
    MyModel.sketches['__profile__'].Line(point1=(-octlarg*6, hi), point2=(-octlarg*6, hi-long_teto[0]))
    MyModel.sketches['__profile__'].Line(point1=(-octlarg*6, hi-long_teto[0]), point2=(-(octlarg*6-long_teto[1]), hi-long_teto[0]))
    MyModel.sketches['__profile__'].Line(point1=(-octlarg*5, hi), point2=(-octlarg*5, hi-long_teto[0]))
    MyModel.sketches['__profile__'].Line(point1=(-octlarg*5, hi-long_teto[0]), point2=(-(octlarg*5-long_teto[1]), hi-long_teto[0]))

    MyModel.Part(dimensionality=THREE_D, name='conves', type=DEFORMABLE_BODY)
    MyModel.parts['conves'].BaseShellExtrude(depth=comp_sm, sketch=
        MyModel.sketches['__profile__'])
    del MyModel.sketches['__profile__']


def teto():
    # Create new part: teto
    MyModel.ConstrainedSketch(name='__profile__', sheetSize=20.0)

    MyModel.ConstrainedSketch(name='__profile__', sheetSize=20.0)
    MyModel.sketches['__profile__'].Line(point1=(orig, orig), point2=(-larg/2, orig))
    MyModel.sketches['__profile__'].Line(point1=(orig, orig), point2=(orig, -long_fundo[0]))                # FLAG
    MyModel.sketches['__profile__'].Line(point1=(-octlarg, orig), point2=(-octlarg, -long_fundo[0]))
    MyModel.sketches['__profile__'].Line(point1=(-octlarg*2, orig), point2=(-octlarg*2, -long_fundo[0]))
    MyModel.sketches['__profile__'].Line(point1=(-octlarg*3, orig), point2=(-octlarg*3, -long_fundo[0]))

    MyModel.Part(dimensionality=THREE_D, name='teto', type=DEFORMABLE_BODY)
    MyModel.parts['teto'].BaseShellExtrude(depth=dist_cavernas, sketch=
        MyModel.sketches['__profile__'])
    del MyModel.sketches['__profile__']


def caverna():
    # Create new part: caverna
    MyModel.ConstrainedSketch(name='__profile__', sheetSize=20.0)
    # Desenho continuo
    MyModel.sketches['__profile__'].Line(point1=(orig, orig), point2=(-(larg-raio_canto), orig))
    MyModel.sketches['__profile__'].Line(point1=(orig, orig), point2=(orig, h1))
    MyModel.sketches['__profile__'].Line(point1=(orig, h1), point2=(-(larg-long_costado[0]), h1))
    MyModel.sketches['__profile__'].Line(point1=(-(larg-long_costado[0]), h1), point2=(-(larg-long_costado[0]), ht-long_costado[0]))
    MyModel.sketches['__profile__'].Line(point1=(-(larg-long_costado[0]), ht-long_costado[0]), point2=(-octlarg*4, ht-long_costado[0]))
    MyModel.sketches['__profile__'].Line(point1=(-octlarg*4, ht-long_costado[0]), point2=(-octlarg*4, ht))
    MyModel.sketches['__profile__'].Line(point1=(-octlarg*4, ht), point2=(-larg, ht))
    MyModel.sketches['__profile__'].Line(point1=(-larg, ht), point2=(-larg, raio_canto))
    MyModel.sketches['__profile__'].ArcByCenterEnds(center=(-(larg-raio_canto), raio_canto),
        direction=COUNTERCLOCKWISE, point1=(-larg, raio_canto), point2=(-(larg-raio_canto), orig))
    # Elipses
    MyModel.sketches['__profile__'].EllipseByCenterPerimeter(
        axisPoint1=(-octlarg*1/2, h1*0.85), axisPoint2=(-octlarg*1/4, h1/2), center=(-octlarg*1/2, h1/2))
    MyModel.sketches['__profile__'].EllipseByCenterPerimeter(
        axisPoint1=(-octlarg*3/2, h1*0.85), axisPoint2=(-octlarg*5/4, h1/2), center=(-octlarg*3/2, h1/2))
    MyModel.sketches['__profile__'].EllipseByCenterPerimeter(
        axisPoint1=(-octlarg*5/2, h1*0.85), axisPoint2=(-octlarg*9/4, h1/2), center=(-octlarg*5/2, h1/2))
    MyModel.sketches['__profile__'].EllipseByCenterPerimeter(
        axisPoint1=(-octlarg*9/2, h1*0.85), axisPoint2=(-octlarg*17/4, h1/2), center=(-octlarg*9/2, h1/2))
    MyModel.sketches['__profile__'].EllipseByCenterPerimeter(
        axisPoint1=(-octlarg*11/2, h1*0.85), axisPoint2=(-octlarg*21/4, h1/2), center=(-octlarg*11/2, h1/2))
    MyModel.sketches['__profile__'].EllipseByCenterPerimeter(
        axisPoint1=(-octlarg*13/2, h1*0.85), axisPoint2=(-octlarg*25/4, h1/2), center=(-octlarg*13/2, h1/2))

    MyModel.Part(dimensionality=THREE_D, name='caverna', type=DEFORMABLE_BODY)
    MyModel.parts['caverna'].BaseShell(sketch=
        MyModel.sketches['__profile__'])
    del MyModel.sketches['__profile__']


def caverna_teto():
    # Create new part: cavernas-teto
    MyModel.ConstrainedSketch(name='__profile__', sheetSize=20.0)
    # Desenho continuo
    MyModel.sketches['__profile__'].Line(point1=(orig, orig), point2=(orig, -long_costado[0]))               # FLAG
    MyModel.sketches['__profile__'].Line(point1=(orig, -long_costado[0]), point2=(-larg/2, -long_costado[0]))
    MyModel.sketches['__profile__'].Line(point1=(-larg/2, -long_costado[0]), point2=(-larg/2, orig))
    MyModel.sketches['__profile__'].Line(point1=(-larg/2, orig), point2=(orig, orig))

    MyModel.Part(dimensionality=THREE_D, name='caverna-teto', type=DEFORMABLE_BODY)
    MyModel.parts['caverna-teto'].BaseShell(sketch=
        MyModel.sketches['__profile__'])
    del MyModel.sketches['__profile__']


def material():
    # This creates the material
    MyModel.Material(name='Steel')
    MyModel.materials['Steel'].Elastic(table=((young_mod_st, poiss), ))
    MyModel.materials['Steel'].Density(table=((density_st, ), ))


def section():
    pass


def assembly():
    MyModel.rootAssembly.DatumCsysByDefault(CARTESIAN)

    MyModel.rootAssembly.Instance(dependent=OFF,
        name='Conves-1', part=MyModel.parts['conves'])

    MyModel.rootAssembly.Instance(dependent=OFF,
        name='Caverna-1', part=MyModel.parts['caverna'])
    MyModel.rootAssembly.instances['Caverna-1'].translate(
        vector=(0.0, 0.0, dist_cavernas))
    MyModel.rootAssembly.LinearInstancePattern(
        direction1=(1.0, 0.0, 0.0), direction2=(0.0, 0.0, 1.0), instanceList=('Caverna-1', ),
        number1=1, number2=int(comp_sm//dist_cavernas-1), spacing1=8.0, spacing2=dist_cavernas)

    MyModel.rootAssembly.Instance(dependent=OFF,
        name='Teto-1', part=MyModel.parts['teto'])
    MyModel.rootAssembly.instances['Teto-1'].translate(
        vector=(0.0, ht, 0.0))
    MyModel.rootAssembly.LinearInstancePattern(
        direction1=(1.0, 0.0, 0.0), direction2=(0.0, 0.0, 1.0), instanceList=('Teto-1', ),
        number1=1, number2=2, spacing1=8.0, spacing2=dist_cavernas)
    MyModel.rootAssembly.Instance(dependent=OFF,
        name='Teto-2', part=MyModel.parts['teto'])
    MyModel.rootAssembly.instances['Teto-2'].translate(
        vector=(0.0, ht, 5*dist_cavernas))
    MyModel.rootAssembly.LinearInstancePattern(
        direction1=(1.0, 0.0, 0.0), direction2=(0.0, 0.0, 1.0), instanceList=('Teto-2', ),
        number1=1, number2=2, spacing1=8.0, spacing2=dist_cavernas)
    MyModel.rootAssembly.Instance(dependent=OFF,
        name='Teto-3', part=MyModel.parts['teto'])
    MyModel.rootAssembly.instances['Teto-3'].translate(
        vector=(0.0, ht, 10*dist_cavernas))
    MyModel.rootAssembly.LinearInstancePattern(
        direction1=(1.0, 0.0, 0.0), direction2=(0.0, 0.0, 1.0), instanceList=('Teto-3', ),
        number1=1, number2=2, spacing1=8.0, spacing2=dist_cavernas)

    MyModel.rootAssembly.Instance(dependent=OFF,
        name='Caverna-teto-1', part=MyModel.parts['caverna-teto'])
    MyModel.rootAssembly.instances['Caverna-teto-1'].translate(
        vector=(0.0, ht, 2*dist_cavernas))
    MyModel.rootAssembly.LinearInstancePattern(
        direction1=(1.0, 0.0, 0.0), direction2=(0.0, 0.0, 1.0), instanceList=('Caverna-teto-1', ),
        number1=1, number2=2, spacing1=8.0, spacing2=3*dist_cavernas)
    MyModel.rootAssembly.Instance(dependent=OFF,
        name='Caverna-teto-2', part=MyModel.parts['caverna-teto'])
    MyModel.rootAssembly.instances['Caverna-teto-2'].translate(
        vector=(0.0, ht, 7*dist_cavernas))
    MyModel.rootAssembly.LinearInstancePattern(
        direction1=(1.0, 0.0, 0.0), direction2=(0.0, 0.0, 1.0), instanceList=('Caverna-teto-2', ),
        number1=1, number2=2, spacing1=8.0, spacing2=3*dist_cavernas)

    MyModel.rootAssembly.InstanceFromBooleanMerge(domain=GEOMETRY,
        instances=(MyModel.rootAssembly.instances['Conves-1'],
        MyModel.rootAssembly.instances['Caverna-1'],
        MyModel.rootAssembly.instances['Caverna-1-lin-1-2'],
        MyModel.rootAssembly.instances['Caverna-1-lin-1-3'],
        MyModel.rootAssembly.instances['Caverna-1-lin-1-4'],
        MyModel.rootAssembly.instances['Caverna-1-lin-1-5'],
        MyModel.rootAssembly.instances['Caverna-1-lin-1-6'],
        MyModel.rootAssembly.instances['Caverna-1-lin-1-7'],
        MyModel.rootAssembly.instances['Caverna-1-lin-1-8'],
        MyModel.rootAssembly.instances['Caverna-1-lin-1-9'],
        MyModel.rootAssembly.instances['Caverna-1-lin-1-10'],
        MyModel.rootAssembly.instances['Caverna-1-lin-1-11'],
        MyModel.rootAssembly.instances['Teto-1'],
        MyModel.rootAssembly.instances['Teto-1-lin-1-2'],
        MyModel.rootAssembly.instances['Teto-2'],
        MyModel.rootAssembly.instances['Teto-2-lin-1-2'],
        MyModel.rootAssembly.instances['Teto-3'],
        MyModel.rootAssembly.instances['Teto-3-lin-1-2'],
        MyModel.rootAssembly.instances['Caverna-teto-1'],
        MyModel.rootAssembly.instances['Caverna-teto-1-lin-1-2'],
        MyModel.rootAssembly.instances['Caverna-teto-2'],
        MyModel.rootAssembly.instances['Caverna-teto-2-lin-1-2']),
        name='Merged', originalInstances=SUPPRESS)


def step():
    MyModel.StaticStep(initialInc=0.01, maxInc=0.01, name='Step-1',
        nlgeom=ON, previous='Initial')


def loads():
    pass


def mesh():
    MyModel.parts['Merged'].seedPart(deviationFactor=0.1,
        minSizeFactor=0.1, size=mesh_size)
    MyModel.parts['Merged'].generateMesh()


def job():
    mdb.Job(atTime=None, contactPrint=OFF, description='', echoPrint=OFF,
        explicitPrecision=SINGLE, getMemoryFromAnalysis=True, historyPrint=OFF,
        memory=90, memoryUnits=PERCENTAGE, model='Model-1', modelPrint=OFF,
        multiprocessingMode=DEFAULT, name='Job-1', nodalOutputPrecision=SINGLE,
        numCpus=1, numGPUs=0, queue=None, resultsFormat=ODB, scratch='', type=
        ANALYSIS, userSubroutine='', waitHours=0, waitMinutes=0)

    mdb.jobs['Job-1'].submit(consistencyChecking=OFF)
    mdb.jobs['Job-1'].waitForCompletion()


conves()
teto()
caverna()
caverna_teto()
material()
# section()
assembly()
step()
# loads()
mesh()
# job()
