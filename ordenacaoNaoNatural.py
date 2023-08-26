from operator import attrgetter
from functools import total_ordering
@total_ordering #para conseguir ter as operações maior/menor igual que
class ContaSalario:

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def __eq__(self, outro):
        if type(outro) != ContaSalario:
            return False

        return self._codigo == outro._codigo and self._saldo == outro._saldo

    def __lt__(self, outro): #menor que / less than
        if self._saldo != outro._saldo:
            return self._saldo < outro._saldo
        else:
            return self._codigo < outro._codigo

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return "[>>Codigo {} Saldo {}<<]".format(self._codigo, self._saldo)



conta_do_guilherme = ContaSalario(55)
conta_da_ana = ContaSalario(43)
conta_da_julia = ContaSalario(45)
conta_da_ana.deposita(500)
conta_da_julia.deposita(600)
conta_do_guilherme.deposita(700)

contas = [conta_do_guilherme, conta_da_ana, conta_da_julia]
for conta in sorted(contas):
    print(conta)
print(sorted(contas))


for conta in sorted(contas, key=attrgetter("_saldo")): #para acessar o saldo da conta mesmo ele sendo privado
    print(conta)



