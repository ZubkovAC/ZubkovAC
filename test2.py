from graph import *

def main():
    windowSize(600,500)
    paint_house(200,200,300,400)
    run()
def paint_house(x, y, width, height):
    '''Рисует домик
       (x,y) -- опорная точка, левая-нижная точка крыши'''
    paint_walls(x, y, width, height // 2)
    paint_roof(x, y, width, height // 2)
    w_widht = width // 3
    w_heigth = height // 6
    paint_window(x + w_widht, y + w_heigth, w_widht, w_heigth)

main()