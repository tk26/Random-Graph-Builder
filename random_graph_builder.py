# Author: Tejas K
# Generates a random graph of friends
# Run from shell: python random_graph_builder.py <NumberOfPeople>
# See output file: myfriends_tk.txt
# More: Lower the range of k to get a thinner web
import random
import sys
pool = int(sys.argv[1])
target = []
friends = []
output = ""
for i in range(0, pool):
	i = []
	friends.append(i)

for i in range(0, pool):
	# i has k friends
	k = random.randrange(0, pool)
	target.append(i)
	for j in range(0, k):
		# generate a friend f for i
		f = random.randrange(0, pool)
		if f not in friends[i] and f != i and i not in friends[f]:
			friends[i].append(f)

for i in range(0, len(friends)):
	if len(friends[i]) > 0:
		output += chr(i+97)
		for j in friends[i]:
			output += " "
			output += chr(j+97)
		output += "\n"

text_file = open("myfriends_tk.txt", "w")
text_file.write(output)
text_file.close()
