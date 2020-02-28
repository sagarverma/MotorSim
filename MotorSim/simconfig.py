
class SimConfig(object):
    def __init__(self):
        Psdnom = 0.95
        Prdnom = 1

        self.Data_Ts = 1/4000

        self.Ts = 0.000250
        self.Tpwm = 0.000250
        self.Tfixe = 500e-6

        self.Rs = 1.5
        self.Rr = 0.9

        self.Ls = 0.160
        self.Lr = 0.160
        self.Lm = 0.153
        self.Lfs = 0.007
        self.Lfr = 0.007
        self.Lmt = 0.210

        self.P1 = 0.7
        self.P2 = 1.5
        self.np = 2
        self.Psdnom = Psdnom

        self.Uo = 15
        self.Ulim = 415*(2/3)**0.5

        self.Psinit = [ Psdnom,  0 ]
        self.Prinit = [ Prdnom,  0 ]
        self.Inom = 9.1
        self.Prdnom = Prdnom

        self.SLP_Coeff = 100
        self.Vnom = 400
        self.SFC_Coeff = 100

        self.J = 0.045
        self.wrinit = 2*3.14*0
        self.thrinit = 0
        self.Jm = 0.045

        self.tauL = 25
        self.wL = 2*3.14*0

        self.wCurr = 0
        self.wSpeed_PI = 2*3.14*2.5
        self.xiSpeed_PI = 1
        self.wCurr_PI = 2*3.14*50
        self.xiCurr_PI = 1/2
        self.wSpeedEst = 2*3.14*500

        self.wn = 2*3.14*50
        self.Tn = 25
