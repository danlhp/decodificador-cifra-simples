#PROGRAMA DE RESOLUÇÃO DE CIFRA SIMPLES
alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
secret = "Uifsf jt b tfdsfu nfttbhf!"
mensagem_decodificada = ""

for char in secret:
    if char.islower():
        index = alfabeto.index(char)
        mensagem_decodificada += alfabeto[(index - 1) % 26]
    elif char.isupper():
        index = alfabeto.index(char.lower())
        mensagem_decodificada += alfabeto[(index - 1) % 26].upper()
    else:
        mensagem_decodificada += char
print(mensagem_decodificada)
