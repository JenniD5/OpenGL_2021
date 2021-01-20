from OpenGL.GL import *
from glew_wish import *
import glfw 

def main():
    #iniciar glfw
    if not glfw.init(): #si no hay nada, se sale 
        return
    #crear ventana independiente dle sistema operativo a usar 
    #crear la centada y poner el glfw dentro 
    window = glfw.create_window(800,600,"mi ventana", None, None )

    #confugiraropengl
    #configuraciones de la ventana, como se deben de comportar, al hacer movimientos remuestra señal o imagen 4 veces, eso es sample. 
    glfw.window_hint(glfw.SAMPLES, 4)

    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR,3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR,3)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT,GL_TRUE)
    glfw.window_hint(glfw.OPENGL_PROFILE,glfw.OPENGL_CORE_PROFILE)
    #validar que se creo la ventana 
    if not window:#i la venatana esta vacia, se termina 
        glfw.terminate()
        return

     #establecer el contexto 
    glfw.make_context_current(window)

    #activar la calidacion de funciones modernas de opengl 
    glewExperimental = True
    
    if glewInit() !=GLEW_OK:
        print("no se pudo iniciar Glew")
        return

    #obtner versiones de opengl y shaders
    version = glGetString(GL_VERSION)
    print(version)

    #string que rerepsenta el lenguaje de shaders que representa 
    version_shaders=glGetString(GL_SHADING_LANGUAGE_VERSION)
    print(version_shaders)


    #ciclo de dibujo
    while not glfw.window_should_close(window):
        #region de dibujo 
        glViewport(0,0,800,600)
        #color de borrado
        glClearColor(0.5,1,0,1)
        #borrar contenido
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        #dibujar 

        #preguntar si hubo entrada de perifericos
        #teclado,mouse,game pad,etc.
        glfw.poll_events()
        #intercambiar los buffers 
        glfw.swap_buffers(window)

    #para terminar todo, debemos destruir la ventana. 
    glfw.destroy_window(window)
    #termina los procesos que inicio glfw.init 
    glfw.terminate()

#hacer que python tenga funcion main
if __name__=="__main__":
    main()






