# Datos primarios / primitivos
cadena_de_texto = "string"
numeros_enteros = 123456789
numeros_decimales = 0.23452345
numeros_decimales = 2.45634564
booleanO_V = True
booleanos_F = False

# Datos complejos
objetos = {
    "llave": "valor",
    "llave": 12,
    "bool": True,
    "otro_objeto": {"llave2": "valor 2"},
}

guitarra = {
    "numero_de_cuerdas": 6,
    "material": "Madera",
    "es_de_sebas": True,
    "fabricante": {"nombre_del_fabricante": "daddario", "pais_del_fabricante": "USA"},
}

array_de_fruas = ["mango", "pera", "banano", 12, True, {}, ["mango2", "banano2"]]


tensor = [
    [
        [1, 2, 3], 
        [4, 5, 6]
    ], 
    [
        [7, 8, 9],
        [10, 11, 12]
    ]
]

tuplas = (12, "sfsdfs", 23423412, "fsdgsdfgs")

# variable_de_condicion2 = False

variable_de_condicion1 = True

if (variable_de_condicion1):
    print("Verdadero")
    variable_afectada = 0
    print(variable_afectada + 30)
    variable_afectada = 10
    print(variable_afectada)
else:
    print("Falso")
