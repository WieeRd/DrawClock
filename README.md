# DrawClock
Renders clock image based on given time and asset images  

### Sample image (12:45)
<p float="left">
  <img src=https://github.com/WieeRd/DrawClock/blob/master/example/frame.png width="100" height="100">
  <img src=https://github.com/WieeRd/DrawClock/blob/master/example/h_pin.png width="100" height="100">
  <img src=https://github.com/WieeRd/DrawClock/blob/master/example/m_pin.png width="100" height="100">
  <img src=https://github.com/WieeRd/DrawClock/blob/master/example/12:45.png width="100" height="100">
</p>
You can find sample images inside example folder

### Example code
```python
from PIL import Image
from drawclock import DrawClock

frame = Image.open("frame.png")

# Requires transparent background
h_pin = Image.open("h_pin.png")
m_pin = Image.open("m_pin.png")

dc = DrawClock(frame, h_pin, m_pin)

hour = int(input("Hour: "))
minute = int(input("Minute: "))

result = dc.draw(hour, minute)
result.show()
# result.save("output.png")
```

### Note
- Requires PIL library (get it with `pip install pillow`)
- I made this instead of studying for midterm test
