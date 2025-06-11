print("Bienvenido")
nombre=input("Por favor ingrese su nombre:")
edad=(f"Hola {nombre}, podrias darme tu edad?:")
confirmacion=(f"veo que tienes {edad} años, es eso cierto?:")
if confirmacion=="si" or confirmacion=="Si":
    print(f"Ok. Bienvenido {nombre}")
else:
    print("Por que mientes? :(")

