import pytest

import numpy as np

import matlab
from matlab.engine.matlabengine import MatlabEngine

from motorsim.simulators.conn_python import Py2Mat
from motorsim.simconfig import SimConfig

class Test_Py2Mat(object):
    @pytest.fixture()
    def test__init(self):
        config = SimConfig()
        py2mat = Py2Mat(config)

        assert isinstance(py2mat.eng, MatlabEngine)
        assert isinstance(py2mat.eng.workspace["Psinit"], matlab.double)
        assert isinstance(py2mat.eng.workspace["Data_Ts"], float)

        return py2mat

    def test__sim(self, test__init):
        ref_speed = "[0 0 50 50]"
        ref_load = "[0 0 0 0]"
        speed_time = "[0 1 1.5 3]"
        load_time = "[0 1 1.5 3]"
        sim_time = "3"

        py2mat = test__init
        data = py2mat.sim(ref_speed, ref_load, speed_time, load_time, sim_time)

        assert isinstance(data, matlab.double)

        data = np.asarray(data)
        assert data.shape[1] == 8
