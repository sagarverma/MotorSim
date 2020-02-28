import pytest

from MotorSim.simconfig import SimConfig

class Test_SimConfig(object):
    def test__init(self):
        config = SimConfig()
        assert config.Data_Ts == config.Ts
        assert config.tauL == 25

    def test__get_config_json(self):
        config = SimConfig()
        params = config.get_config_json()
        assert isinstance(params, dict)
        assert len(params.keys()) == 39
