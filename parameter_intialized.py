

class parameter():
	def __init__(self):
		self.Time_interval =3.0 # coding time interval
		self.beta=0.7
		self.q=6 # total number of reciptive field
		self.sigma=0.6
		self.learning_rate=0.5
		# PLASTICITY Window and maximum weight change
		self.A=1 # value does not matter A/A while  calculation fractional contribution 
		self.toh=3 # time constant tah
		self.efficacy_value=0.55 # Window for STDP learning 
def parm():
	return parameter()
