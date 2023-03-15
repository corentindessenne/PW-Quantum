import numpy as np
# Importer methodes pour definir entre autres un modèle ISING
import dimod
import dwave.inspector
# On importe les librairies de DWAVE
from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite

# Resolution du Max-Cut Problem sur une petite instance.

# On definit un group tres simple avec deux noeuds.
# J correspond aux expressions quadratiques
# (var1, var2):poids
J = {(1,2):1, (1,4):3, (2,3):3, (4,3):4, (3,5):5, (4,5):2, (4,6):4, (5,6):2}
# poids de chaque qubits pris individuellement
h = {}

# On rentre le modele dans la structure associee.
model = dimod.BinaryQuadraticModel(h, J, 0.0, dimod.SPIN)
# On affiche le modèle
print("Le modele resolu est le suivant :")
print(model)


##                RESOLUTION APPROCHEE              ##
##     Recuit quantique sur Machine D-WAVE          ##
sampler = EmbeddingComposite(DWaveSampler(solver='Advantage2_prototype1.1'))
sampler_name = sampler.properties['child_properties']['chip_id']
response = sampler.sample(model, num_reads=5000)
print("The solution obtained by D-Wave's quantum annealer",sampler_name,"is")
print(response)
#dwave.inspector.show(response)
 
