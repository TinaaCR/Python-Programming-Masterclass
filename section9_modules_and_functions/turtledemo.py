# import turtle
# # import time
#
# turtle.forward(250)
# turtle.right(250)
# turtle.forward(150)
#
# # time.sleep(4)
#
# turtle.done()

# koden over kan skrives på en annen måte og. ved å kun ta inn delene fra turtle modulen som vi er interessert i (men da har man såklart ikke tilgang til de andre delene):

# from turtle import forward, right, done
#
# forward(150)
# right(250)
# forward(150)
#
# done()

# om vi ønsker å både være spesifikk og å få med alt kan vi gjøre en kombi (men det er anbefalt å velge en av delene...):

# from turtle import forward, right, done
# import turtle
#
# forward(150)
# right(250)
# turtle.circle(75)
# forward(150)
#
# done()

# en annen variant (MEN denne metoden er ikke anbefalt, siden vi ikke egentlig vet helt hva vi importerer):

from turtle import *

forward(150)
right(250)
circle(75)
forward(150)

done()