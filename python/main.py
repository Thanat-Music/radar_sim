import python.Envi as Envi
import numpy as np
import matplotlib.animation as animation  
import matplotlib.pyplot as plt  

env = Envi.Env(time_step=0.0001)
env.set_object(position=np.array([0.0, 0.0]),direction=np.array([.0,1.0]), obj_type="radar",speed=500)
env.set_object(position=np.array([10.0, 0.0]),direction=np.array([.0,1.0]), obj_type="radar",speed=500)
env.set_object(position=np.array([-10.0, 0.0]),direction=np.array([.0,1.0]), obj_type="radar",speed=500)
# env.set_object(position=np.array([10.0, 0.0]), obj_type="radar",speed=1000)
env.set_object(position=np.array([0.0, 85.0]), obj_type="obj",radius = 5.)

# env.run(2, log=True)


fig = plt.figure()  
axis = plt.axes(xlim =(env.map_conner[1][0]-5, env.map_conner[0][0]+5), 
                ylim =(env.map_conner[1][1]-5, env.map_conner[0][1]+5))  
radar_posi, = axis.plot([], [], 'ro')  
photon_posi, = axis.plot([], [], 'bo')  
object_posi, = axis.plot([], [], 'go')  

# Visualization with Matplotlib
def animate(i):
    env.run_step(100)
    radar_positions = [obj.pos for obj in env.obj_dict.values() if obj.type == "radar"]
    photon_positions = [obj.pos for obj in env.obj_dict.values() if obj.type == "photon"]
    object_positions = [obj.pos for obj in env.obj_dict.values() if obj.type == "obj"]   

    radar_posi.set_data([pos[0] for pos in radar_positions], [pos[1] for pos in radar_positions])  
    photon_posi.set_data([pos[0] for pos in photon_positions], [pos[1] for pos in photon_positions])  
    object_posi.set_data([pos[0] for pos in object_positions], [pos[1] for pos in object_positions])  
    
    return radar_posi,photon_posi,object_posi 

# calling the animation function      
anim = animation.FuncAnimation(fig, animate, frames = 500, interval = 1, blit = False)  
   
# # saves the animation in our desktop 
# anim.save('growingCoil.mp4', writer = 'ffmpeg', fps = 30) 
plt.show()
    
    
