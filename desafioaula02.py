def obter_nome():
    while True:
        nome = input("Digite seu nome: ").strip()
        if not nome:  # Campo vazio
            print("Você deixou o campo em branco! Tente novamente.")
        elif nome.isdigit():  # Nome numérico
            print("Você digitou seu nome errado. Tente novamente.")
        else:
            return nome


def obter_valor_float(mensagem):
    while True:
        entrada = input(mensagem).strip()
        try:
            valor = float(entrada)
            if valor < 0:  # Verifica valores negativos
                print("O valor não pode ser negativo. Tente novamente.")
            else:
                return valor
        except ValueError:
            print("Valor inválido! Por favor, insira um número válido.")


def main():
    # 1) Solicita o nome do usuário
    nome_usuario = obter_nome()

    # 2) Solicita o salário do usuário
    salario = obter_valor_float(f"{nome_usuario}, qual o seu salário mensal? ")

    # 3) Solicita a porcentagem do bônus recebido
    bonus_porcentagem = obter_valor_float(f"{nome_usuario}, qual a porcentagem de aumento teve esse ano? ")

    # 4) Calcula o valor do bônus final
    valor_bonus = salario * (bonus_porcentagem / 100)
    novo_salario = salario + valor_bonus

    # 5) Exibe a mensagem final personalizada
    print(
        f"Certo, {nome_usuario}! Seu salário é de R$ {salario:.2f} "
        f"e você teve um bônus de {bonus_porcentagem:.2f}%. "
        f"Com isso, você teve um aumento de R$ {valor_bonus:.2f} "
        f"e seu salário ficou em R$ {novo_salario:.2f}."
    )


# Executa o programa principal
if __name__ == "__main__":
    main()
