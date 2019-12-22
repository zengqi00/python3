
from matplotlib import pyplot as plt
import random
x = range(120)
y = [random.randint(20,30) for i in range(120)]

plt.figure(figsize=(20,8),dpi=80)

plt.plot(x,y)


#调整x轴的刻度
_x = x
_xticks = ["hello.{}".format(i) for i in _x]
plt.xticks(_x,_xticks)
plt.yticks()

plt.show()