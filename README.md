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
import RPi.GPIO as gpio
import time

def distance(measure='cm'):
    try:
        gpio.setmode(gpio.BOARD)
        gpio.setup(12, gpio.OUT)
        gpio.setup(16, gpio.IN)
        
        gpio.output(12, False)
        while gpio.input(16) == 0:
            nosig = time.time()

        while gpio.input(16) == 1:
            sig = time.time()

        tl = sig - nosig

        if measure == 'cm':
            distance = tl / 0.000058
        elif measure == 'in':
            distance = tl / 0.000148
        else:
            print('improper choice of measurement: in or cm')
            distance = None

        gpio.cleanup()
        return distance
    except:
        distance = 100
        gpio.cleanup()
        return distance

		
if __name__ == "__main__":
    print(distance('cm'))

```

### Evidence

### wiring

### Reflection

## CircuitPython_LCD

### Description & Code

```python
Code goes here

```

### Evidence

### wiring

### Reflection





## NextAssignment

### Description & Code

```python
Code goes here

```

### Evidence

### wiring

### Reflection
