saltos_do_atleta = ['Primeiro', 'Segundo', 'Terceiro', 'Quarto', 'Quinto']

distância_saltos = [0.0, 0.0, 0.0, 0.0, 0.0]
atleta = input("Atleta: ")
if atleta != '':
    for salto in range(0, 5):
    distância_saltos[salto] = float(input(f"{texto_salto[salto]} salto: "))

    distância_saltos.sort()
    media_saltos = (distância_saltos[1] + distância_saltos[2] + distância_saltos[3])/3

    print("Resultado final: ")
    print(f"Atleta: {atleta}")
    print(f"Media de saltos.: {media_saltos:.2f}\n")
else:
    print('Informe o nome do atleta')
