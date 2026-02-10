from .item_cardapio import ItemCardapio
from .bebida import Bebida
from .prato import Prato
from rich.table import Table
from rich.console import Console
from rich import box
from typing import List, ClassVar

class Cardapio:
    """
    Esta classe representa a entidade de um cardápio de um restaurante.
    Utiliza composição para gerir uma coleção de instâncias de ItemCardapio.
    """
    
    # Instância única do Console para otimização de recursos (ClassVar)
    console: ClassVar[Console] = Console()
    
    # <------CONSTRUTOR------>
    def __init__(self, title: str) -> None:
        """
        Inicializa a lista de itens como privada para garantir o encapsulamento.
        """
        self._cardapio: List[ItemCardapio] = []
        self._title = title
    
    # <------GETTERS------>
    @property 
    def title(self) -> str:
        return self._title
    @property
    def cardapio(self) -> List[ItemCardapio]:
        """Retorna a lista de itens (somente leitura)."""
        return self._cardapio

    # <------MÉTODOS------>
    def adicionar_item(self, item: ItemCardapio) -> None:
        """Adiciona um novo item ao cardápio, validando a herança."""
        if item and isinstance(item, ItemCardapio):
            self._cardapio.append(item)

    def show_cardapio(self) -> None:
        """
        Renderiza o cardápio formatado no terminal utilizando a biblioteca Rich.
        Aplica polimorfismo para exibir detalhes específicos de cada tipo de item.
        """
        # Configuração da tabela com bordas arredondadas e estilo profissional
        table = Table(
            title=f"[bold magenta]CARDÁPIO: {self.title.upper()}[/]",
            box=box.ROUNDED,
            header_style="bold cyan"
        )

        # Definição das colunas com larguras e estilos específicos
        table.add_column("Índice", justify="center", style="dim")
        table.add_column("Item", style="white", min_width=20)
        table.add_column("Preço", justify="right", style="green")
        table.add_column("Tipo", justify="center", style="yellow")
        table.add_column("Tamanho", justify="center")
        table.add_column("Descrição", style="italic", ratio=1)

        if self._cardapio:
            for c, i in enumerate(self._cardapio, start=1):
                # Formatação de preço para o padrão monetário (R$ 0.00)
                preco_fmt = f"R$ {i.preco:.2f}"
                # Captura segura da descrição caso o atributo exista
                desc = getattr(i, 'descricao', "-") or "-"
                
                if isinstance(i, Bebida):
                    table.add_row(
                        str(c), 
                        i.nome, 
                        preco_fmt, 
                        "Bebida", 
                        i.tamanho, 
                        desc
                    )
                elif isinstance(i, Prato):
                    # Correção: Identificação correta como Prato e uso de placeholder para tamanho
                    table.add_row(
                        str(c), 
                        i.nome, 
                        preco_fmt, 
                        "Prato", 
                        "-", 
                        desc
                    )
            
            # Renderização final via ClassVar
            Cardapio.console.print(table)
            Cardapio.console.print(f"[dim]Total de produtos: {len(self._cardapio)}[/]\n")
        else:
            Cardapio.console.print(f"[yellow]O cardápio de {self.title} está vazio no momento.[/]")

    # <------CONSTRUTOR------>