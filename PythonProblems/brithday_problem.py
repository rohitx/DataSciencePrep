import math
import matplotlib.pyplot as plt
import matplotlib
plt.style.use('ggplot')
x = xrange(2,100)
birthday = [1-(math.factorial(365)/math.factorial(365 - k))/float(365**k) for k in x]


plt.plot(x, birthday, 'g-')
plt.ylim(0,1.05)
plt.xlabel('# of people')
plt.ylabel('Probability')
plt.show()