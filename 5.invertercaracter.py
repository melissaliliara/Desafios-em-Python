
def inverter_string(s):
    string_invertida = ''
    for i in range(len(s) - 1, -1, -1):
        string_invertida += s[i]
    return string_invertida

# Recebe a string de uma entrada do usuário
string_original = input("Digite uma palavra para ser invertida: ")
string_invertida = inverter_string(string_original)
print("palavra original:", string_original)
print("palavra invertida:", string_invertida)