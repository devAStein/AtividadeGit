def cifra_de_cesar(texto, deslocamento):

    if not texto:
        return ""

    resultado = ""
    alfabeto_maiusculo = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alfabeto_minusculo = "abcdefghijklmnopqrstuvwxyz"

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




texto_usuario = input("Digite o texto para criptografar: ")
deslocamento_usuario_str = input("Digite o número do deslocamento: ")



if not texto_usuario.strip():
    print("Erro: O campo de texto não pode estar vazio.")

elif not deslocamento_usuario_str.strip():
    print("Erro: O campo de deslocamento não pode estar vazio.")

# 3. VERIFICAÇÃO ADICIONAL: O deslocamento é um número válido?
elif not deslocamento_usuario_str.isdigit():
    print("Erro: O deslocamento deve ser um número inteiro positivo.")


else:

    deslocamento_int = int(deslocamento_usuario_str)


    texto_criptografado = cifra_de_cesar(texto_usuario, deslocamento_int)

    print("\n--- Resultado ---")
    print(f"Texto Criptografado: {texto_criptografado}")