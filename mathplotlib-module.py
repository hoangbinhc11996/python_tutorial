import matplotlib.pyplot as plt
# plt.plot([1, 2, 3, 4])
# plt.ylabel('some numbers')
# plt.show()

# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
# plt.axis([0, 6, 0, 20])
# plt.ylabel('numbers')
# plt.xlabel('numbers')
# plt.show()

import numpy as np

# t = np.arange(0., 5., 0.2)

# plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
# plt.show()

# data = {'a': np.arange(50), \
# 		'c': np.random.randint(0, 50, 50), \
# 		'd': np.random.randn(50)}
# data['b'] = data['a'] + 10 * np.random.randn(50)
# data['d'] = np.abs(data['d']) * 100

# plt.scatter('a', 'b', c = 'c', s = 'd', data = data)
# plt.xlabel('entry a')
# plt.ylabel('entry b')
# plt.show()



# names = ['group_a', 32, 54]
# values = [1, 10, 100]

# plt.figure(1, figsize=(9, 3))

# plt.subplot(131)
# plt.bar(names, values)
# plt.subplot(132)
# plt.bar(['group_a', 'group_b', 'group_c'], [1, 10, 100])
# plt.subplot(133)
# plt.plot(names, values)
# plt.suptitle('Categorical Plotting')
# plt.show()

# def f(t):
# 	return np.exp(-t) * np.cos(2*np.pi*t)

# t1 = np.arange(0.0, 5.0, 0.1)
# t2 = np.arange(0.0, 5.0, 0.02)

# plt.figure(1)
# plt.subplot(211)
# plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

# plt.subplot(212)
# plt.plot(t2, np.cos(2*np.pi*t2), 'r--')

# plt.show()

mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

# the histogram of the data
n, bins, patches = plt.hist(x, 50, facecolor='g', alpha=0.75)


plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()