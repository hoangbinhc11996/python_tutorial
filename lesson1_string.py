message = "Hello World"

print(message[7:])
print(message.find('o'))

new_message = message.replace('World', 'Universe')

print(new_message)

greeting = 'Hello'
name ='Michael'
print(greeting + " \
	" + name)

#string format

person = {'name': 'Hoang', 'age': 23}

sentence = 'My name is {0} and I am {1} years old.' \
	.format(person['name'], person['age'])

print sentence

person2 = {'name': 'Thao', 'age': 21}

sentence = 'My name is {0[name]} and I am {0[age]} years old.' \
	.format(person2)

print sentence

for i in range(1, 11):
	sentence = 'The value is {:03}'.format(i)
	print sentence


pi = 3.14159265

sentence = 'Pi is equal to {:.4f}'.format(pi)
print sentence

sentence = '1 MB is equal to {:,.2f} bytes'.format(1000**2)
print sentence

import datetime

my_data = datetime.datetime(2016, 9, 24, 12, 30, 45)
sentence = '{:%B %d, %Y}'.format(my_data)
print sentence


