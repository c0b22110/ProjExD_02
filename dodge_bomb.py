import random
import sys
import pygame as pg


WIDTH, HEIGHT = 1600, 900


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    bom_img = pg.Surface((20, 20)) # 練習１
    bom_img.set_colorkey((0, 0, 0)) #黒い部分を透明にする
    pg.draw.circle(bom_img, (255, 0, 0), (10, 10), 10)
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    bom_rct = bom_img.get_rect()
    # 爆弾Surfaceから爆弾Rectを抽出する
    bom_rct.center = x, y 
    # 爆弾Rectの中心座標を乱数で指定する
    vx, vy = +5, +5 #練習２
    clock = pg.time.Clock()
    tmr = 0
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return

        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, [900, 400])
        bom_rct.move_ip(vx, vy) #練習２
        screen.blit(bom_img,bom_rct)
        pg.display.update()
        tmr += 1
        clock.tick(10)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()