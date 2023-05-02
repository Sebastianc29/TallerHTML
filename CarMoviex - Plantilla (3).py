# Se importa la libreria PulP
import pulp as lp
# Se importa la librería de gráficos Matplotlib
import matplotlib.pyplot as plt

# -----------------
# Conjuntos
# -----------------
# Peliculas
P = ["Avatar: The Way of Air","Bug-Man: Quantumania","The Dolphin","John Wicked"]

# Horas
T = [t for t in range(1, 13)]

# -----------------
# Parámetros
# -----------------
# Duración de la presentación
d = {"Avatar: The Way of Air": 3,
     "Bug-Man: Quantumania": 3,
     "The Dolphin": 2,
     "John Wicked": 2}

k = 1  # Máxima cantidad de películas presentando en simultaneo

# -------------------------------------
# Creación del objeto problema en PuLP
# -------------------------------------
# Crea el problema para cargarlo con la instancia (model)


# -----------------------------
# Variables de Decisión
# -----------------------------


# -----------------------------
# Restricciones
# -----------------------------
# la cantidad de Películas presentandose en simultaneo a cada hora h en T es menor o igual a k.


# cada pelicula p en P debe presentarse por exactamente la cantidad de horas que le corresponden

# cada pelicula i en P inicia su presentación una vez.

# cada pelicula i en P se presenta en horas consecutivas y no presenta durante horas previas a la hora de inicio.

# Contabilizar la máxima finalización de las películas


# -----------------------------
# Función objetivo
# -----------------------------
# Crea la función Objetivo

# -----------------------------
# Optimizar modelo
# -----------------------------
# Optimizar el modelo con CBC (default de PuLP)
model.solve(lp.PULP_CBC_CMD(msg=0))

# -----------------------------
#    Imprimir resultados
# -----------------------------
# Imprimir estado final del optimizador
print(f"Estado (optimizador): {lp.LpStatus[model.status]}")

# Audiencia total alcanzada
print(f"Jornada de finalización: {lp.value(model.objective) * 1000}")
print()

# Imprimir variables de decisión
print("Variables de decisión")
print("", end="\t")
for t in T:
    print(t, end="\t")
print()

for p in P:
    print(p[:6], end="\t")
    for t in T:
        if y[(p, t)].value() == 1:
            print('X', end="\t")
        else:
            print('-', end='\t')
    print()

# -----------------------------
#    Graficar resultados
# -----------------------------
# Guardamos en listas las horas de inicio y fin de cada artista
comienzo = {p:sum(t * x[p, t].value() for t in T) for p in P}

# Le asignamos un color a cada película para nuestra visualización
# En python podemos llamar muchos colores por nombre
# En el siguiente link pueden ver todos los colores de python que tienen nombre:
# https://matplotlib.org/stable/gallery/color/named_colors.html

colores = {"Avatar: The Way of Air":"deepskyblue",
           "Bug-Man: Quantumania":"darkorchid",
           "The Dolphin":"gold",
           "John Wicked":"seagreen"}

# Creamos un objeto tipo figure con un subplot, guardado en la variable ax.
fig, ax = plt.subplots(figsize=(3,5))

for p in P:
    # Con ax.bar vamos a graficar una barra que cubra la franja de tiempo
    # en la que se está presentando cada película p \in P
    ax.bar(x=0, height=d[p], bottom=comienzo[p], color=colores[p], label=p)

# En el eje x no necesitamos ninguna información
ax.set_xticks([])
# Establecemos el límite a los ejes de la gráfica
ax.set_ylim(1,13)
ax.set_xlim(-0.4,0.4)
# Invertimos el eje y para que nos muestre en la parte superior el inicio del día
ax.invert_yaxis()
# Añadimos la leyenda para saber a qué película pertenece cada barra
# El argumento de bbox_to_anchor nos permite mover la leyenda de tal forma
# en que quede fuera del gráfico de barras.
ax.legend(loc="center right",bbox_to_anchor=(2,0.5))
# En el eje y tendremos las horas
ax.set_ylabel("Hora")
# Le ponemos un título al gráfico
ax.set_title("Cartelera de Cine",fontsize=14)