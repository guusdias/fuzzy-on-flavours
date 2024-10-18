import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

class SistemaGorjetaFuzzy:
    def __init__(self):
        # Definição das variáveis fuzzy (qualidade da refeição, serviço, tempo de atendimento e gorjeta)
        self.qualidade_refeicao = ctrl.Antecedent(np.arange(0, 11, 1), 'qualidade_refeicao')
        self.servico = ctrl.Antecedent(np.arange(0, 11, 1), 'servico')
        self.tempo_atendimento = ctrl.Antecedent(np.arange(0, 11, 1), 'tempo_atendimento')
        self.gorjeta = ctrl.Consequent(np.arange(0, 26, 1), 'gorjeta')

        self._definir_funcoes_pertinencia()
        self._definir_regras()

    def _definir_funcoes_pertinencia(self):
        """Define as funções de pertinência para todas as variáveis fuzzy."""
        self.qualidade_refeicao['insosso'] = fuzz.trimf(self.qualidade_refeicao.universe, [0, 0, 5])
        self.qualidade_refeicao['saboroso'] = fuzz.trimf(self.qualidade_refeicao.universe, [5, 10, 10])

        self.servico['ruim'] = fuzz.trimf(self.servico.universe, [0, 0, 5])
        self.servico['excelente'] = fuzz.trimf(self.servico.universe, [5, 10, 10])

        self.tempo_atendimento['demorado'] = fuzz.trimf(self.tempo_atendimento.universe, [0, 0, 5])
        self.tempo_atendimento['rapido'] = fuzz.trimf(self.tempo_atendimento.universe, [5, 10, 10])

        self.gorjeta['pouca'] = fuzz.trimf(self.gorjeta.universe, [0, 0, 13])
        self.gorjeta['generosa'] = fuzz.trimf(self.gorjeta.universe, [13, 25, 25])

    def _definir_regras(self):
        """Define as regras fuzzy baseadas nas funções de pertinência."""
        regra1 = ctrl.Rule(self.qualidade_refeicao['insosso'] & self.servico['ruim'], self.gorjeta['pouca'])
        regra2 = ctrl.Rule(self.qualidade_refeicao['saboroso'] & self.servico['excelente'], self.gorjeta['generosa'])
        regra3 = ctrl.Rule(self.tempo_atendimento['demorado'], self.gorjeta['pouca'])
        regra4 = ctrl.Rule(self.tempo_atendimento['rapido'], self.gorjeta['generosa'])

        self.sistema_controle = ctrl.ControlSystem([regra1, regra2, regra3, regra4])
        self.simulador = ctrl.ControlSystemSimulation(self.sistema_controle)

    def calcular_gorjeta(self, qualidade_refeicao, servico, tempo_atendimento):
        """Calcula a gorjeta com base nos valores de entrada fornecidos."""
        self.simulador.input['qualidade_refeicao'] = qualidade_refeicao
        self.simulador.input['servico'] = servico
        self.simulador.input['tempo_atendimento'] = tempo_atendimento

        self.simulador.compute()

        return self.simulador.output['gorjeta']

if __name__ == "__main__":
    sistema_gorjeta = SistemaGorjetaFuzzy()

    qualidade_refeicao = 8 
    servico = 9
    tempo_atendimento = 6

   
    gorjeta_sugerida = sistema_gorjeta.calcular_gorjeta(qualidade_refeicao, servico, tempo_atendimento)

    print(f"Gorjeta sugerida: {gorjeta_sugerida:.2f}%")
