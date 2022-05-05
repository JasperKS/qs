#Q1
def minimumRounds(tasks):
	#Dictionary to store the frequency of each task
	tasks_freq = {}

	#Counter for the number of rounds
	rounds = 0;

	#Counts the fequency of each tasks store in the dict
	for task in tasks:
		if task in tasks_freq:
			tasks_freq[task] += 1
		else:
			tasks_freq[task] = 1


	#Loop through each task and greedily find the min number of rounds required
	for task in tasks_freq:
		#Case where the frequncy of a task is only 1, return -1
		if tasks_freq[task] == 1:
			return -1
		else:
			#Group the tasks by 3
			rounds += tasks_freq[task] // 3

			"""If the freq of the task is not divisbile by 3 then it must be grouped
			into two rounds 2 and 2, hence + 1 round"""
			if tasks_freq[task] % 3 != 0:
				rounds += 1

	return rounds


#Q2
def threeBuildings(s):
	
	#Dictionary to keep track of the buildings as we go through them
	combi = {"0": 0, "1": 0, "01": 0, "10": 0, "010": 0, "101": 0}

	#Loop through the buildings and increment the possible combinations accordingly
	for ch in s:

		#If the current building is 0 then we need to increment
		#"0", "10". and "010"
		if ch == "0":
			combi["0"] += 1
			combi["10"] += combi["1"]
			combi["010"] += combi["01"]

		#If the current building is 1 then we need to increment
		#"1", "01". and "101"
		if ch == "1":
			combi["1"] += 1
			combi["01"] += combi["0"]
			combi["101"] += combi["10"]

	#Combine the possible "010" and "101" counts
	return combi["010"] + combi["101"]


if __name__ == "__main__":
	#Q1 Tests
	assert(minimumRounds([2,2,3,3,2,4,4,4,4,4]) == 4)
	assert(minimumRounds([2,3,3]) ==  -1)
	assert(minimumRounds([2]) ==  -1)
	assert(minimumRounds([3,3,3,3]) == 2)

	#Q2 Tests
	assert(threeBuildings("010") == 1)
	assert(threeBuildings("101") == 1)
	assert(threeBuildings("001101") == 6)
	assert(threeBuildings("11100") == 0)



