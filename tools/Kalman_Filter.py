''' 
    The filter focuses on deleting the noise
    the more noise the longer it takes to converge
    Single state because it only takes one data stream
'''

class SingleStateKalmanFilter():

    def __init__(self,A,B,C,x,P,Q,R):
        self.A = A     # process dynamics
        self.B = B     # Control dynamics
        self.C = C     # Measurement Dynamics
        self._current_state_estimate = x  
        self._current_prob_estimate = P
        self.Q = Q     # Process Covarience
        self.R = R     # Measurement Covariance 

    #@property
    def current_state(self):
        return self._current_state_estimate

    def step(self,*,control_input,measurement):

        # prediction step
        pre_state = self.A*(self._current_state_estimate) + self.B*control_input
        pre_prob = (self.A*self._current_prob_estimate)*self.A + self.Q

        # observation step
        innovation = measurement - self.C*pre_state
        innovation_covarience = self.C*pre_prob*self.C + self.R

        # update state
        kal_gain = pre_prob*self.C/(float(innovation_covarience))
        self._current_state_estimate = pre_state + kal_gain*innovation
        
        # nxn identity matrix
        self._current_prob_estimate = (1 - kal_gain*(self.C)*pre_prob)