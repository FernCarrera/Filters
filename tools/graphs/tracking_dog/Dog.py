import numpy as np
import math
import copy
from numpy.random import randn

class Dog():

    def __init__(self,x0=0,velocity=1,measurement_var=0.0,process_var=0.0):
        ''' x0 - initial position
            velocity - += right, -=left
            measurement_variance - variance in measurement m^2
            process_variance - variance in process (m/s)^2
        '''
        self.x = x0 #initial position
        self.velocity = velocity
        self.measurement_noise = math.sqrt(measurement_var) # converting to std deviation
        self.process_noise = math.sqrt(process_var) # converting to std deviation
  
        self.sensor = 0.0

    @property
    def get_pos(self):
        return self.x

    @property
    def get_vel(self):
        return self.velocity

    @property
    def get_sensor(self):
        return self.sensor

    def move(self,dt=1.0):
        ''' compute new position of dog, 
            every dt '''
        velocity = self.velocity + randn()*self.process_noise*dt
        self.x += velocity*dt

    def sense_position(self):
        # simulating measuring the position with some  noise
        return self.x + randn()*self.measurement_noise

    def sense_custom(self):

        self.sensor = self.x + randn()*self.measurement_noise

    def move_and_sense(self,dt=1.0):
        self.move(dt)
        x = copy.deepcopy(self.x)
        return x, self.sense_position()

    def run_simulation(self,dt=1,count=1):
        ''' simulate dog moving over a period of time
        returns: data: np.array[float,float]
        first column returns the actual position of dog
        second column returns the measurement of that position
        '''
        return np.array([self.move_and_sense(dt) for i in range(count)])