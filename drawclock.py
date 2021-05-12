#!/usr/bin/env python3
from PIL import Image

class DrawClock:
    def __init__(self, frame: Image.Image, h_pin: Image.Image, m_pin: Image.Image):
        self.frame = frame
        self.h_pin = h_pin
        self.m_pin = m_pin

    def draw(self, hour: int, minute: int) -> Image.Image:
        base = self.frame.copy()

        angle_h = 360 - hour*30 - minute//2
        angle_m = 360 - minute*6

        h_pin = self.h_pin.rotate(angle_h)
        m_pin = self.m_pin.rotate(angle_m)

        base.paste(h_pin, (0,0), h_pin.convert('RGBA'))
        base.paste(m_pin, (0,0), m_pin.convert('RGBA'))

        return base

if __name__=="__main__":
    frame = Image.open("./example/frame.png")
    h_pin = Image.open("./example/h_pin.png")
    m_pin = Image.open("./example/m_pin.png")
    dc = DrawClock(frame, h_pin, m_pin)

    while True:
        get = input("hh:mm = ").split(sep=':')
        if len(get)!=2:
            continue
        hh, mm = int(get[0]), int(get[1])
        result = dc.draw(hh, mm)
        result.show()
        result.save("output.png")
