import os
import matplotlib.pyplot as plt
import numpy as np


# Change work directory
os.chdir(r"C:\repos\EngNaval-Poli-USP\Mecânica de Estruturas II\Projeto Final")


# Parameters




# This creates the material
mdb.models['Model-1'].Material(name='Steel')
mdb.models['Model-1'].materials['Steel'].Elastic(table=((206000000000.0, 0.3), ))
mdb.models['Model-1'].materials['Steel'].Density(table=(7800.0, ))

# This creates the 3 sections with different thicknesses 
mdb.models['Model-1'].HomogeneousShellSection(idealization=NO_IDEALIZATION, 
    integrationRule=SIMPSON, material='Steel', name='Section-1', 
    nodalThicknessField='', numIntPts=5, poissonDefinition=DEFAULT, 
    preIntegrate=OFF, temperature=GRADIENT, thickness=top_flange_thickness, thicknessField='', 
    thicknessModulus=None, thicknessType=UNIFORM, useDensity=OFF)
mdb.models['Model-1'].HomogeneousShellSection(idealization=NO_IDEALIZATION, 
    integrationRule=SIMPSON, material='Steel', name='Section-2', 
    nodalThicknessField='', numIntPts=5, poissonDefinition=DEFAULT, 
    preIntegrate=OFF, temperature=GRADIENT, thickness=web_thickness, thicknessField='', 
    thicknessModulus=None, thicknessType=UNIFORM, useDensity=OFF)
mdb.models['Model-1'].HomogeneousShellSection(idealization=NO_IDEALIZATION, 
    integrationRule=SIMPSON, material='Steel', name='Section-3', 
    nodalThicknessField='', numIntPts=5, poissonDefinition=DEFAULT, 
    preIntegrate=OFF, temperature=GRADIENT, thickness=bot_flange_thickness, thicknessField='', 
    thicknessModulus=None, thicknessType=UNIFORM, useDensity=OFF)
mdb.models['Model-1'].HomogeneousShellSection(idealization=NO_IDEALIZATION, 
    integrationRule=SIMPSON, material='Steel', name='Section-4', 
    nodalThicknessField='', numIntPts=5, poissonDefinition=DEFAULT, 
    preIntegrate=OFF, temperature=GRADIENT, thickness=stiffner_thickness, thicknessField='', 
    thicknessModulus=None, thicknessType=UNIFORM, useDensity=OFF)


# This starts the assemble
mdb.models['Model-1'].rootAssembly.DatumCsysByDefault(CARTESIAN)
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Part-1-1', 
    part=mdb.models['Model-1'].parts['Part-1'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Part-2-1', 
    part=mdb.models['Model-1'].parts['Part-2'])
# This merges the two parts into one
mdb.models['Model-1'].rootAssembly.InstanceFromBooleanMerge(domain=GEOMETRY, 
    instances=(mdb.models['Model-1'].rootAssembly.instances['Part-1-1'], 
    mdb.models['Model-1'].rootAssembly.instances['Part-2-1']), name='Part-3', 
    originalInstances=SUPPRESS)

# This creates the step
mdb.models['Model-1'].StaticStep(initialInc=0.01, maxInc=0.01, name='Step-1', 
    nlgeom=ON, previous='Initial')

# This meshes the assembly
mdb.models['Model-1'].parts['Part-3'].seedPart(deviationFactor=0.1, 
    minSizeFactor=0.1, size=mesh_size)
mdb.models['Model-1'].parts['Part-3'].generateMesh()



# This creates the job!
mdb.Job(atTime=None, contactPrint=OFF, description='', echoPrint=OFF, 
    explicitPrecision=SINGLE, getMemoryFromAnalysis=True, historyPrint=OFF, 
    memory=90, memoryUnits=PERCENTAGE, model='Model-1', modelPrint=OFF, 
    multiprocessingMode=DEFAULT, name='Job-1', nodalOutputPrecision=SINGLE, 
    numCpus=1, numGPUs=0, queue=None, resultsFormat=ODB, scratch='', type=
    ANALYSIS, userSubroutine='', waitHours=0, waitMinutes=0)

# This submits the job
mdb.jobs['Job-1'].submit(consistencyChecking=OFF)


# TO WAIT FOR JOB COMPLETION
mdb.jobs['Job-1'].waitForCompletion()
print("SS I-beam Model finished running")
