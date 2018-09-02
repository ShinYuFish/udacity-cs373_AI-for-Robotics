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
    + gradient->differential, follow the slope to get to the minimum


## PID Control
- P:Proportional
    + Overshoot, oscillating around target state
    + marginally stable
- D:Differential
- I:Integral
- TWIDDLE: Coordinate Ascent
    - Optimize PID gain


## Related Resource 
#### Video
- [Mathematics of Gradient Descent - Intelligence and Learning](https://www.youtube.com/watch?v=jc2IthslyzM) by The Coding Train
- [PID Control - A bried Introduction](https://www.youtube.com/watch?v=UR0hOmjaHp0) by Brian Douglas
- [Simple Examples of PID Control](https://www.youtube.com/watch?v=XfAt6hNV8XM) by Brian Douglas
- [Controlling Self Driving Cars](https://www.youtube.com/watch?v=4Y7zG48uHRo)

#### Reading Material
- [Gradient Descent: All You Need To Know](https://hackernoon.com/gradient-descent-aynk-7cbe95a778da)
- [PID Control Principle](http://www.ni.com/white-paper/3782/zht/) by National Instrument
- [PID Control with MATLAB and Simulink](https://www.mathworks.com/discovery/pid-control.html) by MathWorks
