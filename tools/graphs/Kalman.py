


class Kalman():

    def __init__(self):
        pass


class One_D_Kalman(Kalman):

    def __init__(self,state=0.0):
        self._state = state

    
    def get_state(self):
        return self._state

    

    def update(self,prior,measurement):

        x,P = prior   # state of the system mean of the prior
       # variance of prior (state)

        z,R = measurement # variance of measurement

        y = z - x             # calculate residual
        K = P/(P + R)    # Kalman gain
        
        x = x + K*y           # posterior calculation
        P = (1-K)*P           # posterior variance

        
        
        return (x,P)

    def predict(self,posterior,movement):

        x,P = posterior   # variance of prior (state)

        dx,Q = movement

        x = x + dx
        P = P + Q

       

        return (x,P)




