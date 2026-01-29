"""
Herança e Polimorfismo em Python
================================

Exemplos completos para a aula de POO.

Autor: Prof. Edson José Pacheco
Disciplina: TE328 
"""

from abc import ABC, abstractmethod
from typing import List
import json
import math


# =============================================================================
# EXEMPLO 1: HERANÇA BÁSICA
# =============================================================================

print("=" * 60)
print("EXEMPLO 1: Herança Básica")
print("=" * 60)


class Animal:
    """Classe base (superclasse)."""
    
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade
    
    def comer(self) -> None:
        print(f"{self.nome} está comendo.")
    
    def dormir(self) -> None:
        print(f"{self.nome} está dormindo.")
    
    def __str__(self) -> str:
        return f"{self.__class__.__name__}(nome={self.nome}, idade={self.idade})"


class Cachorro(Animal):
    """Classe derivada (subclasse)."""
    
    def __init__(self, nome: str, idade: int, raca: str):
        # Chama construtor da classe base
        super().__init__(nome, idade)
        self.raca = raca
    
    def latir(self) -> None:
        """Método específico da subclasse."""
        print(f"{self.nome} faz: Au Au!")
    
    def comer(self) -> None:
        """Sobrescrita (override) do método da base."""
        print(f"{self.nome} devora a ração rapidamente!")


class Gato(Animal):
    """Outra subclasse."""
    
    def __init__(self, nome: str, idade: int, pelagem: str):
        super().__init__(nome, idade)
        self.pelagem = pelagem
    
    def miar(self) -> None:
        print(f"{self.nome} faz: Miau!")
    
    def comer(self) -> None:
        # Chama implementação da base E adiciona comportamento
        super().comer()
        print("E lambe os bigodes.")


# Demonstração
rex = Cachorro("Rex", 5, "Pastor Alemão")
mimi = Gato("Mimi", 3, "Branca")

print(f"\n{rex}")
rex.comer()      # Versão sobrescrita
rex.dormir()     # Herdado da base
rex.latir()      # Específico

print(f"\n{mimi}")
mimi.comer()     # Chama super().comer() + adiciona


# =============================================================================
# EXEMPLO 2: CLASSES ABSTRATAS
# =============================================================================

print("\n" + "=" * 60)
print("EXEMPLO 2: Classes Abstratas")
print("=" * 60)


class Forma(ABC):
    """Classe abstrata - não pode ser instanciada."""
    
    def __init__(self, cor: str):
        self.cor = cor
    
    @abstractmethod
    def area(self) -> float:
        """Método abstrato - DEVE ser implementado."""
        pass
    
    @abstractmethod
    def perimetro(self) -> float:
        """Outro método abstrato."""
        pass
    
    def descricao(self) -> str:
        """Método concreto - pode ser herdado."""
        return f"Forma {self.cor} com área {self.area():.2f}"


class Circulo(Forma):
    """Implementação concreta."""
    
    def __init__(self, cor: str, raio: float):
        super().__init__(cor)
        self.raio = raio
    
    def area(self) -> float:
        return math.pi * self.raio ** 2
    
    def perimetro(self) -> float:
        return 2 * math.pi * self.raio


class Retangulo(Forma):
    """Outra implementação concreta."""
    
    def __init__(self, cor: str, largura: float, altura: float):
        super().__init__(cor)
        self.largura = largura
        self.altura = altura
    
    def area(self) -> float:
        return self.largura * self.altura
    
    def perimetro(self) -> float:
        return 2 * (self.largura + self.altura)


# Demonstração de polimorfismo
formas: List[Forma] = [
    Circulo("azul", 5),
    Retangulo("vermelho", 4, 3),
    Circulo("verde", 2.5)
]

print("\nPolimorfismo em ação:")
for forma in formas:
    print(f"  {forma.descricao()}, perímetro: {forma.perimetro():.2f}")

# Tentativa de instanciar classe abstrata (descomente para ver o erro):
# forma = Forma("amarelo")  # TypeError!


# =============================================================================
# EXEMPLO 3: @property
# =============================================================================

print("\n" + "=" * 60)
print("EXEMPLO 3: @property")
print("=" * 60)


