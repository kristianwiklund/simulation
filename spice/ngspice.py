#! /usr/bin/python
from __future__ import absolute_import, division, print_function, unicode_literals

from .simulator import SimulatorBase

import numpy as np

class Ngspice(SimulatorBase):
    SIMULATOR = 'ngspice'

    def __init__(self, trace = None):
        super(Ngspice, self).__init__(trace)

    def update_variables(self, dataset):
        dataset.dt = []
        for idx, (name, unit, params) in enumerate(self.variables):
            name = name.upper()
            if name in [ 'V(V-SWEEP)', 'I(I-SWEEP)' ]:
                assert idx == 0
                name = 'SWEEP'

            dataset.unit[name] = unit
            dataset.params[name] = params

            name = str(name)

            if 'complex' in dataset.flags:
                dataset.dt.append(( name, np.complex128 ))
            else:
                dataset.dt.append(( name, '<f8' ))

Simulator = Ngspice
