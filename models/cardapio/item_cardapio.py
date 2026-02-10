from abc import ABC, abstractmethod
# O que é uma classe abstrata: Uma classe abstrata serve apenas para servir de superclasse, molde, ou base para outras classes, ela não é uma classe concreta e tem como ob
class ItemCardapio(ABC): 
    """
    Esta classe é uma superclasse usada para representar um item qualquer no cardápio.
    """

    # <------CONSTRUTOR------>
    def __init__(self, nome: str, preco: float) -> None:
        """
        Inicializa o item utilizando as propriedades para garantir a validação imediata.
        """
        # Encapsulamento através de setters
        self.nome = nome
        self.preco = preco

    # <------GETTERS------>
    @property
    def nome(self) -> str:
        return self._nome

    @property
    def preco(self) -> float:
        return self._preco

    # <------SETTERS------>
    @nome.setter
    def nome(self, novo_nome: str) -> None:
        # Verifica se a string está vazia ou contém apenas espaços
        if not novo_nome or not novo_nome.strip():
            raise ValueError(f"'{novo_nome}' é inválido. O nome não pode ser vazio ou None.")
        else:  
            # Limpa espaços extras e capitaliza cada palavra
            self._nome = novo_nome.strip().title()

    @preco.setter
    def preco(self, novo_preco: float) -> None:
        if novo_preco < 0:
            raise ValueError(f"R$ {novo_preco} é inválido. O preço não pode ser negativo.")
        # Arredonda para 2 casas decimais, ideal para valores monetários
        self._preco = round(novo_preco, 2)
    # <------INSTANCE METHODS------>
    @abstractmethod 
    def aplicar_desconto(self,tax = 0.0):
        """Método de assinatura que todas as subclasses devem"""

        pass

    # <------DUNDER METHODS------>
    def __str__(self) -> str:
        """Retorna uma representação formatada do item."""
        return f"Item: {self.nome} | Preço: R$ {self.preco:.2f}"
    
    # <------CONSTRUTOR------>
    # Nota: O bloco final foi mantido conforme sua estrutura de marcação visual.