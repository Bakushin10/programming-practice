def topologicalSort(jobs, deps):
	from collections import defaultdict
	
	pendingJob = defaultdict(list)
	
	for first, scnd in deps:
		pendingJob[scnd].append(first)
		if scnd in jobs:
			jobs.remove(scnd)
	
	ans = []
	while jobs:
		jobToFinish = jobs.pop()
		ans.append(jobToFinish)
		emptyJob = []
		for key, values in pendingJob.items():
			if jobToFinish in values:
				values.remove(jobToFinish)
			if len(pendingJob[key]) == 0:
				emptyJob.append(key)
				jobs.append(key)
		
		for i in emptyJob:
			del pendingJob[key]
	return ans

jobs = [1, 2, 3, 4]
deps = [[1, 2], [1, 3], [3, 2], [4, 2], [4, 3]]

jobs = [1, 2, 3, 4, 5]
deps = [[1, 4], [5, 2]]
print(topologicalSort(jobs, deps))
