#Mermaid API
#This program works with the following foundation of mathemetical notions:
#1. Sets
#2. Sequences and Tuples
#3. Functions and Relations
#4. Graphs
#5. Strings and Languages
#6. Boolean Logic
#################
# Developer: Jason Banks
# Development Date - 4/9/2017
#################


import sys
import os.path

print("Welcome to Mermaid!")
print("This program works with mathematical terms.")

option = sys.argv[1]
dataset = sys.argv[2]
dataset_stack = []
count = 1
ss_count = 0
ms_count = 0
result = []
check_list = []
dataset_list = []
line_list = []
ms_flag = 0
prop_count = 0
result_cache = ""

filename = 'mermaid.txt'

if option == '-set':
	print("We're now adding your new set to the system.")
	print("Elements: " + dataset)
	dataset_split = dataset.split(",")
	for element in dataset_split:
		print("Element #" + str(count) + ": " + element)
		count += 1

	if not os.path.exists(filename):
		with open(filename, 'w') as f:
			f.write("set," + dataset + "\n")
			
	else:
		if os.path.exists(filename):	
			with open(filename, 'a') as f:
				f.write("set," + dataset + "\n")

	print("Your set has been added.")
else:
	if option == '-prop':
		print ("Set Analysis:")
		for dataset_item in dataset.split(","):
			dataset_stack.append(dataset_item)
		#Proper Subsets
		with open(filename) as f_obj:
			for line in f_obj:
				for element in dataset.split(","):
					dataset_list.append(element)
					for line_element in line.split(","):
						line_list.append(line_element)
						if line_element.strip() == element and line_element.strip() != 'set' and result_cache != element:
							result.append(element)
							result_cache = element
						else:
							continue
					result_cache = ""
				print("Result: " + str(result))
				print("-----")
				if len(result) == len(dataset_stack):
					print(dataset + " is a proper subset of " + line[4:])
				result = []
		#List all sets
	if option == '-list':
		with open(filename) as f_obj_ms:
			for line_ms in f_obj_ms:
				print(line_ms)