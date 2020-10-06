#!/usr/local/bin/python3
#
# route.py: Find driving directions between pairs of cities given by the user
#
# Code by: Dhruva Bhavsar(dbhavsar), Hely Modi(helymodi), Aneri Shah(annishah)
#
# put your routing program here!

from queue import PriorityQueue
import sys
from math import sqrt


# Import data from file city-gps.txt
def load_city(filename):
    city_gps={}
    with open(filename, "r") as file:
        for line in file:
            l = line.split()
            city_gps[l[0]] = [ float(i) for i in l[1:] ] 
    return city_gps

# Import data from file road-segments.txt
def load_road(filename):
    roads=[]
    with open(filename, "r") as file:
        for line in file:
            roads.append(line.split())
    road=list(roads)
    for i in road:
        roads.append([i[1],i[0],i[2],i[3],i[4]])
    return roads

# Find the route between the given pair of cities and given cost function
def find_route(start_city,end_city,roads,cost_fn,citygps):
    visited=[]
    fringe=PriorityQueue()
    #cost,heuristic,start_city,path,total_segments,total_miles,total_hours,total_gas
    fringe.put((0,0,start_city,start_city+' ',0,0,0,0))
    
    while fringe:
        (cost,h,s,path,total_segments,total_miles,total_hours,total_gallon)=fringe.get()
#        print(cost)
#        cost=cost-h
        for c in roads:
             # Expand the successors till the destination is reached
            if(c[1] not in visited and c[0]==s):
                if c[1]==end_city:
                    return (total_segments+1,total_miles+int(c[2]),total_hours+(float(c[2])/float(c[3])),total_gallon+(int(c[2])/((400*(float(c[3])/150)*(1-(float(c[3])/150))**4))),path+c[1])
                else:
                    visited.append(c[1])                   
#                    h=heuristic(c[1],end_city,citygps)
#                    print(cost+calculate_cost(cost_fn,c))
                    fringe.put((cost+calculate_cost(cost_fn,c),h,c[1],path+c[1]+' ',total_segments+1,total_miles+int(c[2]),total_hours+(float(c[2])/float(c[3])),total_gallon+(int(c[2])/((400*(float(c[3])/150)*(1-(float(c[3])/150))**4)))))
            else:
                continue
    return False

# Function defining the heuristic                    
def heuristic(sc,dc,citygps):
    if(sc in citygps.keys() and dc in citygps.keys()):
        # Euclidean distance
        return sqrt((citygps[dc][0]-citygps[sc][0])**2+(citygps[dc][1]-citygps[sc][1])**2)
        # Manhattan distance
#        return (abs(citygps[dc][0]-citygps[sc][0])+abs(citygps[dc][1]-citygps[sc][1]))
    else:
        return 0
    

# Calculate cost based on given cost function
def calculate_cost(cost_fn,c):
    if(cost_fn=='segments'):
        return 1
    elif(cost_fn=='distance'):
        return (int(c[2])) 
    elif(cost_fn=='time'):
        return (float(c[2])/float(c[3]))
    elif(cost_fn=='mpg'):
        return (400*(float(c[3])/150)*(1-(float(c[3])/150))**4)
                            
if __name__ == "__main__":

#    if(len(sys.argv) != 4):
#        raise Exception('Error: expected 3 command line arguments')
#    start_city=sys.argv[1]
#    end_city=sys.argv[2]
#    cost=sys.argv[3]
    
    start_city='Charlotte,_North_Carolina'
    end_city='Milwaukee,_Wisconsin'
    cost='distance'
    
    city_gps=load_city("city-gps.txt")
    roads = load_road("road-segments.txt")
   

    if(find_route(start_city,end_city,roads,cost,city_gps)==False):
        print('Inf')
    else:
        solution=find_route(start_city,end_city,roads,cost,city_gps)
        print(*solution)