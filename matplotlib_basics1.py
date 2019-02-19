#!/usr/local/bin/python3

print ("Numpy Processing")

import sys
print (sys.path)

# Import the necessary packages and modules
import matplotlib.pyplot as plt
import numpy as np



# ===========================
# Plot - Linear
# ===========================

# Prepare the data
x = np.linspace(0, 10, 100)

# Plot the data
plt.plot(x, x, label='linear')

# Add a legend
plt.legend()

# Set the style to `ggplot`
# plt.style.use("ggplot")

# Show the plot
# plt.show()
plt.savefig("output/mpl_linear1.png", transparent=True)


# ===========================
# Plot - Scatter
# ===========================

fig = plt.figure()
ax = fig.add_subplot(111)

plt.title("Scatter Plot") 

ax.plot([1, 2, 3, 4], [10, 20, 25, 30], color='lightblue', linewidth=3)
ax.scatter([0.3, 3.8, 1.2, 2.5], [11, 25, 9, 26], color='darkgreen', marker='^')
ax.set_xlim(0.5, 4.5)

#plt.show()
plt.savefig("output/mpl_scatter1.png", transparent=True)





# ===========================
# Plot - Subplots
# ===========================

# Initialize the plot
#fig = plt.figure()
#ax1 = fig.add_subplot(131)
#ax2 = fig.add_subplot(132)
#ax3 = fig.add_subplot(133)

# Plot the data
#ax1.bar([1,2,3],[3,4,5])
#ax2.barh([0.5,1,2.5],[0,1,2])
#ax2.axhline(0.45)
#ax1.axvline(0.65)
#ax3.scatter(x,y)

# Show the plot
# plt.show()




# ==========================
# Plot - Sine Plot
# ==========================

# Compute the x and y coordinates for points on a sine curve 
x = np.arange(0, 3 * np.pi, 0.1) 
y = np.sin(x) 
plt.title("Sine wave form") 

# Plot the points using matplotlib 
plt.plot(x, y) 
# plt.show() 
plt.savefig("output/mpl_sine1.png", transparent=True)



# ==========================
# Plot - Bar
# ==========================

# Initialize the plot
fig = plt.figure(figsize=(20,10))
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

# or replace the three lines of code above by the following line: 
#fig, (ax1, ax2) = plt.subplots(1,2, figsize=(20,10))

# Plot the data
ax1.bar([1,2,3],[3,4,5])
ax2.barh([0.5,1,2.5],[0,1,2])

plt.legend()

# Show the plot
# plt.show()
plt.savefig("output/mpl_bar1.png", transparent=True)



# ==========================
# Plot - Polar
# ==========================

#plt.axes([0,0,1,1])

#N = 20
#theta = np.arange(0.0, 2*np.pi, 2*np.pi/N)
#radii = 10*np.random.rand(N)
#width = np.pi/4*np.random.rand(N)
#bars = plt.bar(theta, radii, width=width, bottom=0.0)

#for r,bar in zip(radii, bars):
#    bar.set_facecolor( cm.jet(r/10.))
#    bar.set_alpha(0.5)

#plt.show()
#plt.savefig("output/mpl_polar1.png", transparent=True)



# =========================
# Multi Plots
# =========================
plt.subplot(2,2,1)
plt.subplot(2,2,3)
plt.subplot(2,2,4)

#plt.show()
plt.savefig("output/mpl_multi1.png", transparent=True)


# Bar Charts
# ==========================
n = 12
X = np.arange(n)
Y1 = (1-X/float(n)) * np.random.uniform(0.5,1.0,n)
Y2 = (1-X/float(n)) * np.random.uniform(0.5,1.0,n)

plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='white')

for x,y in zip(X,Y1):
    plt.text(x+0.4, y+0.05, '%.2f' % y, ha='center', va= 'bottom')

plt.ylim(-1.25,+1.25)
#plt.show()
plt.savefig("output/mpl_barcharts1.png", transparent=True)

# Contours
# ==================

def f(x,y): return (1-x/2+x**5+y**3)*np.exp(-x**2-y**2)

n = 256
x = np.linspace(-3,3,n)
y = np.linspace(-3,3,n)
X,Y = np.meshgrid(x,y)

plt.contourf(X, Y, f(X,Y), 8, alpha=.75, cmap='jet')
C = plt.contour(X, Y, f(X,Y), 8, colors='black', linewidth=.5)
# plt.show()
plt.savefig("output/mpl_contours1.png", transparent=True)


