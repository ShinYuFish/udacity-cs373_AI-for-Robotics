# CS373: AI for Robotics lesson6: SLAM

## Planning Comparison
| Filters| Countinuous | Optimal | Universe | Local |  
| ------ | ----------- | ------------ | -----------| ------------------|  
| BFS | x |v| x | x| 
| A* | x | v | x | x | 
| DP | x |v| v| x | 
| smoothing| v | x | x | v |

## Simultaneous Localization and Mapping
Uncertainty(Noise) in robot motion and sensor sensing, leads to perform localization during robots movement
- Graph SLAM:
    + Turned motion into gaussian function->probability
        + For the gaussian function, the covariance represent the certainty of measurement, we can give higher weight for measurement with high certainty.
    + collect constraints:
        + Initial Location: $x_0$
        + relative motion constraint: $x_1$, $x_2$
        + relative landmark constraint: $L_1$, $L_2$
    + Using distance relation among those constraint to initial system matrix $\Omega$ and corresponding value $\xi$, by calculating $\Omega$.`inverse()` * $\xi$ can get the estimating value of every object's location $\mu$

## Related Resource
#### Video
- Rotot Mapping
#### Reading Material
- [SLAM for Dummies](https://ocw.mit.edu/courses/aeronautics-and-astronautics/16-412j-cognitive-robotics-spring-2005/projects/1aslam_blas_repo.pdf)
- [Graphical SLAM - A Self-Correcting Map](http://www.nada.kth.se/~johnf/johnficra04.pdf) by John Folkesson and Henrik Christensen
- [A tutorial on Graph-based SLAM](https://www.researchgate.net/publication/231575337/download)