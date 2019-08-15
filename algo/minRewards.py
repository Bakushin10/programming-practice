"""
https://www.algoexpert.io/questions/Min%20Rewards

import program
import unittest


class TestProgram(unittest.TestCase):
	
	def test_case_1(self):
		self.assertEqual(program.minRewards([1]), 1)
	
	def test_case_2(self):
		self.assertEqual(program.minRewards([5, 10]), 3)
	
	def test_case_3(self):
		self.assertEqual(program.minRewards([10, 5]), 3)

	def test_case_4(self):
		self.assertEqual(program.minRewards([4, 2, 1, 3]), 8)
	
	def test_case_5(self):
		self.assertEqual(program.minRewards([0, 4, 2, 1, 3]), 9)
	
	def test_case_6(self):
		self.assertEqual(program.minRewards([8, 4, 2, 1, 3, 6, 7, 9, 5]), 25)
	
	def test_case_7(self):
		self.assertEqual(program.minRewards([2, 20, 13, 12, 11, 8, 4, 3, 1, 5, 6, 7, 9, 0]), 52)
	
	def test_case_8(self):
		self.assertEqual(program.minRewards([2, 1, 4, 3, 6, 5, 8, 7, 10, 9]), 15)
	
	def test_case_9(self):
		self.assertEqual(program.minRewards([800, 400, 20, 10, 30, 60, 70, 90, 17, 21, 22, 13, 12, 11, 8, 4, 2, 1, 3, 6, 7, 9, 0, 68, 55, 67, 57, 60, 51, 661, 50, 65, 53]), 93)
	

if __name__ == "__main__":
	unittest.main()


1. all students must at least get one point
2. student next to each other (immediately right and left) with lower score must recieve lower score and higher score must recieve higher score. 

what is the mim total score
"""
def minRewards(scores):
    L = len(scores)
    right, left = [0]*L, [0]*L
    rewards = 0

    for i in range(1, L):
        if scores[i] > scores[i-1]:
            left[i] = left[i-1] + 1
    
    for i in range(L-2, -1, -1):
        if scores[i] > scores[i+1]:
            right[i] = right[i+1] + 1

    for i in range(L):
        reward = max(right[i], left[i]) + 1
        rewards += reward
    
    return rewards


rewards = [4, 2, 1, 3]
print(minRewards(rewards))
