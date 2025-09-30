class Processador:
    def __init__(self, modelo: str, velocidade_ghz: float):
        self._modelo = modelo
        self._velocidade_ghz = velocidade_ghz

    def get_modelo(self) -> str:
        return self._modelo

    def get_velocidade_ghz(self) -> float:
        return self._velocidade_ghz

    def __str__(self):
        return f"processador: {self.get_modelo()} @ {self.get_velocidade_ghz():.2f} GHz"

#classe processador e suas funçoes
class MemoriaRAM:
    def __init__(self, capacidade_gb: int, tipo: str):
        self._capacidade_gb = capacidade_gb
        self._tipo = tipo

    def get_capacidade_gb(self) -> int:
        return self._capacidade_gb

    def get_tipo(self) -> str:
        return self._tipo

    def __str__(self):
        return f"memória RAM: {self.get_capacidade_gb()} GB ({self.get_tipo()})"

#classe memoriaRAM e suas funçoes
class Armazenamento:
    def __init__(self, tipo: str, capacidade_gb: int):
        if tipo.upper() not in ['SSD', 'HDD']:
            raise ValueError("tipo de armazenamento inválido use SSD ou HDD.")
        self._tipo = tipo.upper()
        self._capacidade_gb = capacidade_gb

    def get_tipo(self) -> str:
        return self._tipo

    def get_capacidade_gb(self) -> int:
        return self._capacidade_gb

    def __str__(self):
        return f"armazenamento: {self.get_tipo()} de {self.get_capacidade_gb()} GB"

#classe armazenamento e suas funçoes
class Computador:
    def __init__(self, marca: str, modelo: str, proc_modelo: str, proc_velocidade: float,
                 ram_capacidade: int, ram_tipo: str, arm_tipo: str, arm_capacidade: int):
        self._marca = marca
        self._modelo = modelo
        
        self._processador = Processador(proc_modelo, proc_velocidade)
        self._memoria_ram = MemoriaRAM(ram_capacidade, ram_tipo)
        self._armazenamento = Armazenamento(arm_tipo, arm_capacidade)

    def get_marca(self) -> str:
        return self._marca

    def get_modelo(self) -> str:
        return self._modelo

    def get_processador(self) -> Processador:
        return self._processador

    def get_memoria_ram(self) -> MemoriaRAM:
        return self._memoria_ram

    def get_armazenamento(self) -> Armazenamento:
        return self._armazenamento

    def ligar(self):
        print(f"\nligando {self.get_marca()} {self.get_modelo()} ---")
        print("especificações Carregadas:")
        
        print(f"  CPU: {self.get_processador().get_modelo()} @ {self.get_processador().get_velocidade_ghz():.2f} GHz")
        print(f"  RAM: {self.get_memoria_ram().get_capacidade_gb()} GB ({self.get_memoria_ram().get_tipo()})")
        print(f"  armazenamento: {self.get_armazenamento().get_tipo()} de {self.get_armazenamento().get_capacidade_gb()} GB")
        
        print(f"sistema operacional inicializado.")
        return self

    def __str__(self):
        return (f"Computador: {self.get_marca()} {self.get_modelo()}\n"
                f"{self.get_processador()}\n"
                f"{self.get_memoria_ram()}\n"
                f"{self.get_armazenamento()}")
    
#classe computaddor e suas funçoes

print("criação do objeto computador ---")
meu_computador = Computador(
    marca="TechCorp",
    modelo="XPS-Ultra",
    proc_modelo="Core i9-12900K",
    proc_velocidade=3.2,
    ram_capacidade=32,
    ram_tipo="DDR5",
    arm_tipo="SSD",
    arm_capacidade=1000
)

print("\ndetalhes do computador (usando print/str) ---")
print(meu_computador)

print("\nchamada de ligar() com encadeamento ---")
meu_computador.ligar()

print(f"\nverificação: modelo da CPU através do getter: {meu_computador.get_processador().get_modelo()}")

print("\ndemonstração de dependência de ciclo de vida (composição) ---")
try:
    processador_ref = meu_computador.get_processador()
    print(f"referência direta ao processador (ANTES da destruição): {processador_ref}")

    print("destruindo o objeto 'meu_computador'...")
    del meu_computador
    
    print(f"referência direta ao processador (DEPOIS da destruição do computador): {processador_ref.get_modelo()}")
    print("o processador ainda pode ser acessado, pois uma referência ('processador_ref') foi criada.")

    print("tentando acessar 'meu_computador'...")
    meu_computador.ligar() 
except NameError as e:
    print(f"SUCESSO: {e}. o objeto computador não existe")