'''
	Author : Neel Vora
	Email: neelrajeshbhai.vora@uta.edu
'''
import sys

# This function will convert input file into Hash Map for graph navigation
def Hash_Map(input_file):
	for city in input_file:
		if(city.lower().find("end of input") != -1):
			break
		else:
			features = city.strip().split(" ")
			src_var = features[0]
			des_var = features[1]
			if des_var in cities:
				pass
			else:
				cities.append(des_var)

			if src_var in cities:
				pass
			else:
				cities.append(src_var)
			
	cities.sort()
	for i in range(len(cities)):
		distance_cities.append([])
		for j in range(len(cities)):
			distance_cities[i].append(-1)
		distance_cities[i][i] = 0
	for city in input_file:
		if(city.lower().find("end of input") != -1):
			break
		else:
			temp = city.strip().split(" ")
			source = temp[0]
			destination = temp[1]
			distance = temp[2]
			distance_cities[cities.index(source)][cities.index(destination)] = float(distance)
			distance_cities[cities.index(destination)][cities.index(source)] = float(distance)
	return

# Checks if current node is already visited or not
def check_visited(curr,vis):
	for node in vis:
		if curr != node["node"]:
			return False
	return True


def set_fringe(fringe,temp):
	if(len(fringe) > 1):
		for i in range(0, len(fringe)-1):
			minimum = i
			for j in range(i+1,len(fringe)):
				m = fringe[minimum]["cumulative_cost"]
				n = fringe[j]["cumulative_cost"]
				if temp:
					m += fringe[minimum]["heuristic_value"]
					n += fringe[j]["heuristic_value"]
				if(m > n):
					minimum = j
			t = fringe[minimum]
			fringe[minimum] = fringe[i]
			fringe[i] = t
		return fringe
	else:
		return fringe

def path(route,visited):
	path = []
	def Extract(destination,visited):
		if destination is None:
			return
		else:
			for node in visited:
				if node["node"] == destination:
					path.append(destination)
					Extract(node["parent"],visited)

	if route:
		print("Distance: " + str(route["cumulative_cost"]) + "Km")
		print("Route:")
		Extract(route["current_node"],visited)
		path.reverse()
		for i in range(0,len(path)-1):
			print(cities[path[i]] + " to " + cities[path[i+1]] + " : " + str(distance_cities[path[i]][path[i+1]]) + "Km")
	else:
		print("Distance: Infinity")
		print("Route:")
		print("None")
	return


def uniformed_cost_search():
	n_p = 0  # Counter for popped nodes
	n_g = 1  # Counter for generated nodes
	n_e = 0  # Counter for expanded node
	destination = cities.index(d)
	fringe = []  
	visited = [] 
	route = False
	fringe.append({"current_node":cities.index(s),"cumulative_cost":0,"parent_node":None}) 
	while(len(fringe) > 0): 
		n_p += 1
		if(fringe[0]["current_node"] == destination):
			visited.append({"node":fringe[0]["current_node"],"parent":fringe[0]["parent_node"]})
			route = fringe[0]
			break
		elif check_visited(fringe[0]["current_node"],visited):
			del fringe[0] 
			continue
		else:
			visited.append({"node":fringe[0]["current_node"],"parent":fringe[0]["parent_node"]})
			for i in range(len(distance_cities[fringe[0]["current_node"]])):
				if distance_cities[fringe[0]["current_node"]][i] > 0:
					fringe.append({"current_node":i,"cumulative_cost":fringe[0]["cumulative_cost"]+distance_cities[fringe[0]["current_node"]][i],"parent_node":fringe[0]["current_node"]})
					n_g += 1
			n_e += 1
			del fringe[0]
			fringe = set_fringe(fringe,False)
	print("Nodes Popped: "+str(n_p))
	print("Nodes Expanded: "+str(n_e))
	print("Nodes Generated: "+str(n_g))
	path(route,visited)
	return

def heuristic_values(heuristic_file):
	for h in heuristic_file:
		if h.lower().find("end of input") != -1:
			break
		else:
			heu = h.split(" ")
			heuristics[cities.index(heu[0])] = float(heu[1])
	return

def Astar():
	n_p = 0  # Counter for popped nodes
	n_g = 1  # Counter for generated nodes
	n_e = 0  # Counter for expanded node
	destination = cities.index(d)
	fringe = []
	visited = []
	route = False
	fringe.append({"current_node":cities.index(s),"cumulative_cost":0,"heuristic_value":heuristics[cities.index(s)],"parent_node":None})
	while(len(fringe) > 0):
		n_p += 1
		if(fringe[0]["current_node"] == destination):
			visited.append({"node":fringe[0]["current_node"],"parent":fringe[0]["parent_node"]})
			route = fringe[0]
			break
		
		elif check_visited(fringe[0]["current_node"],visited):
			del fringe[0]
			continue
		else:
			visited.append({"node":fringe[0]["current_node"],"parent":fringe[0]["parent_node"]})
			for i in range(len(distance_cities[fringe[0]["current_node"]])):
				if distance_cities[fringe[0]["current_node"]][i] > 0:
					fringe.append({"current_node":i,"cumulative_cost":fringe[0]["cumulative_cost"]+distance_cities[fringe[0]["current_node"]][i],"heuristic_value":heuristics[i],"parent_node":fringe[0]["current_node"]})
					n_g += 1
			n_e += 1
			del fringe[0]
			fringe = set_fringe(fringe,True)	
	print("Nodes Popped: "+str(n_p))
	print("Nodes Expanded: "+str(n_e))
	print("Nodes Generated: "+str(n_g))
	path(route,visited)
	return
					
 

if __name__ == "__main__":

    if(len(sys.argv) >= 4):
        cities = []
        distance_cities = []
        Hash_Map(open(sys.argv[1],"r").read().split("\n"))
        s = sys.argv[2]
        d = sys.argv[3]
        if(len(sys.argv) == 4):
            uniformed_cost_search()
        elif(len(sys.argv) == 5):
            heuristics = [0] * len(cities)
            heuristic_values(open(sys.argv[4],"r").read().split("\n"))
            Astar()
        else:
            print("There is an error in input file")
    else:
        print("There is an error in input file")