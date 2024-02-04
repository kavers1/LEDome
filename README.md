# LEDome
LEDome is een host application that renders gameplay for on a dome powered and visualized by leds.

We need 4 things to get this to work.

- Clients = 1 player (this can be badge controller, mobile phone, ...) that will send instructions.
- LedDome Host that can receive all client input. (process the input to output with game logic)
- The Nats server to send all the output distribution mechanism.
- 15 pieces IRA boards (each a part on the dome) that will send the color output to the led. (5 led strips on each Ira board.)



```mermaid
graph TD;

C1(Badge version 2024)
C2(Badge version 2022)
C3(Mobile Phone)
C4(Console application)
H(Host)
N(Nats)
I1(IRA 1)
I2(IRA 2)
I3(IRA 3)
I4(IRA 4)
I5(IRA 5)
I6(IRA 6)
I7(IRA 7)
I8(IRA 8)
I9(IRA 9)
I10(IRA 10)
I11(IRA 11)
I12(IRA 12)
I13(IRA 13)
I14(IRA 14)
I15(IRA 15)

C1 --> H
C2 --> H
C3 --> H
C4 --> H
H --> N
N --> H
N --> I1
N --> I2
N --> I3
N --> I4
N --> I5
N --> I6
N --> I7
N --> I8
N --> I9
N --> I10
N --> I11
N --> I12
N --> I13
N --> I14
N --> I15


```



The advantage of this is that all knowledge is centralized for the game to play.

We can easy switch the game from snake to something else. :-)

​	
