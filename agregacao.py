class Funcionario:
    def __init__(self, nome, cargo, salario):
        self._nome = nome
        self._cargo = cargo
        self._salario = salario

    def get_nome(self):
        return self._nome

    def get_cargo(self):
        return self._cargo

    def get_salario(self):
        return self._salario

    def __str__(self):
        return f"Funcionário: {self.get_nome()} | Cargo: {self.get_cargo()} | Salário: R${self.get_salario():.2f}"

    def __repr__(self):
        return f"Funcionario(nome='{self.get_nome()}', cargo='{self.get_cargo()}')"

#Primeira classe, funcionario
class Empresa:
    def __init__(self, nome_empresa, cnpj):
        self._nome_empresa = nome_empresa
        self._cnpj = cnpj
        self._funcionarios = []

    def get_nome_empresa(self):
        return self._nome_empresa

    def get_cnpj(self):
        return self._cnpj

    def get_funcionarios(self):
        return list(self._funcionarios)

    def contratar_funcionario(self, funcionario: Funcionario):
        if funcionario not in self._funcionarios:
            self._funcionarios.append(funcionario)
            print(f"-> {funcionario.get_nome()} CONTRATADO por {self.get_nome_empresa()}.")
        else:
            print(f"-> {funcionario.get_nome()} JÁ está na lista de funcionários de {self.get_nome_empresa()}.")
        return self 

    def demitir_funcionario(self, funcionario: Funcionario):
        try:
            self._funcionarios.remove(funcionario)
            print(f"-> {funcionario.get_nome()} DEMITIDO de {self.get_nome_empresa()}.")
        except ValueError:
            print(f"-> ERRO: {funcionario.get_nome()} NÃO é funcionário de {self.get_nome_empresa()}.")
        return self 

    def listar_funcionarios(self):
        print(f"\n--- Funcionários de {self.get_nome_empresa()} ({self.get_cnpj()}) ---")
        if not self._funcionarios:
            print("Nenhum funcionário cadastrado.")
            return

        for func in self._funcionarios:
            nome = func.get_nome()
            cargo = func.get_cargo()
            salario = func.get_salario()
            print(f"[+] Nome: {nome}, Cargo: {cargo}, Salário: R${salario:.2f}")

    def __str__(self):
        return f"Empresa: {self.get_nome_empresa()} | CNPJ: {self.get_cnpj()} | Total de Funcionários: {len(self._funcionarios)}"

#Segunda classe, empresa

print("  inicio cenario teste: Agregação")

func1 = Funcionario("Alice Silva", "Desenvolvedora Jr", 3500.00)
func2 = Funcionario("Bruno Costa", "Analista de RH Pleno", 6200.50)
func3 = Funcionario("Carla Souza", "Gerente de Projetos", 12500.00)

print("Objetos Funcionário Criados:")
print(f"Func1: {func1}")
print(f"Func2: {func2}")
print(f"Func3: {func3}\n")

empresa_a = Empresa("Tech Solutions Ltda", "01.234.567/0001-89")
print(f"Empresa Criada: {empresa_a}\n")

print("Contratações (Utilizando Encadeamento de Métodos)")
empresa_a.contratar_funcionario(func1).contratar_funcionario(func2).contratar_funcionario(func3)
print(f"\nEmpresa A após contratações: {empresa_a}\n")

empresa_a.listar_funcionarios()

print("Demissão (Utilizando Encadeamento de Métodos)")
empresa_a.demitir_funcionario(func2).demitir_funcionario(func1)

empresa_a.listar_funcionarios()

print("\nVerificação de Existência Pós-Demissão (Agregação)")
print(f"O objeto func2 ainda existe? SIM!")
print(f"Nome do func2 demitido: {func2.get_nome()}")
print(f"Cargo do func2 demitido: {func2.get_cargo()}")
print(f"Salário do func2 demitido: R${func2.get_salario():.2f}")

print("\nContratação em Nova Empresa (Independência de Ciclo de Vida)")
empresa_b = Empresa("Nova StartUp S.A.", "98.765.432/0001-11")


empresa_b.contratar_funcionario(func2)

print(f"\nEmpresa A: {empresa_a}")
print(f"Empresa B: {empresa_b}")

empresa_b.listar_funcionarios()

print("FIM DO CENÁRIO DE TESTE")
