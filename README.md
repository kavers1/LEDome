# LEDome
LEDome is een host application that renders gameplay for on a dome powered and visualized by leds.

We need 4 things to get this to work.

- Clients = 1 player (this can be badge controller, mobile phone, ...) that will send instructions.
- LedDome Host that can receive all client input. (process the input to output with game logic)
- The Nats server to send all the output distribution mechanism.
- 15 pieces IRA boards (each a part on the dome) that will send the color output to the led. (5 led strips on each Ira board.)
  The IRA can do more things but for now we keep it like this.



```mermaid
graph LR;

C1(Badge version 2024)
C2(Badge version 2022)
C3(Mobile Phone)
C4(Console application)
H(LEDome Host)
N(Nats)
I1(IRA 1)
I8(Other IRA's 2 to 14)
I15(IRA 15)
L1(Ledstrip 1)
L2(Ledstrip 2)
L3(Ledstrip 3)
L4(Ledstrip 4)
L5(Ledstrip 5)

L6(Connects to 5 unique <br> ledstrips like above)

C1 --> H
C2 --> H
C3 --> H
C4 --> H
H --> N
N --> H
N --> I1
N --> I8
N --> I15

I1 --> L1
I1 --> L2
I1 --> L3
I1 --> L4
I1 --> L5

I8 --> L6
I15 --> L6



```



The advantage of this is that all knowledge is centralized for the game to play.

We can easy switch the game from "Snake" to something else. :-)

This is the 10% version of the dome
![small version](https://github.com/Makerspace-baasrode/LEDome/blob/main/mini-Dome.jpg?raw=true)



**Important info!**
The "*Small*" dome version vs "*Real*" version will have a difference in length strips. This will not change the logic, it's only display purpose.



<u>Spelregels & knowledge base for snake</u> 
reference: [](https://wormate.io/)

- We starten met een basislengte van 5 leds. (elk patroon moet unique zijn!) Eventueel het patroon op de badge tonen. 
  Het kleur patroon kan niet de kleur zijn van de breadcrumbs.
- We bewegen enklel voorwaarts en kunnen enkel links of rechts.
- Komen 2 snakes elkaar tegen kop aan kop -> spelen we blad steen schaar. -> de verliezer start opnieuw op en de winnaar krijgt de lengte van zijn snake.
- De snakes kunnen langer worden door de breadcrumbs te eten die enkel zichtbaar zijn op de dome.
- Komen we onderaan aan de voet van de dome dan keren we van richting als we beneden zijn)
- We hebben een vaste snelheid -> maar we kunnen die optrekken.
