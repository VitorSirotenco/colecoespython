class ContaSalario:

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def __eq__(self, outro):
        if type(outro) != ContaSalario:
            return False

        return self._codigo == outro._codigo and self._saldo == outro._saldo

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return "[>>Codigo {} Saldo {}<<]".format(self._codigo, self._saldo)


class ContaCorrente:

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0




conta1 = ContaSalario(50)
conta2 = ContaSalario(50)
conta3 = ContaCorrente(50)

conta1.deposita(100)
conta2.deposita(100)

print(conta3 == conta2)





