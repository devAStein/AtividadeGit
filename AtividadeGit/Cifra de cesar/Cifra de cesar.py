def cifra_de_cesar(texto, deslocamento):

    resultado = ""
    alfabeto_maiusculo ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alfabeto_minusculo ="abcdefghijklmnopqrstuvwxyz"

    for caractere in texto:
        if caractere in alfabeto_minusculo:
           
            posicao_original = alfabeto_minusculo.find(caractere)

            nova_posicao = (posicao_original + deslocamento) % 26

            resultado += alfabeto_minusculo[nova_posicao]
        elif caractere in alfabeto_maiusculo:

            posicao_original = alfabeto_maiusculo.find(caractere)
            nova_posicao = (posicao_original + deslocamento) % 26
            resultado += alfabeto_maiusculo[nova_posicao]
        else:

            resultado += caractere

    return resultado


texto1 ="abc"
deslocamento1 = 2
print(f'cifra_de_cesar("{texto1}", {deslocamento1}) -> "{cifra_de_cesar(texto1, deslocamento1)}"')

# Exemplo 2
texto2 = "xyz"
deslocamento2 = 3
print(f'cifra_de_cesar("{texto2}", {deslocamento2}) -> "{cifra_de_cesar(texto2, deslocamento2)}"')

# Exemplo 3
texto3 = "Ataque ao Amanhecer!"
deslocamento3 = 5
print(f'cifra_de_cesar("{texto3}", {deslocamento3}) -> "{cifra_de_cesar(texto3, deslocamento3)}"')