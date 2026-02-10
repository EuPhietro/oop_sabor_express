from rich.traceback import install
from .cardapio import (ItemCardapio, Cardapio, Prato, Bebida)
from rich import inspect
from .avaliacao import Avaliacao

# <-------- CONFIGURAÇÃO DE AMBIENTE -------->
# Instala o handler de exceções do Rich para erros coloridos e detalhados no console
install()

class Restaurante:
    """
    Representa uma entidade de Restaurante.
    Gere o ciclo de vida operacional, a reputação via avaliações e a composição do menu.
    """

    # <-------- CONSTRUTOR -------->
    def __init__(self, title: str, category: str) -> None:
        """
        Inicializa o restaurante com dados higienizados.
        Utiliza composição para integrar o gestor de cardápio.
        """
        # Atributos Públicos (Identidade)
        self.title = title.strip().title()
        self.category = category.strip().upper()

        # Atributos Protegidos (Encapsulamento de Estado)
        self._evaluations = []
        self._active = False
        
        # Composição: O Restaurante "tem um" Cardápio
        self._cardapio = Cardapio(title=self.title)

    # <-------- PROPERTIES -------->

    @property
    def active(self) -> bool:
        """Retorna o estado de atividade (Ativo/Inativo) do restaurante."""
        return self._active

    @property
    def average_score(self) -> float:
        """
        Calcula a média aritmética das notas recebidas.
        Retorna 0.0 caso não existam avaliações para prevenir divisões por zero.
        """
        if not self._evaluations:
            return 0.0
        
        total_score = sum(i.nota for i in self._evaluations)
        return round(total_score / len(self._evaluations), 2)
    
    # <-------- MÉTODOS DE NEGÓCIO -------->

    def toggle_active(self) -> None:
        """Inverte o status operacional do estabelecimento."""
        self._active = not self._active

    def receive_evaluation(self, cliente: str, nota: float) -> None:
        """
        Regista uma nova avaliação.
        Valida se a nota cumpre os requisitos de integridade (0 a 10).
        """
        if not (0 <= nota <= 10):
            raise ValueError(f"Nota inválida ({nota}). A pontuação deve situar-se entre 0 e 10.")
        
        nova_avaliacao = Avaliacao(cliente=cliente, nota=nota)
        self._evaluations.append(nova_avaliacao)

    def ver_cardapio(self) -> None:
        """Delega a exibição do menu para o objeto Cardapio (Especialista)."""
        # Nota: Assume-se que o Cardápio já conhece o título do restaurante via __init__
        self._cardapio.show_cardapio()
    
    def adicionar_item(self, item: ItemCardapio) -> None:
        """Adiciona um item ao cardápio interno via composição."""
        self._cardapio.adicionar_item(item)

    # <-------- OVERRIDE DUNDER METHODS -------->

    def __str__(self) -> str:
        """
        Retorna uma representação tabular otimizada para visualização em CLI.
        """
        status_icon = "✅ ABERTO" if self.active else "❌ FECHADO"

        return (
            f"{self.title.ljust(25)} | "
            f"{self.category.ljust(20)} | "
            f"{status_icon.ljust(12)} | "
            f"⭐ {str(self.average_score).ljust(5)}"
        )