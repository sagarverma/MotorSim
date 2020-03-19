import pytest

from motorsim.simconfig import SimConfig

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

    def test__set_config_json(self):
        config = SimConfig()
        params = config.get_config_json()
        params['Tn'] = 30
        config.set_config_from_json(params)
        assert len(config.__dict__) == 39
        assert config.Tn == 30
