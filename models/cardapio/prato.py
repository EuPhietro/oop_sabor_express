from .item_cardapio import ItemCardapio
from typing import Optional

class Prato(ItemCardapio):
    """
    Representa uma especialização da classe ItemCardapio focada em pratos de comida.
    Herda atributos fundamentais e adiciona uma descrição detalhada.
    """

    # <------CONSTRUTOR------>
    def __init__(self, nome: str, preco: float, descricao: str) -> None:
        """
        Inicializa o prato utilizando a superclasse e valida a descrição.
        A herança garante que nome e preço sigam as regras da classe base.
        """
        super().__init__(nome, preco)
        # Atribuição via propriedade para disparar o setter
        self.descricao = descricao

    # <------GETTERS------>
    @property
    def descricao(self) -> Optional[str]:
        """Retorna a descrição detalhada do prato."""
        return self._descricao

    # <------SETTERS------>
    @descricao.setter
    def descricao(self, valor: Optional[str]) -> None:
        """
        Define a descrição do prato. 
        Utiliza Truthiness para tratar strings vazias ou nulas como None.
        """
        if valor and valor.strip():
            self._descricao = valor.strip()
        else:
            self._descricao = None

    # <------INTERFACE METHODS------>
    def aplicar_desconto(self,tax=0.2):
        self.preco = self.preco - (self.preco * tax) 


    # <------DUNDER METHODS------>
    def __str__(self) -> str:
        """
        Método polimórfico: estende a representação da superclasse 
        adicionando a descrição específica do prato.
        """
        base_info = super().__str__()
        if self.descricao:
            return f"{base_info} | Descrição: {self.descricao}"
        return base_info