class ContaBancaria:
    """Demonstra uso de @property para encapsulamento."""
    
    def __init__(self, titular: str, saldo_inicial: float = 0):
        self._titular = titular
        self._saldo = saldo_inicial
        self._historico: List[str] = []
    
    @property
    def titular(self) -> str:
        """Propriedade somente leitura."""
        return self._titular
    
    @property
    def saldo(self) -> float:
        """Getter para saldo."""
        return self._saldo
    
    @saldo.setter
    def saldo(self, valor: float) -> None:
        """Setter com validação."""
        if valor < 0:
            raise ValueError("Saldo não pode ser negativo!")
        self._saldo = valor
    
    @property
    def historico(self) -> List[str]:
        """Retorna cópia do histórico (protege o original)."""
        return self._historico.copy()
    
    def depositar(self, valor: float) -> None:
        if valor <= 0:
            raise ValueError("Valor deve ser positivo!")
        self._saldo += valor
        self._historico.append(f"Depósito: +R$ {valor:.2f}")
    
    def sacar(self, valor: float) -> bool:
        if valor > self._saldo:
            self._historico.append(f"Saque negado: R$ {valor:.2f}")
            return False
        self._saldo -= valor
        self._historico.append(f"Saque: -R$ {valor:.2f}")
        return True


# Demonstração
conta = ContaBancaria("João Silva", 1000)
print(f"\nTitular: {conta.titular}")
print(f"Saldo: R$ {conta.saldo:.2f}")

conta.depositar(500)
conta.sacar(200)
conta.sacar(2000)  # Negado

print(f"Saldo final: R$ {conta.saldo:.2f}")
print(f"Histórico: {conta.historico}")

# Tentativa de alterar titular (erro):
# conta.titular = "Maria"  # AttributeError!


# =============================================================================
# EXEMPLO 4: @classmethod e @staticmethod
# =============================================================================

print("\n" + "=" * 60)
print("EXEMPLO 4: @classmethod e @staticmethod")
print("=" * 60)


class Data:
    """Demonstra classmethod e staticmethod."""
    
    def __init__(self, dia: int, mes: int, ano: int):
        self.dia = dia
        self.mes = mes
        self.ano = ano
    
    @classmethod
    def hoje(cls) -> "Data":
        """Factory method - cria instância com data atual."""
        from datetime import date
        d = date.today()
        return cls(d.day, d.month, d.year)
    
    @classmethod
    def from_string(cls, data_str: str) -> "Data":
        """Factory method - cria a partir de string."""
        dia, mes, ano = map(int, data_str.split('/'))
        return cls(dia, mes, ano)
    
    @staticmethod
    def eh_bissexto(ano: int) -> bool:
        """Método utilitário - não precisa de instância."""
        return ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)
    
    @staticmethod
    def dias_no_mes(mes: int, ano: int) -> int:
        """Outro método utilitário."""
        if mes in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif mes in [4, 6, 9, 11]:
            return 30
        else:  # Fevereiro
            return 29 if Data.eh_bissexto(ano) else 28
    
    def __str__(self) -> str:
        return f"{self.dia:02d}/{self.mes:02d}/{self.ano}"


# Demonstração
d1 = Data(25, 12, 2024)
d2 = Data.hoje()
d3 = Data.from_string("01/01/2025")

print(f"\nData manual: {d1}")
print(f"Data hoje: {d2}")
print(f"Data de string: {d3}")
print(f"2024 é bissexto? {Data.eh_bissexto(2024)}")
print(f"Dias em fev/2024: {Data.dias_no_mes(2, 2024)}")


# =============================================================================
# EXEMPLO 5: HERANÇA MÚLTIPLA E MIXINS
# =============================================================================

print("\n" + "=" * 60)
print("EXEMPLO 5: Herança Múltipla e Mixins")
print("=" * 60)


class JSONMixin:
    """Mixin para serialização JSON."""
    
    def to_json(self) -> str:
        return json.dumps(self.__dict__, indent=2)
    
    @classmethod
    def from_json(cls, json_str: str):
        data = json.loads(json_str)
        return cls(**data)


class ComparableMixin:
    """Mixin para comparação."""
    
    @property
    @abstractmethod
    def valor_comparacao(self):
        """Deve retornar valor para comparação."""
        pass
    
    def __lt__(self, other):
        return self.valor_comparacao < other.valor_comparacao
    
    def __le__(self, other):
        return self.valor_comparacao <= other.valor_comparacao
    
    def __gt__(self, other):
        return self.valor_comparacao > other.valor_comparacao
    
    def __ge__(self, other):
        return self.valor_comparacao >= other.valor_comparacao


class Produto(JSONMixin):
    """Classe que usa mixin."""
    
    def __init__(self, nome: str, preco: float, estoque: int = 0):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
    
    def __str__(self) -> str:
        return f"{self.nome}: R$ {self.preco:.2f} ({self.estoque} un.)"


# Demonstração
p = Produto("Notebook", 3500.00, 10)
print(f"\n{p}")

# Serialização JSON via mixin
json_str = p.to_json()
print(f"JSON:\n{json_str}")

# Deserialização
p2 = Produto.from_json('{"nome": "Mouse", "preco": 99.90, "estoque": 50}')
print(f"De JSON: {p2}")


