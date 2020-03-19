
class SimConfig(object):
    def __init__(self):
        Psdnom = 0.95
        Prdnom = 1

        self.Data_Ts = 1/4000           #Data aquisition rate

        self.Ts = 0.000250              #Simulation time of the electrical part of the control law
        self.Tpwm = 0.000250            #Simulation time of the electrical part of the control law
        self.Tfixe = 500e-6             #Sampling time of the mechanical part of the control law

        self.Rs = 1.5                   #Stator resistance
        self.Rr = 0.9                   #Rorot resistance

        self.Ls = 0.160                 #Stator inductance
        self.Lr = 0.160                 #Rotor inductance
        self.Lm = 0.153                 #Mutual inductance
        self.Lfs = 0.007                #Stator leakage inductance
        self.Lfr = 0.007                #Rotor leakage inductance
        self.Lmt = 0.210                #Parameter for magnetic saturation model

        self.P1 = 0.7                   #Parameter for magnetic saturation model
        self.P2 = 1.5                   #Parameter for magnetic saturation model
        self.np = 2                     #Number of pole pairs
        self.Psdnom = Psdnom            #Nominal stator flux on axis-d

        self.Uo = 15                    #Not being used
        self.Ulim = 415*(2/3)**0.5      #Voltage limitation, hard-coded directly in the simulink

        self.Psinit = [ Psdnom,  0 ]    #Initial value of the stator flux
        self.Prinit = [ Prdnom,  0 ]    #Initial value of the rotor flux
        self.Inom = 9.1                 #Nominal current
        self.Prdnom = Prdnom            #Nominal rotor flux on axis-d

        self.SLP_Coeff = 100            #Parameter of the control law
        self.Vnom = 400                 #Nominal voltage
        self.SFC_Coeff = 100            #Parameter of the control law

        self.J = 0.045                  #Motor shaft inertia
        self.wrinit = 2*3.14*0          #Initial value of rotor speed
        self.thrinit = 0                #Initial value of the motor angle
        self.Jm = 0.045                 #Inertia of the motor

        self.tauL = 25                  #Torque load
        self.wL = 2*3.14*0              #Speed of the load

        self.wCurr = 0                  #Parameter of the control law
        self.wSpeed_PI = 2*3.14*2.5     #Parameter of the control law
        self.xiSpeed_PI = 1             #Parameter of the control law
        self.wCurr_PI = 2*3.14*50       #Parameter of the control law
        self.xiCurr_PI = 1/2            #Parameter of the control law
        self.wSpeedEst = 2*3.14*500     #Parameter of the control law

        self.wn = 2*3.14*50             #Nominal frequency (Not used)
        self.Tn = 25                    #Nominal torque

    def get_config_json(self):
        return {key:value for key, value in self.__dict__.items() if not key.startswith('__') and not callable(key)}
        
    def set_config_from_json(self, config):
        for k in config.keys():
            self.__dict__[k] = config[k]
