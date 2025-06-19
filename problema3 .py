    ## Problema 3: Sistema de Acceso Condicional (20 pts)

    **Enunciado:**  
    En una empresa, el acceso a una zona restringida depende de la edad, el rol de supervisor y la autorización especial. Debes crear un sistema que determine si una persona puede ingresar.

    **Indicaciones paso a paso:**
    1. Solicita al usuario su edad, si es supervisor y si tiene autorización.
    2. Verifica si puede acceder: debe ser mayor de edad y cumplir al menos una condición (ser supervisor o tener autorización).
    3. Muestra un mensaje indicando si el acceso está permitido o denegado.

    **Puntos asignados:** 20 pts

    **Criterios evaluados:**
    - Uso correcto de operadores lógicos (10 pts)
    - Validación de condiciones y entrada de datos (5 pts)
    - Claridad de la salida (5 pts)


  edad = int(input("ingese su edad corespondiente: "))
es_supervisor = input("¿usted es un supervisor?: ")
posee_autorizacion = input("¿posee autorizacion?: ")

while True:
    if edad <18:
        print("acceso denegado")
        break
    elif edad <18 and es_supervisor == "si" or posee_autorizacion == "si":
        print("acceso permitido")
        break
    else:
        print("acceso denegado")
        break
