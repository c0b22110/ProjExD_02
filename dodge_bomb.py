import random
import sys
import pygame as pg


WIDTH, HEIGHT = 1600, 900
delt = {
    pg.K_UP: (0, -5),
    pg.K_DOWN: (0, +5),
    pg.K_LEFT: (-5, 0),
    pg.K_RIGHT: (+5, 0),
    }


def hoge(rect: pg.Rect) -> tuple[bool, bool]:
    '''
    こうかとんRect、爆弾Rectが画面の外か中かを判定する関数
    引数 :こうかとんRect or 爆弾Rect
    戻り値：横方向、縦方向の判定結果タプル(True:画面内、False:画面外)
    '''
    yoko, tate = True, True
    if rect.left < 0 or WIDTH < rect.right: #横方向判定
        yoko = False
    if rect.top < 0 or HEIGHT < rect.bottom: #縦方向判定
        tate = False
    return yoko, tate


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    #こうかとんSurface(kk_img)からこうかとんRect（kk_rct)を抽出
    kk_rct = kk_img.get_rect()
    kk_rct.center = 900, 400
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
    accs = [a for a in range(1, 11)]
    bom_imgs = []
    for r in range(1, 11):
        bom_img = pg.Surface((20*r, 20*r))
        bom_img.set_colorkey((0, 0, 0))
        pg.draw.circle(bom_img, (255, 0, 0), (10*r, 10*r), 10*r)
        bom_imgs.append(bom_img)
    key_lis = {(-5, 0): pg.transform.rotozoom(kk_img, 0, 1.0), 
               (-5, -5): pg.transform.rotozoom(kk_img, -45, 1.0),
               (0, -5): pg.transform.flip(pg.transform.rotozoom(kk_img, -90, 1.0), True, False),
               (+5, -5): pg.transform.flip(pg.transform.rotozoom(kk_img, -45, 1.0), True, False),
               (+5, 0): pg.transform.flip(kk_img, True, False),
               (+5, +5): pg.transform.flip(pg.transform.rotozoom(kk_img, 45, 1.0), True, False),
               (0, +5): pg.transform.flip(pg.transform.rotozoom(kk_img, 90, 1.0), True, False),
               (-5, +5): pg.transform.rotozoom(kk_img, 45, 1.0)}

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
            
        if kk_rct.colliderect(bom_rct):

            print("ゲームオーバー")
            return
        key_lst = pg.key.get_pressed()
        sum_mv = [0, 0] #合計移動量
        for k, mv in delt.items():
            if key_lst[k]: 
                sum_mv[0] += mv[0]
                sum_mv[1] += mv[1]
            for l, m in key_lis.items():
                if sum_mv[0] ==l[0] and sum_mv[1] == l[1]:
                    kk_img = m
        

        kk_rct.move_ip(sum_mv)
        if hoge(kk_rct) != (True,True):
            kk_rct.move_ip(-sum_mv[0], -sum_mv[1])
        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, kk_rct) #練習２
        avx, avy = vx*accs[min(tmr//500, 9)], vy*accs[min(tmr//500, 9)]
        bom_rct.move_ip(avx, avy)
        yoko, tate = hoge(bom_rct)
        if not yoko:
            vx *= -1
        if not tate:
            vy *= -1
        bom_img = bom_imgs[min(tmr//500, 9)]
        screen.blit(bom_img,bom_rct)
        pg.display.update()
        tmr += 1
        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()