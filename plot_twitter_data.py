import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

style.use('ggplot')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

# method to read the tweets.txt file and generate a line graph by analyzing the sentiments
def animate(i):
	pull_data = open('tweets.txt','r',encoding='utf-8').read()
	lines = pull_data.split('\n')
	xs = []
	ys = []

	x=0
	y=0

	for line in lines:
		x+=1
		if "pos" in line:
			y+=1
		elif "neg" in line:
			y-=0.3
		xs.append(float(x))
		ys.append(float(y))
	ax1.clear()
	ax1.plot(xs, ys)
# Create a live line graph using animation
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()