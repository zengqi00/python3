#coding = utf-8

from matplotlib import pyplot as plt


x = range(2,26,2)
y = [14,12,14,5,14,15,17,23,24,25,26,27]

#设置图片大小
plt.figure(figsize=(20,8),dpi=80)
#绘图
plt.plot(x,y)

#设置x轴的刻度
_xtick_labels = [i for i in range(2,25)]
plt.xticks(_xtick_labels[::3])
plt.yticks(range(2,30,2))
#保存
plt.savefig('./sig.png')
#展示
plt.show()
