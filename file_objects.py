
# with open('test.txt', 'w') as f:

# 	# for line in f:
# 	# 	print(line)

# 	# f_contents = f.readline()
# 	# print(f_contents)

# 	# f_contents = f.readline()
# 	# print(f_contents)

# 	# f_contents = f.read(10)
# 	# print(f_contents)

# 	# f_contents = f.read(10)
# 	# print(f_contents)

# 	# size_to_read = 1
# 	# f_contents = f.read(size_to_read)
# 	# while len(f_contents):
# 	# 	print(f_contents)
# 	# 	f_contents = f.read(size_to_read)

# 	# size_to_read = 10
# 	# f_contents = f.read(size_to_read)
# 	# print(f.tell())

# 	f.write('Test')
# 	f.seek(0)
# 	f.write('Test')



with open('test.txt', 'r') as rf:
	with open('test_copy.txt', 'w') as wf:
		for line in rf:
			wf.write(line)
