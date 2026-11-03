# Pesquisa de opinião - TudoWeb
# Coleta nome, idade e opinião de 50 entrevistados e mostra o resultado.

TOTAL_ENTREVISTADOS = 50  # para o teste com 10, troque para 10

excelente = 0
bom = 0
ruim = 0

for i in range(TOTAL_ENTREVISTADOS):
    print(f"\nEntrevistado {i + 1} de {TOTAL_ENTREVISTADOS}")
    nome = input("Nome: ")
    idade = int(input("Idade: "))

    opiniao = 0
    while opiniao not in (1, 2, 3):
        opiniao = int(input("Opinião sobre o atendimento (1-EXCELENTE, 2-BOM, 3-RUIM): "))
        if opiniao not in (1, 2, 3):
            print("Opção inválida! Digite 1, 2 ou 3.")

    if opiniao == 1:
        excelente += 1
    elif opiniao == 2:
        bom += 1
    else:
        ruim += 1

print("\n===== RESULTADO DA PESQUISA =====")
print(f"Respostas EXCELENTE: {excelente}")
print(f"Respostas RUIM: {ruim}")
