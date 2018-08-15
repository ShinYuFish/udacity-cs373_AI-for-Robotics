# CS373: AI for Robotics lesson2: Kalman Filter

## Kalman Filter
- Purpose: state estimation(which is important in localization)
- Comparison:
    + Kalman Filter: continuous/uni-modal
    + Monte Carlo Localization: discrete model, multi-modal
    + Particue Filer: continuous/multi-modal
        - Uni-modal: one peak
- Representation: Guassian Distribution    
    + A 1-D Guassian characteristic is determined by two parameters: 
        + mean
        + variance: the smaller the better, less uncertainty
    + Multiply two Guassian (measurement update)
        * New mean is between the previous two means
        * New Covariance is LESS than previous covariances
    + High-dimenstional Gaussian
        * mu = 1 * n matrix
        * var = n * n matrix
        * 2-D figure, different shape corresponding different covariance on axis ex: circle vs. oval
- position and velocity
    + using observable parameter (position) to estimate hidden parameter
    + x' = x + delta(t) v'
- Parameter:
    + x: initial state
    + u: external motion
    + B: scale of external works on state
    + P: initial uncertainty
    + z: measurement
    + F: next state function
    + R: measurement uncertainty
    + H: measurement function
- UPDATE!!!!!!!!!!
    + *know-how*
        1. Estimate current state based on previous state and gyro measurements
        2. Predict priori error covariance matrix, based on previous matrix and noise.
        3. Collect observation data(innovation)   
        4. Compute the difference between observation data and predict state
        5. Get Kalman gain (innovation matrix covariance determines the reliability of data, the higher the covariance the bigger kalman gain)
        6. Update estimated data for current state
        7. Update the priori error covarianc matrix
        
## Programming Work:A Real Simple 1-D Kalman Filter
```python
# Merging guassian1 with guassian2
# corresponding to product
def update(mean1, var1, mean2, var2):      
    new_mean = float(var2 * mean1 + var1 * mean2) / (var1 + var2)
    new_var = 1./(1./var1 + 1./var2)
    return [new_mean, new_var]

 # Shifting one guassian1 with the parameter of guassian2
 # corresponding to addition
def predict(mean1, var1, mean2, var2):   
    new_mean = mean1 + mean2
    new_var = var1 + var2
    return [new_mean, new_var]

measurements = [5., 6., 7., 9., 10.]
motion = [1., 1., 2., 1., 1.]
measurement_sig = 4.       # Uncertainty for measurement
motion_sig = 2.            # Uncertainty for motion
mu = 0.
sig = 10000.

# Insert code here
for i in range(len(measurements)):
    [mu, sig] = update(mu, sig, measurements[i], measurement_sig)
    [mu, sig] = predict(mu, sig, motion[i], motion_sig)
print [mu, sig]

```

## Concept Review
**Update Measurement** and **Predict Motion**
