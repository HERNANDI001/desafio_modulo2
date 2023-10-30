# Define as palavras-chave para cada vaga
vagas = {
    "Vaga 1": ["Python", "Programação", "Desenvolvimento"],
    "Vaga 2": ["Análise de dados", "Dados", "SQL"]
}

# Inicializa os dicionários para contar o número de candidatos e candidatos válidos por vaga
candidatos_por_vaga = {vaga: 0 for vaga in vagas}
candidatos_validos_por_vaga = {vaga: 0 for vaga in vagas}

# Loop para coletar informações dos candidatos
while True:
    vaga = input("Para qual vaga você se inscreveu? (Digite Vaga 1 para: 'Python', 'Programação','Desenvolimento'. ou \n Digite Vaga 2 para: 'Análise de Dados' ou 'Dados' ou 'SQL' ou digite '0' para sair): ")
    if vaga == "0":
        break

    if vaga not in vagas:
        print("Vaga não reconhecida. Tente novamente.")
        continue

    resumo = input("Digite o resumo/minibio: ")

    palavras_chave_vaga = vagas[vaga]
    palavras_resumo = resumo.split()  # Divide o resumo em palavras

    # Verifica se o candidato tem as palavras-chave necessárias
    tem_palavras_chave = all(palavra in palavras_resumo for palavra in palavras_chave_vaga)

    candidatos_por_vaga[vaga] += 1

    if tem_palavras_chave:
        candidatos_validos_por_vaga[vaga] += 1

# Mostra os totais
print("Totais:")
for vaga in vagas:
    print(f"{vaga}:")
    print(f"  Total de inscritos: {candidatos_por_vaga[vaga]}")
    print(f"  Total de candidatos válidos: {candidatos_validos_por_vaga[vaga]}")