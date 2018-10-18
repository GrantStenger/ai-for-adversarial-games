# Optimal Elevator Routing

### Problem Statement
We develop and experimentally compare policies for the control of a system of k elevators with capacity c in a transport environment with l floors, an idealized version of a pallet elevator system in a large distribution center. Each elevator in the idealized system has an individual waiting queue of infinite capacity. On each floor, requests arrive over time in global waiting queues of infinite capacity. The goal is to find a policy that, without any knowledge about future requests, assigns an elevator to each request and a schedule to each elevator so that certain expected cost functions (e.g., the average or the maximal flow times) are minimized.

### History and Background
- Good context here [2]
- "Optimization literature on elevator control in particular is surprisingly sparse." [3]

### Questions
- Test generalizations:
	- k: elevators
	- l: floors
	- l_i: floors per elevator given all have lobby 0
	- elevators have different ground floors
  - c: capacity
	- staircase? If there is a staircase, we should incur some cost for having people use them
	- m: max number of people per elevator
- What if elevators split into different zones? (i.e. elevator 1 accesses lobby and floors 1-10, elevator 2 accesses lobby and floors 11-20, … , elevator 10 accesses lobby and floors 91-100)
- What happens of there is an additional staircase? Can drop passengers off within a floor or two of their destination and have them walk. Should incur a large cost for this.
- What if we include time necessary for elevator to accelerate and for door closing and opening?
- How effective is zoning? What would be optimal given two elevators, one elevator going to all odd and one to all even, one to all low and one to all high, both elevators to all floors, or some other sort of zoning construction?
- How should routing policy change as the arrival rate changes? ("An arrival
rate λ of 0.4 seconds means that, on average, every second there are 0.4 passengers arriving to the ground floor lobby, i.e. on average the time between two arrivals is 1/0.4 = 2.5 seconds." [1])

### Starting Assumptions
- Assume only travel from floor 1-n to lobby (floor 0)
- Assume equally likely to travel to each floor
- Assume constant flow of passengers, then assume uniform distribution of passenger arrival and exit, then assume poisson.
- "The passengers arrive at the ground floor approximately according to a Poisson process. This means that the inter-arrival times follow the exponential distribution, with the following probability density function: x*e^(-λx), where λ is the arrival rate. The destination of a passenger follows a uniform distribution. Every populated floor (1, 2, 3 and 4) has the same probability to be chosen." [1]
- Originally assume 1 elevator and h floors, then assume n elevators
- There is no extra staircase
- There is no max number of people per elevator
- Elevator is either waiting for passengers or moving at a constant speed. Later include time necessary to accelerate and for door closing and opening
- Originally only assume passengers going up (e.g. weekday morning). Next solve problem where passengers only go down (e.g. weekday evening). Then solve problem with passengers coming up and down. Then solve problem where passengers can travel inter-floor as well.
- Time for doors to open and doors to close: ____
- Time for k passengers to enter and exit elevator: ____
- Time to pass from one floor to the next: ____
- "In the model, the maximum load of the elevators is infinite. This is not realistic; most systems have a load sensor in the elevator. The load sensor tells the computer how full the elevator is. If the elevator is near capacity, the computer would not make any more pick-up stops until some people have gotten off."

### Optimize For
- Expected wait time per passenger
- Expected journey time per passenger
- Average number of passengers waiting
- Total elevator distance (efficiency, cost effectiveness?)
- 95th percentile longest waiting time, longest journey, passengers waiting

### Approaches
- Dynamic programming
- Stochastic simulation
- Artificial intelligence with historical data (e.g. Traffic Master System 9000)

### Algorithms
##### Simplest ("The Elevator-Algorithm") [1]
-  An elevator continues traveling in the same direction while there are remaining requests in that same direction.
-  If there are no further requests in that direction, then the elevator stops and become idle, or change direction if there are requests in the opposite direction.

##### FIFO Heuristic [3]
"It was observed that FIFO was problematic in high load periods"

##### Nearest-Neighbors Heuristic [3]
"It was observed that the NEAREST-NEIGHBOR heuristic was fast but unreliable in the following sense: surprisingly often, individual pallets were not transported at all for a very long time."

### Disorganized Notes
- “Traffic in an elevator consists of three
components: incoming, outgoing and inter-floor components.” [1]
- Model elevator as discrete-event system

### To-Dos:
- Implement [NIPS Paper](https://papers.nips.cc/paper/1073-improving-elevator-performance-using-reinforcement-learning.pdf) [4]
- Finish digging through [3]

### Sources
[1] https://beta.vu.nl/nl/Images/werkstuk-boer_tcm235-91327.pdf
[2] https://www.popularmechanics.com/technology/infrastructure/a20986/the-hidden-science-of-elevators/
[3] [Online-optimization of multi-elevator transport systems with reoptimization algorithms based on set-partitioning models](https://www.sciencedirect.com/science/article/pii/S0166218X06001466)
[4] [Improving Elevator Performance Using Reinforcement Learning](https://papers.nips.cc/paper/1073-improving-elevator-performance-using-reinforcement-learning.pdf)

### Interesting, Unused Sources (i.e. Papers to Go Through)
- Elevator traffic handbook: theory and practice
- [Optimal control of double-deck elevator group using genetic algorithm](https://www.popularmechanics.com/technology/infrastructure/a20986/the-hidden-science-of-elevators/)
- [Elevator Group Control Using Multiple Reinforcement Learning Agents](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.464.6183&rep=rep1&type=pdf)


*Keywords & Tags*: vehicle routing, simulation, optimization
