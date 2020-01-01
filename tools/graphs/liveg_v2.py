
from Kalman import One_D_Kalman
from tracking_dog.Dog import Dog 
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib
import numpy as np


dog = Dog(measurement_var=500.5,process_var=30.0)
kal = One_D_Kalman()
dt = 1 # 30 frames per second

fig = plt.figure()
#fig.set_tight_layout(True)
ax = fig.add_subplot(111)
ax.grid()


line, = ax.plot([],[],'ro')
time_text = ax.text(0.02, 0.95, '', transform=ax.transAxes)

times = []
x_pos = []
sensor_pos = []
kalman_pos = []
prev = 0

patches = x_pos + sensor_pos + kalman_pos

states_to_track = 3 # make this input to class
lines = []
plotcols = ["orange","white","black"]
names = ['Actual Movement','Sensor Data','kalman_estimate']
markers = ['_','o',',']
# make lines of states to track
for index in range(states_to_track):
    state_set = plt.plot([],[],color=plotcols[index],marker=markers[index],label=names[index])[0]
    lines.append(state_set)

def init():
    '''init animation'''
    for line in lines:
        line.set_data([],[])
    
    time_text.set_text('')

    return patches
x = (50.0,20.0**2)
var = []
def animate(i):
    ''' animation epoch'''
    global dog,dt,x

    dog.move(dt)
    sensor = dog.move_and_sense()   # makes dog move and return sensor data
    
    prior = kal.predict(x,(0,0.40))
    x = kal.update(prior,(sensor[1],1.5))
    

    times.append(i)
    x_pos.append(sensor[0])
    sensor_pos.append(sensor[1])
    kalman_pos.append(x[0])
    var.append(x[1])
    
    data = [x_pos,sensor_pos,kalman_pos]
    time_text.set_text('Time = %.1f' % i)

    
    for t,line in enumerate(lines):
        
        #line.set_data(alist[i],blist[i],clist[i])
        line.set_data(times,data[t])
        time_text.set_text('Frame = %.1f' % i)
    return lines,time_text

'''used to define interval time '''
from time import time
t0 = time()
animate(0)
t1 = time()
interval = 1000*dt - (t1-t0)


ani = FuncAnimation(fig,animate,frames=201,interval=dt,init_func=init,repeat=False)



plt.xlim(0,200)
plt.ylim(0,400)

plt.xlabel('time s')
plt.ylabel('position')
#plt.autoscale(enable=True,axis = 'both',tight=False)
plt.legend()
plt.show()

plt.xlabel('time s')
plt.ylabel('Variance m^2')
plt.plot(var)
plt.show()
print('Variance converged to {:.3f}'.format(var[-1]))
