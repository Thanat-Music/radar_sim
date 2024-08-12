import math
import numpy as np

def intersec2Circle(x1,y1,r1,x2,y2,r2):
    # soltion at https://www.desmos.com/calculator/rpqz6q10eb
    c1 = np.array([x1,y1])
    c2 = np.array([x2,y2])
    v = c2-c1
    d = np.linalg.norm(v)
    if d > r1 + r2 or d < abs(r1 - r2):
        return None, None
    ux = v/d
    uy = np.array([ux[1], -ux[0]])
    xvec = ((d**2)-(r2**2)+(r1**2))/2/d
    yvec = math.sqrt(r2**2-(d-xvec)**2)
    return c1+ux*xvec+uy*yvec,c1+ux*xvec-uy*yvec

def distance(posA, posB):
    return np.linalg.norm(posA - posB)

class Env:
    def __init__(self, time_step=0.001,size = np.array([200,200])):
        self.obj_dict = {}
        self.time_step = time_step
        self.time = 0.0
        self.id_number = 0
        self.map_size = size
        self.map_conner = [size/2,-size/2]

    def set_object(self, position, obj_type, direction=np.array([1, 0]), speed=0, radius = 1.):
        if obj_type == "radar":
            obj = Radar(self.id_number, position,direction, speed)
        elif obj_type == "photon":
            obj = Photon(self.id_number, self.time, position, direction, speed)
        else:
            obj = Object(self.id_number, position, direction, speed, radius)
        self.obj_dict[self.id_number] = obj
        print(f"Object {self.id_number} added: {obj_type}")
        self.id_number += 1

    def remove_object(self, obj_id):
        if obj_id in self.obj_dict:
            del self.obj_dict[obj_id]
            print(f"Object {obj_id} removed")
        else:
            print(f"Object {obj_id} not found")
            
    def in_map(self,pos):
        return (pos<=self.map_conner[0]).all() and (pos>=self.map_conner[1]).all()
            
    def run_step(self,step):
        for _ in range(step):
            obj_keys = list(self.obj_dict.keys())
            for obj_key in obj_keys:
                if obj_key in self.obj_dict:
                    obj = self.obj_dict[obj_key]
                    obj.update(self)
                    if not self.in_map(obj.pos): 
                        self.remove_object(obj_key)
            self.time = round(self.time + self.time_step, 6)

    def run(self, till_time, log=False):
        while self.time <= till_time:
            if log and (self.time * 10) % 1 == 0:
                print("Running....", self.time)
                        # Create a list of keys to iterate over to avoid dictionary size change errors
            obj_keys = list(self.obj_dict.keys())
            for obj_key in obj_keys:
                if obj_key in self.obj_dict:  # Check if the object still exists in the dictionary
                    self.obj_dict[obj_key].update(self)
            self.time = round(self.time + self.time_step, 6)

class Object:
    def __init__(self, ID, position=np.array([0, 0]), direction=np.array([1, 0]), speed=0,radius = .001, obj_type="obj"):
        self.id = ID
        self.type = obj_type
        self.pos = position
        self.dir = direction
        self.speed = speed
        self.velocity = speed * direction
        self.radius = radius

    def __str__(self):
        return f"id:{self.id} | type:{self.type} | position:{self.pos} | direction:({self.dir}) | velocity:{self.velocity}"

    def move(self, time):
        self.pos = self.pos + self.velocity * time

    def update(self, env):
        self.move(env.time_step)

class Radar(Object):
    def __init__(self, ID, position=np.array([0, 0]),direction = np.array([1,0]),send_speed = 100):
        super().__init__(ID=ID, position=position, direction=direction , obj_type="radar")
        self.distance = 0
        self.sendding_speed = send_speed

    # def send_photon(self, env):s
    #     env.set_object(self.pos + self.dir * .001, 'photon', direction=self.dir, speed=self.sendding_speed)
        
    def send_photons(self, env, num_directions=0.5):
        for i in range(int(178*num_directions)):
            angle = ((np.pi/180/num_directions) * (i+1)) + np.arctan2(self.dir[1],self.dir[0]) -np.pi/2
            direction = np.array([np.cos(angle), np.sin(angle)])
            env.set_object(self.pos + direction * 0.1, 'photon', direction=direction, speed=100)

    def receive_photon(self, speed, time, start_time):
        delta_time = time - start_time
        self.distance = delta_time * speed / 2 
        print(f"Photon received by {self.id}. Time: {delta_time:.4f}s, Distance: {self.distance:.4f}m.")

    def update(self, env):
        if env.time == 0.001:
            print("Sending photon....", env.time)
            self.send_photons(env)
                        # Create a list of keys to iterate over to avoid dictionary size change errors
        obj_keys = list(env.obj_dict.keys())
        for obj_key in obj_keys:
            if obj_key in env.obj_dict:  # Check if the object still exists in the dictionary
                obj = env.obj_dict[obj_key]
                if obj.type == "photon":
                    if distance(self.pos, obj.pos) <= 0.01 and (env.time-obj.time)>0.01:
                        self.receive_photon(obj.speed, env.time, obj.time)
                        env.remove_object(obj.id)

class Photon(Object):
    def __init__(self, ID, start_time, position=np.array([0, 0]), direction=np.array([1, 0]), speed=0):
        super().__init__(ID, position=position, obj_type="photon", direction=direction, speed=speed)
        self.start_pos = position
        self.time = start_time

    def collision(self, env):
        for obj in env.obj_dict.values():
            if obj.type != "photon" and distance(self.pos, obj.pos) <= self.radius+obj.radius and (env.time-self.time)>0.01:
                print("hit.....",distance(self.pos, obj.pos))
                self.velocity *= -1

    def update(self, env):
        self.move(env.time_step)
        self.collision(env)
        if not env.in_map(self.pos):
            env.remove_object(self.id)