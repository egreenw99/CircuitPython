# CircuitPython
 The follwing files are my first foray into CircuitPython.
## Table of Contents
* [Table of Contents](#TableOfContents)
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [CircuitPython_LCD](#CircuitPython_LCD)
* [NextAssignmentGoesHere](#NextAssignment)
---

## Hello_CircuitPython

.

### Description & Code
Description goes here

Here's how you make code look like code:

```python
import board
import neopixel

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
dot.brightness = 0.1


print("Make it Cyan!")
while True:
    dot.fill((0, 255, 255))

```


### Evidence
Pictures / Gifs of your work should go here

### wiring
Make an account with your google ID at [tinkercad.com](https://www.tinkercad.com/learn/circuits), and use "TinkerCad Circuits to make a wiring diagram."  It's really easy!  
Then post an image here.   [here's a quick tutorial for all markdown code, like making links](https://www.markdownguide.org/basic-syntax/)

### Reflection
What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience?  Your ultimate goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person.




## CircuitPython_Servo

### Description & Code

```python


import time
import board
import pwmio
import servo

# create a PWMOut object on Pin A2.
import time
import board
import pwmio
import servo
import touchio

# create a PWMOut object on Pin A2.
pwm = pwmio.PWMOut(board.A3, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)


touch_A1 = touchio.TouchIn(board.A1)
touch_A2 = touchio.TouchIn(board.A2)

while True:
    if touch_A1.value:
        print("Touch A1!")
    my_servo.angle = 90
    if touch_A2.value:
        print("Touched A2!")
        my_servo.angle = 0
        time.sleep(0.05)
```

### Evidence

### wiring
 
### Reflection 
 I was able to get the servo turning with compasitive touch after help from peers. I had some equipment malfunctions and wiring issues so next time I will double check my equipment and learn to code a little bit so im not so reliant on having other poeple code for me 
 
 ## CircuitPython_Distance 

### Description & Code

```python
import simpleio
import time
import board
import adafruit_hcsr04
import neopixel

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)
blueValue = 0
redValue = 0
greenValue = 0

while True:
    try:
        cm = sonar.distance
        print((cm,))
        if cm < 5:
            dot.fill((0, 0, 0))
        elif cm < 20:
            redValue = simpleio.map_range(cm, 5, 20, 255, 0)
            greenValue = 0
            blueValue = simpleio.map_range(cm, 5, 20, 0, 255)
            print("RGB: (", redValue, ", ", greenValue, ", ", blueValue, ")")
            dot.fill((int(redValue), int(greenValue), int(blueValue)))
        elif cm < 35:
            redValue = 0
            greenValue = simpleio.map_range(cm, 20, 35, 0, 255)
            blueValue = simpleio.map_range(cm, 20, 35, 255, 0)
            print("RGB: (", redValue, ", ", greenValue, ", ", blueValue, ")")
            dot.fill((int(redValue), int(greenValue), int(blueValue)))
        else:
            dot.fill((0, 0, 0))
            time.sleep(0.1)
    except RuntimeError:
        print("Retrying!")

```

### Evidence

### wiring

### Reflection





## Photointerrupters

### Description & Code

```python
from digitalio import DigitalInOut, Direction, Pull
import time
import board

interrupter = DigitalInOut(board.D7)
interrupter.direction = Direction.INPUT
interrupter.pull = Pull.UP

counter = 0

photo = False
state = False

max = 4
start = time.time()
while True:
    photo = interrupter.value
    if photo and not state:
            counter += 1
    state = photo

    remaining = max - time.time()

    if remaining <= 0:
        print("Interrupts:", str(counter))
        max = time.time() + 4
        counter = 0
```

### Evidence

### wiring

### Reflection
