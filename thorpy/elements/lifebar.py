from __future__ import division
import thorpy, pygame

class LifeBar(thorpy.Element):

    @staticmethod
    def make(text, color=(255,165,0), text_color=(0,0,0),
                    size=(200,30), font_size=None):
        return LifeBar(text,color,text_color,size,font_size)

    def __init__(self, text, color=(255,165,0), text_color=(0,0,0),
                    size=(200,30), font_size=None):
        thorpy.Element.__init__(self)
        painter = thorpy.painterstyle.ClassicFrame(size,
                                                    color=thorpy.style.DEF_COLOR,
                                                    pressed=True)
        self.set_painter(painter)
        self.finish()
        #
        self.life_text = thorpy.make_text(text,font_color=text_color,font_size=font_size)
        self.life_text.center(element=self)
        self.life_color = color
        self.add_elements([self.life_text])
        self.life_width = size[0]-2
        self.life_rect = pygame.Rect(1,1, self.life_width,size[1]-2)

    def set_text(self, text):
        self.life_text.set_text(text)
        self.life_text.center(element=self)

    def blit(self):
        """Recursive blit"""
        self._clip_screen()
        for e in self._blit_before:
            e.blit()
        if self.visible:
            self.solo_blit()
            pygame.draw.rect(self.surface, self.life_color, self.life_rect)
        for e in self._blit_after:
            e.blit()
        self._unclip_screen()

    def move(self,shift):
        thorpy.Element.move(self,shift)
        self.life_rect.move_ip(shift)

    def set_life(self,life):
        self.life_rect.width = int(life*self.life_width)