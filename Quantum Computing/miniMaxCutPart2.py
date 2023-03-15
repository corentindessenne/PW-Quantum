from dimod import ConstrainedQuadraticModel, CQM, SampleSet
from dimod import Binary, quicksum
from dwave.system import LeapHybridCQMSampler
from dimod.serialization.format import Formatter
import numpy as np

totalNumberOfSloths = 6
numberOfDormitories = 3
c2 = [[0, 1, 6, 1, 8, 0], [1, 0, 3, 3, 9, 8], [6, 3, 0, 8, 7 , 4],
      [1, 3 ,8, 0, 9, 8], [8, 9, 7, 9, 0, 9, ], [0, 8, 4, 8, 9, 0]]
beds = [1, 2, 3]
cqm = ConstrainedQuadraticModel()

x = {
(i, d): Binary('x{}_{}'.format(i, d))
for i in range(totalNumberOfSloths)
for d in range(numberOfDormitories)}

objective = quicksum(c2[i][j] * x[(i,d)] * x[(j,d)]
    for i in range(totalNumberOfSloths - 1)
    for j in range(i + 1, totalNumberOfSloths)
    for d in range(numberOfDormitories))
cqm.set_objective(objective)

for d in range(numberOfDormitories):
    cqm.add_constraint(quicksum(x[(i,d)]
    for i in range(totalNumberOfSloths)) <= beds[d])

for i in range(totalNumberOfSloths):
    cqm.add_constraint(quicksum(x[(i,d)]
    for d in range(numberOfDormitories)) == 1)

cqm_sampler = LeapHybridCQMSampler()
sampleset = cqm_sampler.sample_cqm(cqm)

Formatter(width=270).fprint(sampleset)