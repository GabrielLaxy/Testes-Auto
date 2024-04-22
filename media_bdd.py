#Given
x = 4
y = 2

def calcula_media(x,y):
    #When
    calculo = (x+y)/2
    return calculo

media = calcula_media(x,y)
print(f"A media de {x} e {y} é {media}")

#Then
assert media == 3 ,f"A média de {x} e {y} deve ser 3, e o resultado foi {media}"

# Feature: Media entre 2 numeros inteiros
#     Scenario: Realizar uma media simples
#     Given eu tenho dois números: 4 e 2
#     When eu divido a soma dos os dois números
#     Then o resultado deve ser 3