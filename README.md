# MotorSim
Simulink model and python interface to simulate electrical motor operations.

### Matlab python engine installation
```
cd /usr/local/MATLAB/{VERSION}/extern/engines/
sudo chmod -R 775 python
cd python
pip install -e .
```

### Install this library
```
pip install -r requirements.txt
pip install -e .
```

### Run tests
```
pytest
```
