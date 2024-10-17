class SistemaGorjetaFuzzySimples:
    def __init__(self):
        pass

    def fuzzificar_qualidade_refeicao(self, qualidade):
        """Fuzzifica a qualidade da refeição."""
        if qualidade <= 5:
            return "insosso"
        else:
            return "saboroso"

    def fuzzificar_servico(self, servico):
        """Fuzzifica o serviço."""
        if servico <= 5:
            return "ruim"
        else:
            return "excelente"

    def fuzzificar_tempo_atendimento(self, tempo):
        """Fuzzifica o tempo de atendimento."""
        if tempo <= 5:
            return "demorado"
        else:
            return "rapido"

    def inferir_gorjeta(self, qualidade_fuzzy, servico_fuzzy, tempo_fuzzy):
        """Realiza a inferência fuzzy e decide a gorjeta."""
        if tempo_fuzzy == "demorado":
            return 0 
        elif qualidade_fuzzy == "insosso" and servico_fuzzy == "ruim":
            return 5  
        elif qualidade_fuzzy == "saboroso" and servico_fuzzy == "excelente":
            return 20  
        else:
            return 10 

    def calcular_gorjeta(self, qualidade, servico, tempo):
        """Calcula a gorjeta com base nos valores fuzzificados."""
        qualidade_fuzzy = self.fuzzificar_qualidade_refeicao(qualidade)
        servico_fuzzy = self.fuzzificar_servico(servico)
        tempo_fuzzy = self.fuzzificar_tempo_atendimento(tempo)

        gorjeta = self.inferir_gorjeta(qualidade_fuzzy, servico_fuzzy, tempo_fuzzy)
        return gorjeta

if __name__ == "__main__":
    sistema_gorjeta = SistemaGorjetaFuzzySimples()

    qualidade_refeicao = 8 
    servico = 9  
    tempo_atendimento = 6  

    gorjeta_sugerida = sistema_gorjeta.calcular_gorjeta(qualidade_refeicao, servico, tempo_atendimento)

    print(f"Gorjeta sugerida: {gorjeta_sugerida}%")
