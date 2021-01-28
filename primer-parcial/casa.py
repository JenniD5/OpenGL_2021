from OpenGL.GL import *
from glew_wish import *
import glfw
from math import*


   

def dibujarTecho():   
    glBegin(GL_TRIANGLES)
    glColor3f(1.0,0.1,0.2)
    glVertex3f(-0.5, 0.0, 0.0)
    glVertex3f(0.0, 0.4, 0.0)
    glVertex3f(0.5, 0.0, 0.0)
 
    glEnd()

def dibujarCirculo():
    glColor3f(1,1,1)
    glBegin(GL_POLYGON)
    
    for x in range(360):
        angulo = x*3.14150 /180
        glVertex3f(cos(angulo)*0.5-0.2, sin(angulo)*0.1+0.5,0.0)
    #(cosex,senx,0.0)
    glEnd()

def dibujarPiso():
    glBegin(GL_QUADS)
    glColor3f(0.5,0.9,0.3)
    glVertex3f(-1.0,-0.6,0.0)
    glVertex3f(-1.0,-1.0,0.0)
    glVertex3f(1.0,-1.0,0.0)
    glVertex3f(1.0,-0.6,0.0)
    
    glEnd()

def dibujarCasa():
    glBegin(GL_QUADS)
    glColor3f(1.0,0.9,.3)
    glVertex3f(-0.3,-0.7,0.0)
    glVertex3f(0.3,-0.7,0.0)
    glVertex3f(0.3,0.0,0.0)
    glVertex3f(-0.3,0.0,0.0)
    glEnd()

def Puerta():
    glBegin(GL_QUADS)
    glColor3f(0.4,0.3,0.0)
    glVertex3f(0.05,-0.7,0.0)
    glVertex3f(0.25,-0.7,0.0) 
    glVertex3f(0.25,-0.4,0.0)
    glVertex3f(0.05,-0.4,0.0)
    glEnd()
def Perilla():
    glBegin(GL_POLYGON)
    glColor(0,0,0)

    for x in range(360):
        angulo = x*3.14159/180
        glVertex3f(cos(angulo)*0.025+0.21,sin(angulo)*0.025-0.55,0.0)


    glEnd()
def Ventana():
    glBegin(GL_QUADS)
    glColor(0,0,0)
    glVertex3f(-0.25,-0.35,0.0)
    glVertex3f(0.05,-0.35,0.0)
    glVertex3f(0.05,-0.1,0.0)
    glVertex3f(-0.25,-0.1,0.0)
    glEnd()

def MarcoVentana1():
    glBegin(GL_QUADS)
    glColor(1,1,1)
    glVertex3f(-0.23,-0.235,0.0)
    glVertex3f(-0.11,-0.235,0.0)
    glVertex3f(-0.11,-0.33,0.0)
    glVertex3f(-0.23,-0.33,0.0)


    glVertex3f(-0.09,-0.235,0.0)
    glVertex3f(0.03,-0.235,0.0)
    glVertex3f(0.03,-0.33,0.0)
    glVertex3f(-0.09,-0.33,0.0)


    glVertex3f(-0.23,-0.120,0.0)
    glVertex3f(-0.11,-0.120,0.0)
    glVertex3f(-0.11,-0.225,0.0)
    glVertex3f(-0.23,-0.225,0.0)


    glVertex3f(-0.09,-0.120,0.0)
    glVertex3f(0.03,-0.120,0.0)
    glVertex3f(0.03,-0.225,0.0)
    glVertex3f(-0.09,-0.225,0.0)



    glEnd()



    #hacer la puerta abierta

def Arbol():
    glBegin(GL_QUADS)
    glColor(0.5,0.2,0.0)
    glVertex3f(-0.8,-0.9,0.0)
    glVertex3f(-0.65,-0.9,0.0)
    glVertex3f(-0.65,-0.2,0.0)
    glVertex3f(-0.8,-0.2,0.0)
    
    glEnd()

def Copa():
    glBegin(GL_POLYGON)
    
    for x in range (360):
        glColor(0.5,0.9,0.1)
        angulo= x*3.14159/180
        glVertex3f(cos(angulo)*0.3-0.7,sin(angulo)/5-0.25,0.0)
    glEnd()    
    
def Copa2():
    glBegin(GL_POLYGON)
    glColor(0.5,0.9,0.1)
    for a in range (360):
        
        angulo= a*3.14159/180
        glVertex3f(cos(angulo)*0.35-0.5,sin(angulo)/4-0.1,0.0)
    
    glEnd()

def Copa3():
    glBegin(GL_POLYGON)
    glColor(0.5,0.9,0.1)
    for a in range (360):
        
        angulo= a*3.14159/180
        glVertex3f(cos(angulo)/3-0.8,sin(angulo)/3.5-0.02,0.0)
    
    glEnd()

def Nubes1():
    glBegin(GL_POLYGON)
    glColor(1,1,1)
      

    for a in range (360):
        
        angulo= a*3.14159/180
        glVertex3f(cos(angulo)/3+0.5,sin(angulo)/7+0.7,0.0)
    glEnd()
   
def Nube2():
    glBegin(GL_POLYGON)
    glColor(1,1,1)
    for a in range (360):
        
        angulo= a*3.14159/180
        glVertex3f(cos(angulo)/4+0.7,sin(angulo)/8+0.8,0.0)
    glEnd()

def Nube3():
    glBegin(GL_POLYGON)
    glColor(1,1,1)
      

    for a in range (360):
        
        angulo= a*3.14159/180
        glVertex3f(cos(angulo)/2+0.1,sin(angulo)/7+0.4,0.0)
    glEnd()
   
