# Fuzzy exercise

Author: Gustavo Dias

## Sistema de Inferência Fuzzy para Cálculo de Gorjeta
Este projeto implementa um sistema de inferência fuzzy simples em Python para calcular a gorjeta em um restaurante com base em três fatores:

Qualidade da refeição (0 a 10)
Serviço (0 a 10)
Tempo de atendimento (0 a 10)

### Regras Fuzzy Definidas
O sistema segue as seguintes regras para determinar o valor da gorjeta:

Se a refeição for insossa (<= 5) e o serviço for ruim (<= 5), a gorjeta será pouca (5%).
Se a refeição for saborosa (> 5) e o serviço for excelente (> 5), a gorjeta será generosa (20%).
Se o tempo de atendimento for demorado (<= 5), a gorjeta será 0%.
Em todos os outros casos, a gorjeta será média (10%).
