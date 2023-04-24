"""
Implement Conway’s Game of Life in Python.
Perform 50 iterations as follows:
a) Print the current status. (Instead of ’X’ and ’O’ you could also print ANSI escape sequences
like ’\033[0;41m \033[0m’ and ’\033[0;47m \033[0m’.
b) Wait one second (time.sleep(1)).
c) Use a function nextgen to compute the next generation.
"""

import argparse, random, copy, time

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('-x', dest='x', required= False)
	parser.add_argument('-y', dest='y', required= False)
	args = parser.parse_args()
	
	current = []

	if args.x and args.y :
		x, y = int(args.x),int(args.y)
	else:
		#Fixed First generations of size 10 * 10
		current = [ [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
					[ 0, 0, 0, 1, 1, 0, 0, 0, 0, 0 ],
					[ 0, 0, 0, 0, 1, 1, 1, 0, 0, 0 ],
					[ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
					[ 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
					[ 0, 0, 0, 1, 1, 0, 0, 0, 0, 0 ],
					[ 0, 0, 1, 1, 0, 0, 0, 0, 0, 0 ],
					[ 0, 0, 0, 0, 0, 1, 0, 0, 0, 0 ],
					[ 0, 0, 0, 0, 1, 0, 0, 0, 0, 0 ],
					[ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ] ]

	# create a first generation
	if not current :
		for j in range(y):
			row = []
			for i in range(x):
				if random.random()<=0.2:
					row.append(1) # Adding live cells with prob of 0.2
				else :
					row.append(0) # Adding dead cells
			current.append(row)

	#Performing 50 Iterations
	for k in range(50) :
		print('Generation : ', k+1)
		printGen(current)
		time.sleep(1)
		current = nextGen(current)
	
#printing generation
def printGen(gen):
	for i in range(len(gen)):
		for j in range(len(gen[i])):
			print('X' if gen[i][j] else 'O', end='')
			#’X’ for live cells and ’O’ for dead cells
		print()

#calculating next generation with current generation
def nextGen(old):
	new = copy.deepcopy(old)
	x = len(old)
	for i in range(x):
		y = len(old[i])
		for j in range(y):
			totNeighbors = int((old[i][(j-1)%y] + old[(i-1)%x][(j-1)%y] + 
								old[(i+1)%x][(j-1)%y] +
								old[i][(j+1)%y] + old[(i-1)%x][(j+1)%y] + 
								old[(i+1)%x][(j+1)%y] +
								old[(i-1)%x][j] + old[(i+1)%x][j])) 
			# Game rules
			if old[i][j]:
				if totNeighbors  < 2 or totNeighbors > 3:
					new[i][j] = 0
			else:
				if totNeighbors == 3:
					new[i][j] = 1
	return new

if __name__ == '__main__':
    main()

#Krutarth Trivedi
#2130962