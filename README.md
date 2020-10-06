# Road Trip:

This is a simple dataset of North American (though mostly U.S.) major roads.

city-gps.txt contains one line per city, with three fields per line, 
delimited by spaces. The first field is the city, followed by the latitude,
followed by the longitude.

road-segments.txt has one line per road segment connecting two cities.
The space delimited fields are:

- first city
- second city
- length (in miles)
- speed limit (in miles per hour)
- name of highway


Note that there are mistakes and bugs in these files and your code should
still operate correctly; e.g. not all cities that appear in road-segments.txt
have a corresponding line in city-gps.txt. You should assume that all roads
in road-segments.txt are bidirectional, i.e. none are one-way roads, so
that it's possible to travel from the first city to the second city at the
same distance at speed as from the second city to the first city.

➔ This problem has been solved using DFS implemented using Priority Queue.

➔ To solve this problem, we started with the DFS algorithm to calculate the distances between the cities provided as input. However, the time taken was much greater and was unable to provide a solution at times within the timeframe. Next, we implemented it using BFS which provided a faster and optimal solution. We then came up with an idea to implement DFS using Priority Queue which turned out to be much faster and optimal similar to the BFS. We tried using heuristics like Manhattan and Euclidean distance but they did not provide the optimal solution, so we did not use any heuristic in the final code.

➔ The search abstractions for this problem are stated below:

    ◆ State Space: All possible cities mentioned in the dataset
    ◆ Successor Function: Any city which plays an intermediate to reach our destination or the destination itself.
    ◆ Cost: As defined by the input(segments, distance, time or mpg)
    ◆ Goal state: the destination city with the required cost function
