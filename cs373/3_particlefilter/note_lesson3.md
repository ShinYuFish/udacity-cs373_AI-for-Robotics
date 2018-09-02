# CS373: AI for Robotics lesson3: Particle Filter

## Comparison(lesson3:part5)

| Filters| state space | peak numbers | efficiency | apply in robotics |  
| ------ | ----------- | ------------ | -----------| ------------------|  
| Histogram Filter | Discrete |multimodal| exponential | approximate | 
| Kalman Filter  | Continuous | unimodal |  quadradic  | approximate | 
| Particle Filter| Continuous |multimodal| higher | approximate | 

## Particle Filter
- Advantage: Easy to Program / Deal with non-linear non-guassian model
- Principle:
    + Monte Carlo localization
    + Bayes' Rule 
- Representation: Particle, each particle represents a guess of the location of the robot
    + structure: structured by 3 elements *X-coordinate* ,Y-coordinate*, *heading direction*
    + concept: splay a bunch of particles into the space, use the sensor data to calculate its weight, weight stands for the importance of the particle
    + meaning: the higher the density of particles refers to higher probability the robot may locate
- RAW: Filter measurement iterates and check how consisent are the particle values are, the consistency is porportion to the survive probabiliy of particle. At the end, particles will converged to a location with the highest consitency.
- Process:
    + Measurement/Sense: compare measurement data and measurement data on particle to get particle weight
    + **Resample**: generate N particles at the location by taking normalized weight as probability of N previous particles
        * How to implement in Python code?
            1. linear distribution with random weight generated
            2. resampling wheel
            ```python
            def resampling_wheel(w, p):
                index = 0#int(random.uniform(1,N))
                beta = 0
                for i in range(N):
                    beta += random.uniform(0, 2 * max(w))
                    while w[index] < beta:
                        beta -= w[index]
                        index += 1
                    return p[index]
    
            for i in range(N):
                new_particle = resampling_wheel(w, p)
                p3.append(new_particle)
                + Move: system stransformation matrix
            ```

## Related Resource
#### Video
- [Particle Filter Basic Idea](https://www.youtube.com/watch?v=_LjBba2hnfk) by Udacity Intro to Computer Vision
- [Particle Filter Explained without Equations](https://www.youtube.com/watch?v=aUkBa1zMKv4)
- [SLAM course-Particle Filter](https://www.youtube.com/watch?v=eAqAFSrTGGY)

#### Reading Material
- [wiki](https://en.wikipedia.org/wiki/Particle_filter)
- [Particle Filters in Robotics](http://robots.stanford.edu/papers/thrun.pf-in-robotics-uai02.pdf)
- [A Tutorial on Particle Filters for Online Nonlinear/Non-Gaussian Bayesian Tracking](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.117.1144&rep=rep1&type=pdf)
