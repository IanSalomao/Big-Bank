# Classe Principal
class usuario():
    def __init__(self, I_numero_conta, I_nome_usuario, I_senha):
        self.n_conta = I_numero_conta
        self.nome_usuario = I_nome_usuario
        self.__senha = I_senha
        self.extrato = 0
        self.debito = 0

    def deposito(self, valor):
        usuario.extrato += valor

    def saque(self, valor):
        if usuario.extrato >= valor:
            usuario.extrato -= valor
            return "Saque concluido"

        else:
            return "Você não tem saldo para fazer este saque"

    def empretimo(self, valor, tempo):
        pass
