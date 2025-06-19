## Problema 1: Control de Temperatura en un Invernadero (25 pts)

**Enunciado:**  
Un agricultor necesita monitorear la temperatura de su invernadero para asegurar el crecimiento óptimo de sus plantas. Debes ayudarle a identificar si las temperaturas registradas están dentro del rango adecuado y alertar si alguna es peligrosa.

**Indicaciones paso a paso:**
1. Solicita al usuario que ingrese 5 temperaturas.
2. Guarda las temperaturas en una lista.
3. Calcula el promedio y la temperatura máxima.
4. Verifica si todas las temperaturas están entre 15°C y 30°C.
5. Si alguna temperatura está fuera de 10°C–35°C, muestra una advertencia.

**Puntos asignados:** 25 pts

**Criterios evaluados:**
- Uso correcto de lista y cálculos (10 pts)
- Evaluación de condiciones lógicas (10 pts)
- Orden y claridad del código (5 pts)

temperatura = []

for i in range(5):
    ingreso_temperatura = int(input("ingrese las 5 temperaturas que desea :"))
temperatura.append(ingreso_temperatura)
cantidadmax = len(temperatura)
promedio = sum(temperatura)/len(temperatura)
t_max = max(temperatura)


print(ingreso_temperatura)
print(f"la temperatura es: {promedio} la tempertura max es de:{t_max} ")

check = True
for t in temperatura:
    if t < 15 or t >30:
        check = False
if check:
    print("las temperaturas estan entre 15° grados a 30° grados:") 
else:
    print("las temperaturas no llegan a 15° grados a 30° grados")  
    for t in temperatura:
  if  t <10 or t >35:
      print("la temperatura eta afuera de 10° grados a 35° gadors")
    