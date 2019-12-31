from collections import namedtuple
import numpy as np
from Dog import Dog

def update(prior,measurement):
    ''' update portion of kalman filter
        prior and measurement are tuples
    
    '''
  
    x,P = prior # mean and variance of the prior
    z,R = measurement[0],measurement[1] # mean and variance of the measurement
  
    y = z - x   # residual
    K = P/(P + R)   # kalman gain

    x = x + K*y # posterior
    P = (1 -K)*P    # posterior variance

    return gaussian(x,P)

def predict(posterior,movement):
    x,P = posterior # mean and variance of posterior
    dx,Q = movement # mean and variance of movement

    x = x + dx
    P = P + Q
    return gaussian(x,P)




gaussian = namedtuple('Gaussian',['mean','var'])
gaussian.__repr__ = lambda s: 'gauss(μ={:.3f}, sigma²={:.3f})'.format(s[0], s[1])

process_var = 2.
sensor_var = 4.5

x = gaussian(0.,400.)
process_model = gaussian(1.,process_var)
N = 10

dog = Dog(x.mean,process_model.mean,sensor_var,process_var)

zs = [dog.move_and_sense() for _ in range(N)]

xs,priors = np.zeros((N,2)),np.zeros((N,2))

for i,z in enumerate(zs):
    prior = predict(x,process_model)
    x = update(prior,z)
    priors[i] = prior
    xs[i] = x

print([x[0] for x in zs])
print('---')
print(xs)
