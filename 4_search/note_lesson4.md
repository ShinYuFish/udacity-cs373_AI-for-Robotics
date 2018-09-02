# CS373: AI for Robotics lesson4: Search

## Motion Planning
- Definition: How to let robot move from start to end position
    + Given: map, starting position, goal position, *cost*
    + Goal: find minimum cost path
- Method: 
    + 2 working list iteration:
        + closed list: record every visited points
        + open list: waiting points to be visited
    + Dynamic Programming(?) -- self opinion
- Required Function:  

## A* search
- Purpose: Solving the Shortest Path Problem
- Enhancement of Dijkstra Algorithm - much faster/able to cope with more cases
- Formula: **h(n)**heuristic
  > f(n) = g(n) + h(n)  
  > g(n): distance from starting point to current node 
  > h(n): prediction distance of current node and goal  
  > f(n): weight of current node  
  > heuristic funciton may differs from cases

## Dijkstra Algorithm
- Purpose: To find the shortest path from starting point to goal
- Principle: 
    + Breadth First Search
    + A* search with *h(n) = 0* -> each direction is searched equally
- Formula:
  > min(d(a) + w(a)(b))  
  > d(a): shortest path from starting point to point a  
  > w(a)(b): distance(weight) between a and b  

## Dynamic Programming
- Setting problem into subsystem, and optimize result in each system comes to the best solution at the end of process
    + Given: map, goal
    + output: best path for ANYWHERE

## Related Resource
#### Reading Material
- [Dijkstra's Algorithm](http://www.csie.ntnu.edu.tw/~u91029/Path.html#4)
- [A Star Search Algorithm](https://cg2010studio.com/2011/12/20/a%E6%98%9F%E6%90%9C%E5%B0%8B%E6%BC%94%E7%AE%97%E6%B3%95-a-search-algorithm/)
- [Intro to A* Algorithm](https://swf.com.tw/?p=67)

#### Video
- [A* Pathfinding Algorithm](https://www.youtube.com/watch?v=aKYlikFAV4k) by The Coding Train
- [Dijkstra's Algorithm vs. A* Search vs. Concurrent Dijkstra's Algorithm](https://www.youtube.com/watch?v=cSxnOm5aceA) by UNSW Mechatronics
#### ROS
- [MoveIt!](https://moveit.ros.org/) ROS package: It provides an easy-to-use platform for developing advanced robotics applications, evaluating new robot designs and building integrated robotics products for industrial, commercial, R&D and other domains.
- [ROS Navigation: Path Planning with a Husky Robot](https://www.youtube.com/watch?v=zDUaazmSukM) by the Construct