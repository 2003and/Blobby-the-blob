import pygame as pg
import colors

pg.init()


class Blob:
    def __init__(self):
        self.image = [pg.transform.scale(pg.image.load('Blob.png'), [150, 120]),
                      pg.transform.scale(pg.image.load('Blob_squeeze.png'), [150, 120])]
        self.rect = self.image[0].get_rect()
        self.rect.centerx = 250
        self.rect.centery = 200
        self.height = 0
        self.width = 0

    def draw(self):
        if self.height == 0 and velocity == 0:
            screen.blit(self.image[0], self.rect)
        else:
            screen.blit(self.image[1], self.rect)

    def do_stuff(self, wtd, vel=0):
        if wtd == 'height':
            if -120 < self.height < 140:
                self.height += vel
            else:
                if self.height > 140:
                    self.height = 140
                elif self.height < -120:
                    self.height = -120
        elif wtd == 'sides':
            if -50 < self.width < 100:
                self.width += vel
            else:
                if self.width > 150:
                    self.width = 150
                elif self.width < -50:
                    self.width = -50
        elif wtd == 'bounce':
            self.height //= -2
            if self.height < -120:
                self.height = -120  # todo: make it stretch out to sides
        self.image = [pg.transform.scale(pg.image.load('Blob.png'), [150 - self.height // 2, 120 + self.height]),
                      pg.transform.scale(pg.image.load('Blob_squeeze.png'),
                                         [150 - self.height // 2, 120 + self.height])]
        self.rect = self.image[0].get_rect()
        self.rect.centerx = 250
        self.rect.centery = 200 - self.height * 0.5


clock = pg.time.Clock()
velocity = 0
screen = pg.display.set_mode([500, 400])
pg.display.set_caption('Blobby the blob - an interactive blob')
# font = pg.font.SysFont(None, 30, True)
blobby = Blob()
while True:
    screen.fill(colors.gray)
    pg.draw.rect(screen, colors.dark_gray, [0, 200, 500, 400])
    # screen.blit(font.render(str(blobby.height), False, colors.red if not blobby.height == 0 else colors.green),
    #             [10, 360])
    for event in pg.event.get():
        if event.type == pg.QUIT:
            quit()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                if blobby.height % 2 != 0:
                    blobby.height += 1
                velocity = 2
                blobby.width = 0
            if event.key == pg.K_DOWN:
                if blobby.height % 2 != 0:
                    blobby.height += 1
                velocity = -2
                blobby.width = 0
            if event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
                if blobby.width % 2 != 0:
                    blobby.width += 1
                velocity = 2
                blobby.height = 0
        elif event.type == pg.KEYUP:
            velocity = 'bounce'
    if velocity == 'bounce':
        if blobby.height > 0.5 or blobby.height < -0.5:
            blobby.do_stuff('bounce')
        else:
            velocity = 0
    else:
        blobby.do_stuff('height', velocity)
    blobby.draw()
    pg.display.flip()
    clock.tick(20)
