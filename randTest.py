import random
from time import clock, sleep

#to do: port to python 3, setup multiprocessing

'''
randTest: Algorithm that tests how many random
numbers can be produced with the random module
without repeating. Is implemented by recursive
recuTest and iterative iterTest functions.
'''

#recursive version
def recuTest(limit = None, randList = None):
	#parameter check
	if (randList == None): randList = []
	if (limit == None): limit = 100
	
	#create random number
	rand = random.randint(0, limit)

	#if in list return list length
	if (rand in randList): return len(randList)
	#if not in list add and recurse
	else: 
		randList.append(rand)
		return recuTest(limit, randList)

#iterative version		
def iterTest(limit = None, randList = None):
	#parameter check
	if (randList == None): randList = []
	if (limit == None): limit = 100
	
	#infinite loop
	while(True):
		#create random number
		rand = random.randint(0, limit)

		#if in list return list length
		if (rand in randList): return len(randList)
		#if not in list add
		else: randList.append(rand)
		
#calls randTest multiple times and collects statistics
def randStats(randTest, limit=None, sampleSize=None):
	#parameter check
	if (limit == None): limit = 100
	if (sampleSize == None): sampleSize = 100
	
	#setup
	start = clock()
	stats = []
	output = "list of tests: "
	
	#run tests and collect results
	map(lambda x: stats.append(randTest(limit)), range(sampleSize))
	output += reduce(lambda x, y: str(x) + ", " + str(y), stats)

	#calculate statistics
	stop = clock()
	average = sum(stats) / len(stats)
	statsMin = min(stats)
	statsMax = max(stats)
	time = stop - start
	
	#print results
	print(output)
	print("Average tests before repeat: " + str(average))
	print("Shortest tests before repeat: " + str(statsMin))
	print("Longest tests before repeat: " + str(statsMax))
	print("Elapsed time: " + str(time))

#runs both randTest implementations for comparison
def benchmark(limit = None, sampleSize = None):
	#parameter check
	if (limit == None): limit = 1000
	if (sampleSize == None): sampleSize = 1000
	
	#script
	print("Iterative version")
	randStats(iterTest, limit, sampleSize)
	sleep(3)
	print("\n\n\n\n")
	print("Recursive version")
	randStats(recuTest, limit, sampleSize)

#run
benchmark()
