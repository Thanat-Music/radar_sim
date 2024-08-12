import matplotlib.animation as animation  
import matplotlib.pyplot as plt  
import numpy as np  
  
   
# creating a blank window 
# for the animation  
fig = plt.figure()  
axis = plt.axes(xlim =(-50, 50), 
                ylim =(-50, 50))  

point, = axis.plot([], [], 'ro')  
pointB, = axis.plot([], [], 'go')
   
# animation function  
def animate(i):  
    # t is a parameter which varies 
    # with the frame number 
    t = 1 * i  
       
    # x, y values to be plotted  
    x = t 
    y = t 
       
    # appending values to the previously  
    # empty x and y data holders  
 
    point.set_data([x], [y])  
    pointB.set_data([-x], [-y])  
    
      
    return point,pointB 
   
# calling the animation function      
anim = animation.FuncAnimation(fig, animate, 
                               frames = 500, interval = 200, blit = True)  
   
# # saves the animation in our desktop 
# anim.save('growingCoil.mp4', writer = 'ffmpeg', fps = 30) 
plt.show()