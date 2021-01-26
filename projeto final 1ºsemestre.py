import time
import math
import pygame
import math



from quaternion import Quaternion
from scene import Scene
from object3d import Object3d
from camera import Camera
from mesh import Mesh
from material import Material
from color import Color
from vector3 import Vector3


def  mesh_cylinder (numSides=40, radius=3, mesh=None):

   
    if mesh is None:
        mesh = Mesh("mesh1")
    
    vertices_bot = []
    vertices_top = []
    
    for n in range(numSides):    
        vertices_bot.append(Vector3(radius * math.cos(n*(2 * math.pi / numSides)), 0, radius * math.sin(n*(2 * math.pi / numSides))))
        
        
        vertices_top.append(Vector3(radius * math.cos(n*(2 * math.pi / numSides)), 9, radius * math.sin(n*(2 * math.pi / numSides))))
    
    

    v=0
    

    for vertex in vertices_bot:
        
        if v>=1:
            
            Mesh.create_tri(vertices_bot[v-1], Vector3(0, 0, 0), vertex, mesh)

        v=v+1

    
    Mesh.create_tri(vertices_bot[v-1], Vector3(0, 0, 0), vertices_bot[0], mesh)
    
    
    
    v = 0
    

    

    for vertex in vertices_top:
        
        if v >= 1:
            
            Mesh.create_tri(vertices_top[v-1], Vector3( vertices_bot[v].x, vertices_bot[v].y,  vertices_bot[v].z), vertex, mesh)

        v = v + 1

    
    Mesh.create_tri(vertices_top[v-1], Vector3(vertices_bot[v-1].x, vertices_bot[v-1].y,  vertices_bot[v-1].z), vertices_top[0], mesh)

    


    
    mesh.polygons.append(vertices_top)

    
    return mesh
    


def main():
    pygame.init()

    (r_x, r_y) = (720 , 580)


    w_open = pygame.display.set_mode((r_x, r_y))



    scene = Scene("Cena")
    scene.camera = Camera(False, r_x, r_y)


    scene.camera.position -= Vector3 (0, 0, 10)


    w_open_bool = True

    
    

    

    obj1 = Object3d("cylinder")
    obj1.scale = Vector3(1,1,1)
    obj1.position = Vector3 (0,0,0)
    obj1.mesh = mesh_cylinder()
    obj1.material = Material(Color(0,0.7,0.7,1),"colour1")
    scene.add_object(obj1)
    
    
    
    
            
      
            
    while w_open:  
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:

                    return    

                if event.key == pygame.K_DOWN:
                    obj1.rotation*=Quaternion.AngleAxis(Vector3(1,0,0),0.1)  
                
                if event.key == pygame.K_UP:
                    obj1.rotation*=Quaternion.AngleAxis(Vector3(1,0,0),-0.1)  
                
                if event.key == pygame.K_RIGHT:
                    obj1.rotation*=Quaternion.AngleAxis(Vector3(0,1,0),0.1)  
                
                if event.key == pygame.K_LEFT:
                    obj1.rotation*=Quaternion.AngleAxis(Vector3(0,1,0),-0.1)  
                
                if event.key == pygame.K_PAGEUP:
                    obj1.rotation*=Quaternion.AngleAxis(Vector3(0,0,1),0.1)  
                
                if event.key == pygame.K_PAGEDOWN:
                    obj1.rotation*=Quaternion.AngleAxis(Vector3(0,0,1),-0.1)  
                
                if event.key == pygame.K_w:
                    obj1.position+=Vector3(0,1,0)
                
                if event.key == pygame.K_s:
                    obj1.position+=Vector3(0,-1,0)
                
                if event.key == pygame.K_a:
                    obj1.position+=Vector3(1,0,0)
                
                if event.key == pygame.K_d:
                    obj1.position+=Vector3(-1,0,0)
                    
                if event.key == pygame.K_q:
                    obj1.position+=Vector3(0,0,1)
                    
                if event.key == pygame.K_e:
                    obj1.position+=Vector3(0,0,-1)
                    
                   
                   
                
                
                w_open_bool = False


                print("uuuuuu") 

        w_open.fill((0,7,10))

        scene.render(w_open)

        pygame.display.flip()    
                    
main()






