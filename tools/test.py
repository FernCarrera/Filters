from Kalman import One_D_Kalman
import numpy as np
import matplotlib.pyplot as plt

data = []
velocity = 0
dt = 1
time = np.linspace(0,100,num=100)
for x in range(0,100):
    
    velocity = velocity + np.random.randn()*dt  
    data.append(velocity)



state = (0,8)
process = (1,2)
kalm = One_D_Kalman()
xs = []

for i,z in enumerate(data):
    prior = kalm.predict(state,process)
    x = kalm.update(prior,(z,1))
    xs.append(x[0])

plt.plot(time,data, label='data')
plt.plot(time,xs,label='kalman state')
plt.legend()
plt.show()

