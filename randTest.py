from random import randint
from time import process_time
#from multiprocessing import Pool, cpu_count

#to do: figure out multiprocessing timing

"""
randTest: Algorithm that tests how many random
numbers can be produced with the random module
without repeating.
"""

#recursive version
def recuTest(limit = None, randList = None):
        #parameter check
        if (randList == None): randList = []
        if (limit == None): limit = 100
        
        #create random number
        rand = randint(0, limit)

        #if in list return list length
        if (rand in randList):
                return len(randList)
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
                rand = randint(0, limit)

                #if in list return list length
                if (rand in randList):
                        return len(randList)
                #if not in list add
                else: randList.append(rand)


#calls randTest multiple times and collects statistics
def randStats(limit=None, sampleSize=None):
        #parameter check
        if (limit == None): limit = 100
        if (sampleSize == None): sampleSize = 10000
        
        #setup
        stats = [limit] * int(sampleSize / 2)
        #pool = Pool(cpu_count())

        #run tests and time them        
        
        iterStart = process_time()
        iterList = list(map(iterTest, stats))
        iterTime = process_time() - iterStart

        recuStart = process_time()
        recuList = list(map(recuTest, stats))
        recuTime = process_time() - recuStart

        #calculate statistics
        stats =  iterList + recuList
        average = sum(stats) / len(stats)
        statsMin = min(stats)
        statsMax = max(stats)
        
        #print results
        print("Number of tests: " + str(len(stats)))
        print("Average tests before repeat: " + str(average))
        print("Shortest tests before repeat: " + str(statsMin))
        print("Longest tests before repeat: " + str(statsMax))
        print("Iterative time: %.9f seconds" % iterTime)
        print("Recursive time: %.9f seconds" % recuTime)
        
#script
randStats()