# =============================================================================
# EXEMPLO 6: MRO - METHOD RESOLUTION ORDER
# =============================================================================

print("\n" + "=" * 60)
print("EXEMPLO 6: MRO (Problema do Diamante)")
print("=" * 60)


class A:
    def metodo(self):
        print("  A.metodo()")


class B(A):
    def metodo(self):
        print("  B.metodo()")
        super().metodo()


class C(A):
    def metodo(self):
        print("  C.metodo()")
        super().metodo()


class D(B, C):
    def metodo(self):
        print("  D.metodo()")
        super().metodo()


# Demonstração
print(f"\nMRO de D: {[c.__name__ for c in D.__mro__]}")
print("\nChamando d.metodo():")
d = D()
d.metodo()


# =============================================================================
# EXEMPLO 7: PADRÃO STATE COMPLETO (TORNIQUETE)
# =============================================================================

print("\n" + "=" * 60)
print("EXEMPLO 7: Padrão State - Torniquete")
print("=" * 60)


class EstadoTorniquete(ABC):
    """Interface abstrata para estados."""
    
    @abstractmethod
    def moeda(self, torniquete: "TorniqueteCompleto") -> None:
        pass
    
    @abstractmethod
    def empurrar(self, torniquete: "TorniqueteCompleto") -> None:
        pass
    
    def __str__(self) -> str:
        return self.__class__.__name__


class Travado(EstadoTorniquete):
    """Estado concreto: travado."""
    
    def moeda(self, torniquete: "TorniqueteCompleto") -> None:
        print("  🪙 Moeda aceita! Destravando...")
        torniquete._estado = Destravado()
    
    def empurrar(self, torniquete: "TorniqueteCompleto") -> None:
        print("  🚫 Bloqueado! Insira uma moeda.")
        print("  🔔 ALARME!")


class Destravado(EstadoTorniquete):
    """Estado concreto: destravado."""
    
    def moeda(self, torniquete: "TorniqueteCompleto") -> None:
        print("  🪙 Moeda extra ignorada (já destravado).")
    
    def empurrar(self, torniquete: "TorniqueteCompleto") -> None:
        print("  🚶 Passagem liberada! Travando...")
        torniquete._estado = Travado()


class TorniqueteCompleto:
    """Contexto - delega comportamento ao estado."""
    
    def __init__(self):
        self._estado: EstadoTorniquete = Travado()
        print("═" * 40)
        print("  TORNIQUETE INICIADO")
        print("═" * 40)
    
    @property
    def estado(self) -> str:
        """Property somente leitura."""
        return str(self._estado)
    
    def moeda(self) -> None:
        print(f"\n[{self.estado}] → MOEDA")
        self._estado.moeda(self)
        print(f"[Novo estado: {self.estado}]")
    
    def empurrar(self) -> None:
        print(f"\n[{self.estado}] → EMPURRAR")
        self._estado.empurrar(self)
        print(f"[Novo estado: {self.estado}]")


def main():
    # Demonstração
    t = TorniqueteCompleto()

    print("\n--- Fluxo normal ---")
    t.moeda()
    t.empurrar()

    print("\n--- Empurrar sem pagar ---")
    t.empurrar()

    print("\n--- Moeda extra ---")
    t.moeda()
    t.moeda()
    t.empurrar()


    # =============================================================================
    # RESUMO FINAL
    # =============================================================================

    print("\n" + "=" * 60)
    print("RESUMO: Conceitos de Herança em Python")
    print("=" * 60)
    print("""
    ┌─────────────────────────────────────────────────────────┐
    │  HERANÇA BÁSICA                                         │
    │    class Filha(Pai):                                    │
    │        def __init__(self, ...):                         │
    │            super().__init__(...)  # Chama construtor    │
    ├─────────────────────────────────────────────────────────┤
    │  CLASSES ABSTRATAS                                      │
    │    from abc import ABC, abstractmethod                  │
    │    class MinhaInterface(ABC):                           │
    │        @abstractmethod                                  │
    │        def metodo_obrigatorio(self): pass               │
    ├─────────────────────────────────────────────────────────┤
    │  DECORATORS                                             │
    │    @property          → getter/setter elegante          │
    │    @classmethod       → factory methods (recebe cls)    │
    │    @staticmethod      → utilitários (sem self/cls)      │
    │    @abstractmethod    → método obrigatório              │
    ├─────────────────────────────────────────────────────────┤
    │  HERANÇA MÚLTIPLA                                       │
    │    class D(B, C):     → MRO resolve conflitos           │
    │    Mixins             → composição de comportamentos    │
    └─────────────────────────────────────────────────────────┘
    """)

if __name__ == "__main__":
    main()
