Pu = int(input("insira a potencia util do motor: "))
n = float(input("insira o rendimento do motor: "))
P = Pu / n
FP = float(input("insira o valor do fator de potencia: "))
S = P / FP
Q = (S**2 - P**2 )**0.5
print(f"a potencia ativa sera {P} Watts")
print(f"a potencia aparente é {S}VA e a potencia reativa é {Q}VAr")
