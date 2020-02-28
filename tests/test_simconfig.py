import pytest

from MotorSim.simconfig import SimConfig

def test__SimConfig():
    config = SimConfig()
    assert config.Data_Ts == config.Ts
    assert config.tauL == 25
