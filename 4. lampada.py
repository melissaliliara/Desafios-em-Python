
# Simulação do problema dos interruptores e lâmpadas

# Estados iniciais dos interruptores: 0 = desligado, 1 = ligado
interruptores = [0, 0, 0]

# Função para simular a visita à sala das lâmpadas
def visita_sala():
    # Simula o estado das lâmpadas baseado nos interruptores
    # lâmpadas: -1 = fria e apagada, 0 = quente e apagada, 1 = acesa
    lampadas = [-1, -1, -1]  # Todas começam frias e apagadas
    
    # Se o interruptor estiver ligado, a lâmpada correspondente fica acesa
    for i in range(3):
        if interruptores[i] == 1:
            lampadas[i] = 1  # Lâmpada acesa
    
    # Simula a espera para uma lâmpada esfriar
    if interruptores[0] == 1:
        lampadas[0] = 0  # Lâmpada quente mas agora apagada
    
    return lampadas

# Estratégia
interruptores[0] = 1  # Ligue o primeiro interruptor
# Simula espera para a lâmpada esquentar
interruptores[0] = 0  # Desligue o primeiro interruptor
interruptores[1] = 1  # Ligue o segundo interruptor

# Primeira visita à sala das lâmpadas
resultado_primeira_visita = visita_sala()
print("Resultado da primeira visita:", resultado_primeira_visita)

# Interpretação dos resultados
# A lâmpada acesa é controlada pelo segundo interruptor
# A lâmpada quente (0 no resultado) é controlada pelo primeiro interruptor
# A lâmpada fria e apagada (-1 no resultado) é controlada pelo terceiro interruptor

# Não precisamos de uma segunda visita com base na estratégia proposta