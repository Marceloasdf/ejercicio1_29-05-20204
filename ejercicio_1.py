import os
import time
import msvcrt
usuarios=[]
while True:
    print("""
    1) inicio sesion.
    2) Registrar usuario.
    3) Eliminar usuario!
    4) Salir
    """)
    opc = int(input("Seleccione su opcion: "))
    if opc==1:
        pass
    elif opc==2:
        print("Registrar usuario")
        nombre= input("nombre: ")
        contrasena =input("contraseña: ")
        usuario ={
            "nombre": nombre,
            "contrasena": contrasena,}
        usuarios.append(usuario)
        print("Usuario guardado exitosamente!")
    elif opc==3:
        pass
    else:
        print("adios!")
        time.sleep
    