import pandas as pd
import numpy as np
import igraph
import sys

def isConnected(matrix, source, target):
	return matrix.iat[source,target]

def extract_subgraphs(network_file,is_absolute_output):
	subgraph = np.zeros(14) #we wont use the subgraph[0] position
	g = igraph.read(network_file,format="pajek")
	g = g.simplify(combine_edges="sum")
	size = g.vcount()
	matrix = pd.DataFrame(g.get_adjacency().data,index=range(size),columns=range(size))

	for A in range(0,size):
		firstDegreeNeighbours = np.where(matrix.iloc[A])[0]
		for B in firstDegreeNeighbours:  
			if isConnected(matrix,B,A): 
				secondDegreeNeighbours = np.where(matrix.iloc[B])[0].tolist()
				secondDegreeNeighbours.remove(A)#A might be a neighbor of B, but C has to be different than A 
				for C in secondDegreeNeighbours: 
					if isConnected(matrix,C, B):
						if (isConnected(matrix,C,A) and isConnected(matrix,A,C)):
							subgraph[13] += 1
						elif (not isConnected(matrix,C,A) and isConnected(matrix,A,C)):
							subgraph[12] += 1
						elif (not isConnected(matrix,C,A) and not isConnected(matrix,A,C)):
							subgraph[8] += 1
					else: # when isConnected(matrix,C, B) == 0
						if (not isConnected(matrix,C,A) and not isConnected(matrix,A,C)): 
							subgraph[7] += 1
						elif (not isConnected(matrix,C,A) and isConnected(matrix,A,C)): 
							subgraph[11] += 1
			else: #when isConnected(matrix,B, A) == 0
				secondDegreeNeighbours = np.where(matrix.iloc[B])[0]
				for C in secondDegreeNeighbours:
					if isConnected(matrix,C, B):
						if (not isConnected(matrix,C,A) and not isConnected(matrix,A,C)): 
							subgraph[3] += 1
						elif (not isConnected(matrix,C,A) and isConnected(matrix,A,C)): 
							subgraph[6] += 1
						elif (isConnected(matrix,C,A) and not isConnected(matrix,A,C)):  
							subgraph[10] += 1
					else: #when isConnected(matrix,C, B)== 0: 
						if (not isConnected(matrix,C,A) and not isConnected(matrix,A,C)): 
							subgraph[2] += 1 
						elif (not isConnected(matrix,C,A) and isConnected(matrix,A,C)): 
							subgraph[5] += 1
						elif (isConnected(matrix,C,A) and not isConnected(matrix,A,C)):  
							subgraph[9] += 1	 	 
				incomingNodes = np.where(matrix[B])[0].tolist()
				incomingNodes.remove(A)#A is an incoming node of B, but C has to be different than A 
				for C in incomingNodes: 
					if (not isConnected(matrix,B, C) and not isConnected(matrix,A,C) and not isConnected(matrix,C,A)): 
						subgraph[1] += 1  
				secondDegreeNeighbours = np.where(matrix.iloc[A])[0].tolist()
				secondDegreeNeighbours.remove(B) #B is a neighbor of A, but C has to be different than B
				for C in secondDegreeNeighbours:
					if (not isConnected(matrix,C,A) and not isConnected(matrix,B,C) and not isConnected(matrix,C,B)):  
						subgraph[4] += 1

	#some subgraphs are symmetric and, therefore, counted more than once
	subgraph /= np.array([1,2,1,1,2,1,2,1,2,3,1,2,1,6])

	if is_absolute_output:
		return subgraph[1:].astype("int").tolist()
	else:
		return (subgraph[1:]/sum(subgraph[1:])).tolist()


if __name__ == '__main__':

	if len(sys.argv) < 3: 
		sys.exit("Input format is wrong. Missing arguments.")

	option = sys.argv[1]
	if option == "-a": 
		is_absolute_output = True
	elif option == "-r": 
		is_absolute_output = False
	else: 
		sys.exit("Input format is wrong. Expecting -a or -r")

	network_file = sys.argv[2]
	values = extract_subgraphs(network_file,is_absolute_output)
	print(values)