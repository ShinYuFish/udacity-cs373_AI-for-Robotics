# CS373: AI for Robotics lesson1: Localization

## Basic Concept
- The mathematical representation of position the robot/vehicle could be on the map is by Probability.
- Inexact move function
- The main concept is Move and Sense (based on Initial Condition)
    + `Sense`: product follow by normalization(sum = 1) lose information
    + `Move`: Convolution ,gain information
    + Concept of entropy

## Programming Work
```python
p=[0.2, 0.2, 0.2, 0.2, 0.2] # initial state
world=['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'red']
motions = [1,1]          
pHit = 0.6               # sensing probability match measurement
pMiss = 0.2              # sensing probability not match with measurement
pExact = 0.8            
pOvershoot = 0.1         # movement error
pUndershoot = 0.1        # movement

# probability result of sensing state 
# Z state for measurement/observation
def sense(p, Z):
    q=[]
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
    # Procedure of Normalization
    s = sum(q)
    for i in range(len(q)):
        q[i] = q[i] / s
    return q

# probability result when shift U block
def move(p, U):
    q = []
    # Convolution(previous position * movement distribution)
    for i in range(len(p)):
        s = pExact * p[(i-U) % len(p)]
        s = s + pOvershoot * p[(i-U-1) % len(p)]
        s = s + pUndershoot * p[(i-U+1) % len(p)]
        q.append(s)
    return q

# For each step, conduct one robot movement and location sensing
for k in range(len(measurements)):
    p = sense(p, measurements[k])
    p = move(p, motions[k])
    
print p         
```

## Probability 
- Bayes' Rule       
    p(X|Z) = P(Z|X)P(X) / P(Z) measurement probability * prior    
    X: Status, position     
    Z: Observation, probability of robot's appearance
- Theorem of Total Probability