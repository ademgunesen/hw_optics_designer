import json
from high_level_objects import *

def save_json(obj_list):
    optic_design ={
        "version": 2,
        "objs": obj_list,
        "mode": "light",
        "rayDensity_light": 0.5,
        "rayDensity_images": 1,
        "observer": "null",
        "origin": {
            "x": 40,
            "y": 200
        },
        "scale": 0.7
    }
    with open("optic_design3" + '.json','w') as json_file:
        json.dump(optic_design, json_file, indent = 4)
        
def calculate_light_pos(eye, o_lens):#lens eq -> 1/f=1/o+1/h
    if(eye.y == o_lens.y):
        pupil_x=eye.x+200
        work_dist = o_lens.x-pupil_x
        ring_dist = 1/(1/o_lens.f - 1/work_dist)
        ring_x = o_lens.x + ring_dist
        ring_r = ring_dist*eye.pup/(2*work_dist)
        return ring_x, o_lens.y, ring_r
    else:
        print("Eye and the lens are not in a straight line")

def calculate_m12_lens(o_lens, camera):
    aerial_img_x = o_lens.x + o_lens.f
    img_dist = camera.x-300 - aerial_img_x
    sensor_dist = camera.x - (camera.x-300) - 100
    f = 1/(1/img_dist + 1/sensor_dist)
    return f

      
def obj_to_json(obj_list):
    obj_json = []
    for i in obj_list:
        obj_json += i.get_obj()
    return obj_json

def diopter_to_mm(diopter):
    mm=(1/diopter)*1000
    return mm

def diopter_to_r(diopter):
    if diopter == 20:
        return 250
    elif diopter == 40 : 
        return 200
    elif diopter == 60:
        return 143
    elif diopter == 90:
        return 130
    else:
        print("Unknown lens")

def generate_model(x=0,y=0,diopter=40, work_dist=260):  
    h_eye = eye(x,y,40)
    
    o_lens_f = 10*diopter_to_mm(diopter)
    o_lens_r = diopter_to_r(diopter)
    o_lens = lens(h_eye.x+200+work_dist,0,o_lens_r,o_lens_f)
    
    light_x, light_y, light_r = calculate_light_pos(h_eye, o_lens)
    ring = ring_light(light_x, light_y, light_r)
    
    camera = cam(light_x+160,light_y)
    f = calculate_m12_lens(o_lens, camera)
    cam_lens = m12_lens(light_x-140,light_y,f)
    camera.set_lens(cam_lens)
    
    rul = ruler(0,300,2000,300)
    obj_list=[h_eye,o_lens,ring,camera,rul]
    return obj_list

obj_list = generate_model(diopter=40, work_dist=300)
obj_json = obj_to_json(obj_list)
save_json(obj_json)