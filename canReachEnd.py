# kimm@mssm.org
# Minkyu Kim

import timeit

"""
For an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.
[2,2,0,2,4] -> Yes
[3,2,1,0,4] -> No
[5] -> Yes
"""

####################################################

"""
Naive implementation without memoization.
"""
def canReachEnd1(iList, init=0):
	if(init >= len(iList)-1):
		return True
	if(iList[init] == 0):
		return False

	#rint(init)
	for i in range(1, iList[init]+1):
		result = canReachEnd1(iList, init+i)
		if result: return True

	return False

####################################################

"""
Implementation with memoization, but using additional function attribute for cache
"""
def _canReachEnd(iList, init=0):
	if(init >= len(iList)-1):
		return True
	if(iList[init] == 0):
		return False

	#rint(init)
	for i in range(1, iList[init]+1):
		result = canReachEnd2(iList, init+i)
		if result: return True

	return False

def canReachEnd2(iList, init=0):
	if init not in canReachEnd2.cache.keys():
		canReachEnd2.cache[init] = _canReachEnd(iList, init)
	return canReachEnd2.cache[init]

####################################################
"""
Implementation with memoization; No global cache required.
"""

class Memoize(object):
	def __init__(self, f):
		self.f = f;
		self.cache = {}
	def __call__(self, l, *args):
		if args in self.cache:
			return self.cache[args]

		result = self.f(l, *args)
		self.cache[args] = result
		return result

@Memoize
def canReachEnd3(iList, init=0):
	if(init >= len(iList)-1):
		return True
	if(iList[init] == 0):
		return False

	for i in range(1,iList[init]+1):
		result = canReachEnd3(iList, init+i)
		if result: 
			return True

	return False

####################################################
"""
Fast Implementation by checking reachability up to index i ~ up to last index in O(n) runtime.
(DP-approach)
"""
def canReachEnd4(iList):
	max_jump = 0
	max_index = len(iList)-1

	#check if index i can be reached.
	for i, elem in enumerate(iList):
		if(max_jump < i): return False
		max_jump = max(max_jump, i+elem)
		
	#passing through i=len(iList)-1 means that last index can be reached.
	return True

"""
Testing & Timing
"""
####################################################
def test_canReachEnd_impl(f, memoization=True):
	test_input = [[2,2,0,2,4],[3,2,1,0,4],[5]]
	test_output = [True, False, True]
	for index, xl in enumerate(test_input):
		if(memoization): f.cache = {}
		if not (f(xl) == test_output[index]):
			print('test failed... on {0} should be {1} on {2}'.format(xl, test_output[index], f.__name__))
			return

	print('ALL TEST PASSED!')

def testAll_canReachEnd():
	test_canReachEnd_impl(canReachEnd1, memoization=False)
	test_canReachEnd_impl(canReachEnd2)
	test_canReachEnd_impl(canReachEnd3)
	test_canReachEnd_impl(canReachEnd4, memoization=False)
	print('\n')

def time_canReachEnd_impl(f, rep=3):
	f.cache = {}
	myTimer = timeit.Timer(lambda: f([2,2,0,2,4]))
	time_list = myTimer.repeat(number=1000, repeat=rep)
	avg_time = 1.0*sum(time_list)/len(time_list)

	try: 
		print('Testing {0}'.format(f.__name__))
	except AttributeError:
		print('Testing Memoized Function')


	print('Out of {0} repeats, '.format(rep))
	print(' Worst runtime was {0}. \n Best runtime was {1}.'.format(round(time_list[0],10), round(time_list[-1],10)))
	print('  Average runtime was {0}.'.format(round(avg_time,10)))
	print('\n')
	
	return avg_time

def timeAll_canReachEnd():
	avg1 = time_canReachEnd_impl(canReachEnd1, rep=5)
	
	avg2 = time_canReachEnd_impl(canReachEnd2, rep=5)
	avg3 = time_canReachEnd_impl(canReachEnd3, rep=5)
	avg4 = time_canReachEnd_impl(canReachEnd4, rep=5)
	print('Memoization added x{0} boost in performance on average to a base-line.'.format(round(avg1*1.0/avg3,1)))
	print('Just checking reachability in O(n) was x{0} boost in performance on average to a base-line.'.format(round(avg1*1.0/avg4,1)))

if __name__ == '__main__':
	testAll_canReachEnd()
	timeAll_canReachEnd()