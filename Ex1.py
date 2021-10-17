texto_salto = ['Primeiro', 'Segundo', 'Terceiro', 'Quarto', 'Quinto']

saltos_do_atleta = [0.0, 0.0, 0.0, 0.0, 0.0]


atleta = input("Atleta: ")

if atleta != '':
    for c in range(0, 5):
        saltos_do_atleta[c] = float(input(f"{texto_salto[c]} salto: "))

    # Ordenando a lista de saltos
    saltos_do_atleta.sort()


    media_saltos = (saltos_do_atleta[1] + saltos_do_atleta[2] + saltos_do_atleta[3])/3

    print("="*30)

    print(f"Media dos demais saltos.: {media_saltos:.2f}\n")
    print("Resultado final: ")
    print(f"{atleta}: {media_saltos:.2f}")
else:
    print('Informe o nome do atleta')
