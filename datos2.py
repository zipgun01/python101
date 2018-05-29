#!/bin/python3
edad=int(input("¿Cual es tu edad?: "))

print("Tu edad es: %d "% edad)

if (edad < 18):
    print("Estas morro")

elif (edad >17 and edad<60):
    print("ADUTO")

else: 
    print("Estas oldie")
