# CS373: AI for Robotics lesson5: PID Control

## Smoothing 
- Algorithm Concept:
    + declare point $y_i$ with $x_i$ value
    + 2 criteria: 
        + $min(x_i - y_i)^2$
        + $min(y_i - y_{i+1})^2$
- Gradient Descent:
    + formula: $b = a -\gamma \nabla F(a)$  
        + a: current position
        + b: next step
        + $\gamma$: constant
        + $\nabla F(a)$: gradient 
    + gradient->differential, follow to get to the minimum


## PID Control
- P:Proportional
    + Overshoot, oscillating around target state
    + marginally stable
- D:Differential
- I:Integral
- TWIDDLE: Coordinate Ascent
    - Optimize PID gain