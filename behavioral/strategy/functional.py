def main():
    # Definir estratégias de validação como funções
    validacao_email = {
        "validar": lambda email: email is not None and "@" in email and "." in email,
        "mensagem_erro": "Email inválido. Deve conter @ e ."
    }

    validacao_senha = {
        "validar": lambda senha: senha is not None and len(senha) >= 8,
        "mensagem_erro": "Senha inválida. Deve ter pelo menos 8 caracteres."
    }

    validacao_nome = {
        "validar": lambda nome: nome is not None and nome.strip() != "" and len(nome) >= 3,
        "mensagem_erro": "Nome inválido. Deve ter pelo menos 3 caracteres."
    }

    # Criar campo de formulário como uma função
    def criar_campo(nome, estrategia):
        campo = {
            "nome": nome,
            "valor": None,
            "estrategia": estrategia
        }

        # Definir métodos do campo
        def set_valor(valor):
            campo["valor"] = valor

        campo["set_valor"] = set_valor
        campo["validar"] = lambda: estrategia["validar"](campo["valor"])
        campo["get_nome"] = lambda: nome
        campo["get_mensagem_erro"] = lambda: estrategia["mensagem_erro"]

        return campo

    # Criar formulário
    formulario = []

    # Criar campos
    campo_nome = criar_campo("nome", validacao_nome)
    campo_email = criar_campo("email", validacao_email)
    campo_senha = criar_campo("senha", validacao_senha)

    # Adicionar campos ao formulário
    formulario.extend([campo_nome, campo_email, campo_senha])

    # Função para validar todo o formulário
    def validar_formulario():
        todos_validos = True

        for campo in formulario:
            if not campo["validar"]():
                print(
                    f"Erro no campo {campo['nome']}: {campo['estrategia']['mensagem_erro']}")
                todos_validos = False

        return todos_validos

    # Simular entrada de dados do usuário
    campo_nome["set_valor"]("Jo")  # Nome muito curto
    campo_email["set_valor"]("emailinvalido")  # Email sem @ e .
    campo_senha["set_valor"]("123")  # Senha muito curta

    # Validar formulário
    resultado = validar_formulario()
    print(
        f"Resultado da validação: {'Formulário válido' if resultado else 'Formulário com erros'}")

    # Corrigir os dados
    print("\nCorrigindo dados...")
    campo_nome["set_valor"]("João Silva")
    campo_email["set_valor"]("joao@example.com")
    campo_senha["set_valor"]("senha12345")

    # Validar novamente
    resultado = validar_formulario()
    print(
        f"\nResultado da nova validação: {'Formulário válido' if resultado else 'Formulário com erros'}")


if __name__ == "__main__":
    main()
