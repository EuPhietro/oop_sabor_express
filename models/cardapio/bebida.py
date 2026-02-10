from .item_cardapio import ItemCardapio
from typing import Optional

class Bebida(ItemCardapio):
    """
    Representa uma especialização da classe ItemCardapio.
    Herda os atributos fundamentais (nome, preco) e adiciona características
    específicas de bebidas (tamanho, descricao).
    """

    # <------CONSTRUTOR------>
    def __init__(self, nome: str, preco: float, tamanho: str, descricao: Optional[str] = None) -> None:
        """
        Inicializa a instância chamando o construtor da superclasse.
        As atribuições são feitas via propriedades para garantir a validação dos dados.
        """
        super().__init__(nome, preco)
        self.tamanho = tamanho
        self.descricao = descricao

    # <------GETTERS------>
    @property
    def tamanho(self) -> str:
        """Retorna o volume ou dimensão da bebida (ex: 300ml, 1L)."""
        return self._tamanho

    @property
    def descricao(self) -> Optional[str]:
        """Retorna a descrição detalhada do produto, podendo ser None."""
        return self._descricao

    # <------SETTERS------>
    @tamanho.setter
    def tamanho(self, value: str) -> None:
        """
        Define o tamanho da bebida.
        Valida se a string não está vazia ou preenchida apenas com espaços.
        """
        if not value or not value.strip():
            raise ValueError(f"O valor '{value}' é inválido. O tamanho não pode ser vazio.")
        self._tamanho = value.strip()

    @descricao.setter
    def descricao(self, value: Optional[str]) -> None:
        """
        Define a descrição da bebida.
        Utiliza lógica de Truthiness para converter strings vazias em None.
        """
        if value and value.strip():
            self._descricao = value.strip()
        else:
            self._descricao = None

    # <------INTERFACE METHODS------>
    def aplicar_desconto(self,tax=0.3):
        self.preco = self.preco - (self.preco * tax) 
    # <------DUNDER METHODS------>
    def __str__(self) -> str:
        """
        Representação textual polimórfica.
        Exibe os dados básicos da superclasse acrescidos dos detalhes da bebida.
        """
        return super().__str__()
