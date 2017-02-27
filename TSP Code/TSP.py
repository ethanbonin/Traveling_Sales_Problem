import sys
import random
from math import sqrt
from itertools import permutations
from timeit import default_timer as timer
import parseFile


def rand(value):
    points = []
    for x in range(0, value):
      y = random.random()*100
      x = random.random()*100
      a = [x, y]
      points.append(a);

    #writes to a file with current points. before they are chosen for an optimal route.
    target = file("points.txt", "w+")
    for p in points:
        target.write('{}'.format(p))
        target.write('\n')
    target.close()

    return points

#Calculates the distances between points
def calculateDistance(current, point):
     return sqrt(((current[0]-point[0])**2) + ((current[1] - point[1])**2))

#Returns true is comparing is less than current distances
def compare(comparing, current):
    if comparing < current:
        return True
    return False


def OptimalRouteNearestNeighbor(opt):
    # writes to a file with current points. after they are chosen for an optimal route.
    target = file("newRoute.txt", "w+")
    for p in opt:
        target.write('{}'.format(p))
        target.write('\n')
    target.close()

def OptimalRouteBrute(opt):
    # writes to a file with current points. after they are chosen for an optimal route.
    target = file("newRoute.txt", "w+")
    target.write("Total Distance: %s" % opt[1])
    target.write('\n')
    for p in opt[0]:
        target.write('{}'.format(p))
        target.write('\n')
    target.close()


def NearestNeighbor(point):
    optimalRoute = []
    current = point[0]
    optimalRoute.append(point[0])
    point.remove(current)

    while point:
        distance = calculateDistance(current, point[0])
        next = point[0]

        for p in point:
            comparingDistance = calculateDistance(current, p)
            if compare(comparingDistance, distance):
                next = p
                distance = comparingDistance
        optimalRoute.append(next)
        point.remove(next)
        current = next

    return optimalRoute





def PermuationOfPoints(points):
  value = [p for p in permutations(points)]
  return value


def totalPath(route):
    total = float("inf")
    for bestDistance, p in route.items():
        if bestDistance < total:
            total = bestDistance
            optimalRoute = p
    return (optimalRoute, total)


def ExhaustiveRoute(P):
    optimalRoute = []
    total = 0
    permutation = PermuationOfPoints(points)
    route = {} 
    for p in permutation:
        distance = 0
        for i in range(0, len(p)-1):
            distance += calculateDistance(p[i], p[i+1])
        distance += calculateDistance(p[0], p[len(optimalRoute)-1])
        route[distance] = p
    return (totalPath(route))



print "Welcome to the TSP. Would you like to your own file?[1]\nOr\nRandomly Generate a file?[2]"

choice = input()

if choice == 1:
    parse = parseFile.ParseFile()
    points = parse.read()
    value = input("Would you like to use Nearest Neighbor(0) or Exhaustive Search(1): ")
else:
    print "Choice 2 Chosen"
    points = input("How many points would you like?: ")
    points = rand(points)
    value = input("Would you like to use Nearest Neighbor(0) or Exhaustive Search(1): ")

if value == 0:
    startTimer = timer()
    opt = NearestNeighbor(points)
    endtimer = timer()
    OptimalRouteNearestNeighbor(opt)
if value == 1:
    startTimer = timer()
    opt = ExhaustiveRoute(points)
    endtimer = timer()
    OptimalRouteBrute(opt)

time = repr(endtimer - startTimer)
print("\n\ntime = " + time)
