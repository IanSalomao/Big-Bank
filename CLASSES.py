# Classe Principal
class usuario():
    def __init__(self, I_numero_conta, I_nome_usuario, I_senha):
        self.n_conta = I_numero_conta
        self.nome_usuario = I_nome_usuario
        self.__senha = I_senha
        self.saldo = 0
        self.debito = 0

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        if self.extrato >= valor:
            self.extrato -= valor
            return "Saque concluido"

        else:
            return "Você não tem saldo suficiente para fazer este saque"

    def extrato(self):
            print(f"Titular: {self.nome_usuario}\nNumero da Conta: {self.n_conta}\nSaldo: R${self.saldo:.2f}\n")

    def empretimo(self, valor, tempo):
        pass
