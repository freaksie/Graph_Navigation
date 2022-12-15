
Author : Neel Vora
Email: neelrajeshbhai.vora@uta.edu



Implementation:

uniformed_cost_search() - It implement the uninformed search with uniform cost search approach.
Astar() - It does informed search by taking heuristic files with a* approach.


Steps:
1) For uninformed search write following command in cmd or terminal, Here I have used VScode Terminal

Command->python find_route.py input1.txt Bremen Kassel 

	Output:

	Nodes Popped: 12
	Nodes Expanded: 6  
	Nodes Generated: 20
	distance: 297.0km  
	route:
	Bremen to Hannover : 132.0Km
	Hannover to Kassel : 165.0Km

Command -> find_route.py  input1.txt London Kassel 
        
	Output:
	
	Nodes Popped: 7
	Nodes Expanded: 4
	Nodes Generated: 7
	Distance: Infinity
	Route:
	None

2) For informed search Using heuristic value: 

Command->python find_route.py input1.txt Bremen Kassel h_kassel.txt 

	Output:

	Nodes Popped: 3
	Nodes Expanded: 2
	Nodes Generated: 8
	distance: 297.0km
	route:
	Bremen to Hannover : 132.0Km
	Hannover to Kassel : 165.0Km

