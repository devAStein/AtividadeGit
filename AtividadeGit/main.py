def sao_anagramas(string1, string2):

  string = string1.replace(" ", "").lower()
  string2 = string2.replace(" ", "").lower()

  if sorted(string) == sorted(string2):
    return True
  else:
    return False

  pass



def cifra_de_cesar(texto, deslocamento):
  # TODO: Implementar a lógica
  pass



print("------ Teste Função Anagramas ---------")
print(sao_anagramas("amor", "roma"))            # True
print(sao_anagramas("A gentleman", "Elegant man"))  # True
print(sao_anagramas("gato", "cabra"))
