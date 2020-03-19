import os

import matlab
import matlab.engine as me

class Py2Mat(object):
    def __init__(self, config):
        self.config = config

        self.eng = me.connect_matlab()
        self.eng.cd(os.path.dirname(os.path.realpath(__file__)))

        self._set_workspace()

    def _set_workspace(self):
        for k, v in self.config.get_config_json().items():
            if isinstance(v, list):
                self.eng.workspace[k] = matlab.double(v)
            else:
                self.eng.workspace[k] = float(v)

    def reconfigure(self, config):
        self.config = config
        self._set_workspace()
        
    def sim(self, ref_speed, ref_load, speed_time, load_time, sim_time):
        data = self.eng.conn_python(ref_speed, ref_load, speed_time, load_time, sim_time)
        return data