def Nube4():
    glBegin(GL_POLYGON)
    glColor(1,1,1)
    for a in range (360):
        
        angulo= a*3.14159/180
        glVertex3f(cos(angulo)/3-0.3,sin(angulo)/7+0.35,0.0)
    glEnd()

def Nube5():
    glBegin(GL_POLYGON)
    glColor(1,1,1)
      

    for a in range (360):
        
        angulo= a*3.14159/180
        glVertex3f(cos(angulo)/6-0.15,sin(angulo)/8+0.85,0.0)
    glEnd()
   
def Nube6():
    glBegin(GL_POLYGON)
    glColor(1,1,1)
    for a in range (360):
        
        angulo= a*3.14159/180
        glVertex3f(cos(angulo)/5-0.2,sin(angulo)/8+0.75,0.0)
    glEnd()

def Nube8():
    glBegin(GL_POLYGON)
    glColor(1,1,1)
    for a in range (360):
        
        angulo= a*3.14159/180
        glVertex3f(cos(angulo)/5+0.78,sin(angulo)/8+0.05,0.0)
    glEnd()

def Nube9():
    glBegin(GL_POLYGON)
    glColor(1,1,1)
      

    for a in range (360):
        
        angulo= a*3.14159/180
        glVertex3f(cos(angulo)/6+0.8,sin(angulo)/8+0.001,0.0)
    glEnd()
   
def Sol():
    glBegin(GL_POLYGON)
    glColor(1,1,0.2)
      

    for a in range (360):
        
        angulo= a*3.14159/180
        glVertex3f(cos(angulo)/3.7-0.7,sin(angulo)/3.7+0.7,0.0)
    glEnd()

def Rayos():
    glColor(1,0.6,0.1)

    glBegin(GL_LINES)
    glVertex3f(-0.9,0.45,0.0)
    glVertex3f(-0.96,0.3,0.0)
    glVertex3f(-0.83,0.4,0.0)
    glVertex3f(-0.86,0.28,0.0)
    glVertex3f(-0.73,0.4,0.0)
    glVertex3f(-0.73,0.28,0.0)
    glVertex3f(-0.63,0.4,0.0)
    glVertex3f(-0.60,0.255,0.0)
    glVertex3f(-0.53,0.42,0.0)
    glVertex3f(-0.485,0.285,0.0)
    glVertex3f(-0.44,0.465,0.0)
    glVertex3f(-0.38,0.34,0.0)
    glVertex3f(-0.40,0.54,0.0)
    glVertex3f(-0.30,0.475,0.0)
    glVertex3f(-0.38,0.63,0.0)
    glVertex3f(-0.25,0.63,0.0)
    glVertex3f(-0.39,0.735,0.0)
    glVertex3f(-0.30,0.775,0.0)
    glVertex3f(-0.43,0.83,0.0)
    glVertex3f(-0.33,0.89,0.0)
    glVertex3f(-0.47,0.93,0.0)
    glVertex3f(-0.38,0.99,0.0)
    glEnd()

def Aves():
    
    glColor(0,0,0)

    glBegin(GL_LINE_STRIP)
    glVertex3f(0.6,0.45,0.0)
    glVertex3f(0.8,0.3,0.0)
    glVertex3f(0.9,0.48,0.0)

    
    glEnd()

def Aves2():
    glColor(0,0,0)

    glBegin(GL_LINE_STRIP)
    glVertex3f(0.4,0.25,0.0)
    glVertex3f(0.5,0.1,0.0)
    glVertex3f(0.7,0.25,0.0)
    glEnd()






def dibujar():
    Nube3()
    Nube4()
    dibujarTecho()
    dibujarPiso()
    dibujarCasa()
    Puerta()
    Perilla()
    Ventana()
    MarcoVentana1()
    Arbol()
    Copa2()
    Copa3()
    Copa()
    Nubes1()
    Nube2()
        
    Nube5()
    Nube6()
    #Nube7()
    Nube8()
    Nube9()
    Sol()
    Rayos()
    Aves()
    Aves2()
    
    #dibujarCirculo()

def main():
    ancho=800
    alto=800
    #inicia glfw
    if not glfw.init():
        return
    
    #crea la ventana, 
    # independientemente del SO que usemos
    window = glfw.create_window(ancho,alto,"Mi casita", None, None)

    #Configuramos OpenGL
    glfw.window_hint(glfw.SAMPLES, 4)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR,3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR,3)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    #Validamos que se cree la ventana
    if not window:
        glfw.terminate()
        return
    #Establecemos el contexto
    glfw.make_context_current(window)

    #Activamos la validación de 
    # funciones modernas de OpenGL
    glewExperimental = True

    #Inicializar GLEW
    if glewInit() != GLEW_OK:
        print("No se pudo inicializar GLEW")
        return

    #Obtenemos versiones de OpenGL y Shaders
    version = glGetString(GL_VERSION)
    print(version)

    version_shaders = glGetString(GL_SHADING_LANGUAGE_VERSION)
    print(version_shaders)

    while not glfw.window_should_close(window):
        #Establece regiond e dibujo
        glViewport(0,0,ancho,alto)
        #Establece color de borrado
        glClearColor(0.6,0.9,1.0,1)
        #Borra el contenido de la ventana
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        #Dibujar
        dibujar()

        #Preguntar si hubo entradas de perifericos
        #(Teclado, mouse, game pad, etc.)
        glfw.poll_events()
        #Intercambia los buffers
        glfw.swap_buffers(window)

    #Se destruye la ventana para liberar memoria
    glfw.destroy_window(window)
    #Termina los procesos que inició glfw.init
    glfw.terminate()

if __name__ == "__main__":
    main()