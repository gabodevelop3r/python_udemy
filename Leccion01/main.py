# Tipo integer
x: int = 18

# tipo float
x: float = 82939832.1

# tipo string
x: str = "gabo.develp3r@gmail.com"

# tipo boolean
x: bool = False

print(type(x))

# cadena (String)
miGrupoFavorito = "Metallica" + " " + "Best metal band"
comentario = "The best metal band"

# print("mi grupo favorito es : " + miGrupoFavorito + " " + comentario)
print("Mi grupo favorito es:", miGrupoFavorito, comentario)

numero1 = "1"
numero2 = "2"
print("concatenacion:", numero1 + numero2)

print(int(numero1) + int(numero2))

# tipos bool (boolean)
miVariable = False
print(miVariable)

miVariable = 3 > 2;
print(miVariable)

if miVariable:
    print("el resultado es verdadero")
else:
    print("el resultado es falso")

# funcion input para procesar la entrada del usuario

# resultado = int(input("Como estuvo tu dia (1 al 10)?:"))
# print("mi dia estuvo de:", resultado)
# print("fin del programa")

titulo = input("Proporciona el titulo del libro")
author = input("Proporciona el autor del libro")
print(titulo, ' fue escrito por:', author)
