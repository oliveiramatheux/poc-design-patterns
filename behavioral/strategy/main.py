from abc import ABC, abstractmethod

# Interface da estratégia (classe abstrata)


class ValidacaoStrategy(ABC):
    @abstractmethod
    def validar(self, valor):
        """Valida o valor fornecido"""
        pass

    @abstractmethod
    def get_mensagem_erro(self):
        """Retorna a mensagem de erro para esta validação"""
        pass

# Validação de Email


class ValidacaoEmail(ValidacaoStrategy):
    def validar(self, email):
        # Validação simplificada de email (contém @ e .)
        return email is not None and "@" in email and "." in email

    def get_mensagem_erro(self):
        return "Email inválido. Deve conter @ e ."

# Validação de Senha


class ValidacaoSenha(ValidacaoStrategy):
    def validar(self, senha):
        # Senha precisa ter pelo menos 8 caracteres
        return senha is not None and len(senha) >= 8

    def get_mensagem_erro(self):
        return "Senha inválida. Deve ter pelo menos 8 caracteres."

# Validação de Nome


class ValidacaoNome(ValidacaoStrategy):
    def validar(self, nome):
        # Nome não pode estar vazio e deve ter pelo menos 3 caracteres
        return nome is not None and nome.strip() != "" and len(nome) >= 3

    def get_mensagem_erro(self):
        return "Nome inválido. Deve ter pelo menos 3 caracteres."


# Classe que utiliza a estratégia
class CampoFormulario:
    def __init__(self, nome, estrategia):
        self.nome = nome
        self.valor = None
        self.estrategia = estrategia

    def set_valor(self, valor):
        self.valor = valor

    def validar(self):
        return self.estrategia.validar(self.valor)

    def get_nome(self):
        return self.nome

    def get_mensagem_erro(self):
        return self.estrategia.get_mensagem_erro()

# Classe que gerencia múltiplos campos


class Formulario:
    def __init__(self):
        self.campos = []

    def adicionar_campo(self, campo):
        self.campos.append(campo)

    def validar_tudo(self):
        todos_validos = True

        for campo in self.campos:
            if not campo.validar():
                print(
                    f"Erro no campo {campo.get_nome()}: {campo.get_mensagem_erro()}")
                todos_validos = False

        return todos_validos


def main():
    # Criar formulário
    formulario = Formulario()

    # Adicionar campos com suas respectivas estratégias de validação
    campo_nome = CampoFormulario("nome", ValidacaoNome())
    campo_email = CampoFormulario("email", ValidacaoEmail())
    campo_senha = CampoFormulario("senha", ValidacaoSenha())

    formulario.adicionar_campo(campo_nome)
    formulario.adicionar_campo(campo_email)
    formulario.adicionar_campo(campo_senha)

    # Simular entrada de dados do usuário
    campo_nome.set_valor("Jo")  # Nome muito curto
    campo_email.set_valor("emailinvalido")  # Email sem @ e .
    campo_senha.set_valor("123")  # Senha muito curta

    # Validar formulário
    resultado = formulario.validar_tudo()
    print(
        f"Resultado da validação: {'Formulário válido' if resultado else 'Formulário com erros'}")

    # Corrigir os dados
    print("\nCorrigindo dados...")
    campo_nome.set_valor("João Silva")
    campo_email.set_valor("joao@example.com")
    campo_senha.set_valor("senha12345")

    # Validar novamente
    resultado = formulario.validar_tudo()
    print(
        f"\nResultado da nova validação: {'Formulário válido' if resultado else 'Formulário com erros'}")


if __name__ == "__main__":
    main()
