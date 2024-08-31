# Este código crea una ventana donde se muestra la animación de un corazón vaciándose y un texto que dice perdiste el juego intenta de nuevo


import pygame,sys   #Se importa la libreria de pygame y el sys


#Esta parte del código le otorga las características necesarias al elemento corazón para que este funcione y realize la animación donde cambia por 5 sprites y al terminar la secuencia se queda en el último
class Corazon(pygame.sprite.Sprite):
    #Esto crea al corazon y le da los sprites iniciales necesarios para hacer la animación
    def __init__(self,x,y):
        super().__init__()
        self.sprites=[]
        self.sprites.append(pygame.image.load("C:/Users/Carolina/Desktop/sprites/c1.png"))
        self.sprites.append(pygame.image.load("C:/Users/Carolina/Desktop/sprites/c2.png"))
        self.sprites.append(pygame.image.load("C:/Users/Carolina/Desktop/sprites/c3.png"))
        self.sprites.append(pygame.image.load("C:/Users/Carolina/Desktop/sprites/c4.png"))
        self.sprites.append(pygame.image.load("C:/Users/Carolina/Desktop/sprites/c5.png")) 

        self.sprite_actual=0
        self.image=self.sprites[self.sprite_actual]
        
        self.rect=self.image.get_rect()
        self.rect.topleft=[x,y]
        
    #Esta parte hace que el corazón vaya cambiando sus sprites hasta llegar al 4 y detenerse
    def update(self):
        self.sprite_actual+=1
        if self.sprite_actual>=len(self.sprites):
            self.sprite_actual=4
        
        self.image=self.sprites[self.sprite_actual]
        


#Parametros para poder iniciar la funcion perdiste_el_juego
coordenadax=1000
coordenaday=500


# Esta función hace que en la pantalla se cree un texto que se mentiene hasta cerrar la pantalla
def perdiste_el_juego(x,y):
    perdiste=font.render("Game",True,(255,255,255))
    eljuego=font.render("over",True,(255,255,255))
    intenta=font.render("¡Try",True,(255,150,150))
    denuevo=font.render("again!",True,(255,150,150))
    screen.blit(perdiste,(740,100))
    screen.blit(eljuego,(1000,100))
    screen.blit(intenta,(750,350))
    screen.blit(denuevo,(750,490))
    

 
#Inicializa la biblioteca de pygame y crea nuestra fuente
pygame.init()
font=pygame.font.SysFont("consolas",110)
clock=pygame.time.Clock()



#Crea una ventana en pantalla y le da un título
screen=pygame.display.set_mode((1300,700))
pygame.display.set_caption("Game Over")


#Crea el grupo del corazón para administar la animación 
animacion=pygame.sprite.Group()
corazon=Corazon(100,100)
animacion.add(corazon)


# Llama un sonido y lo reproduce
pygame.mixer.music.load("C:/Users/Carolina/Desktop/sprites/sfx-defeat6.mp3")
pygame.mixer.music.play(1)


# Esto abre una ventana y lo va actualizando con los parámetros de nuestro código, es decir la animación y el texto, también establece que si damos clic en x la ventana se cerrará
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
            
            
    screen.fill((0,0,0))

    
    #Usa el grupo del corazón para dubijar las animaciones y el texto y luego actualiza la pantalla, además de establecer los frames por segundo 
    animacion.draw(screen)
    perdiste_el_juego(coordenadax,coordenaday)
    animacion.update()

    pygame.display.flip()
    clock.tick(2) 
    