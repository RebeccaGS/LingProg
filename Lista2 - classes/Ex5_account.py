'''
Classe Conta Corrente: Crie uma classe para implementar uma conta corrente.
A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo.
Os métodos são os seguintes: alterarNome, depósito e saque; No construtor, saldo é opcional,
com valor default zero e os demais atributos são obrigatórios.
'''

class Account:
    def __init__(self, numberAccount, name, balance = 0):
        self.numberAccount = numberAccount
        self.name = name
        self.balance = balance

    # Func para mudar nome
    def changeName(self, name):
        self.name = name
        return self.name

    # Func para depositar dinheiro
    def deposit(self, deposit):
        self.balance = self.balance + deposit
        return self.balance

    # Func para sacar dinheiro, diminui saque do saldo    
    def withDraw(self, withDraw):
        self.balance = self.balance - withDraw
        return self.balance
    
rebecca = Account('004926', 'Rebecca Gomes', 700)
rebecca.deposit(30)
rebecca.withDraw(70)
rebecca.changeName('Amanda')
print(f'The {rebecca.numberAccount} account belongs to {rebecca.name} that has {rebecca.balance} R$.')
