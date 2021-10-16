# define some colors (R, G, B)
import  pygame as pg
vec = pg.math.Vector2


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BROWN = (205, 102, 0)

# game settings
WIDTH = 1024   # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 768  # 16 * 48 or 32 * 24 or 64 * 12
FPS = 60
TITLE = "Tilemap Demo"
BGCOLOR = BROWN


TILESIZE = 32
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

WALL_IMG = "tile_98.png"

#Player settings
PLAYER_SPEED = 200
PLAYER_ROT_SPEED = 250
PLAYER_HIT_RECT = pg.Rect( 0, 0 ,35 ,35)
PLAYER_IMG = "Escanorfire.png"
#Es para que las balas salgana del arma
BARREL_OFFSET = vec(30, 12)
PLAYER_HEALTH = 100

#Gun settings
BULLET_IMG = "Cruel Sun.png"
BULLET_SPEED = 500
BULLET_LIFETIME = 1000
BULLET_RATE = 150
#El recoil
KICK_BACK = 200
#Spray del arma
GUN_SPREAD = 5
BULLET_DAMAGE = 10


#Mobs settings
MOB_IMG = "Demon1.png"
MOB_SPEED = 125
MOB_HIT_RECT = pg.Rect( 0, 0 ,30 ,30)
MOB_HEALTH = 100
MOB_DAMAGE = 10
MOB_KNOCKBACK = 20
score = 0

#Eventos
Moverse = 0

Customevent_1 = pg.USEREVENT

pg.time.set_timer(Customevent_1,5000)

