from typing import ClassVar, List

class Livro:
    """
    Representa um livro na biblioteca com controle de estoque e disponibilidade.
    """
    
    # Banco de dados em memória compartilhado (Pattern: Active Record simplificado)
    livros: ClassVar[List["Livro"]] = []

    def __init__(self, titulo: str, autor: str, publicacao: int):
        self.titulo = titulo
        self.autor = autor
        self.publicacao = publicacao
        # Encapsulamento: Atributo protegido
        self._disponivel = True
        
        # Auto-registro na lista global
        Livro.livros.append(self)
    
    # --- Factory Method (Padrão de Criação) ---

    @classmethod
    def from_csv(cls, row: str) -> "Livro":
        """
        Cria uma instância a partir de uma string CSV (titulo,autor,ano).
        Retorna a instância criada para flexibilidade de uso.
        """
        atributos = row.split(',')
        
        # Validação básica (Fail Fast)
        if len(atributos) != 3:
            raise ValueError("Formato CSV inválido. Esperado: 'titulo,autor,ano'")

        # Sanitização (.strip) para remover espaços acidentais
        titulo = atributos[0].strip()
        autor = atributos[1].strip()
        try:
            publicacao = int(atributos[2].strip())
        except ValueError:
            raise ValueError("O ano de publicação deve ser um número inteiro.")

        # Retornamos a instância! (Correção Arquitetural)
        return cls(titulo, autor, publicacao)

    # --- Properties (Getters) ---

    @property
    def disponivel(self) -> bool:
        """Retorna o estado booleano real."""
        return self._disponivel
    
    # --- Dunder Methods (Representação) ---

    def __str__(self) -> str:
        status_livro = "Disponível" if self.disponivel else "Indisponível"
        return (
            f"Título: {self.titulo.ljust(25)} | "
            f"Autor: {self.autor.ljust(20)} | "
            f"Ano: {str(self.publicacao).ljust(6)} | "
            f"Status: {status_livro}"
        )
    
    # --- Métodos de Negócio (Ações) ---

    def emprestar(self) -> str:
        """Marca o livro como emprestado."""
        self._disponivel = False
        return "Indisponível" 
    
    def recuperar(self) -> str:
        """Marca o livro como disponível."""
        self._disponivel = True
        return "Disponível"
    
    # --- Métodos Estáticos (Busca) ---

    @staticmethod 
    def verificar_disponibilidade(ano: int) -> List["Livro"]:
        """Retorna lista de livros disponíveis filtrada por ano."""
        return [
            livro for livro in Livro.livros 
            if livro.publicacao == ano and livro.disponivel
        ]

# --- Funções Auxiliares ---

def popular_biblioteca() -> None:
    """Cria massa de dados híbrida (Construtor e CSV)."""
    # Via Construtor
    Livro("Python Fluente", "Luciano Ramalho", 2015)
    Livro("Código Limpo", "Robert C. Martin", 2009)
    Livro("Arquitetura Limpa", "Robert C. Martin", 2017)
    
    # Via CSV (Agora validando e limpando dados)
    Livro.from_csv("Domain-Driven Design, Eric Evans, 2003")
    Livro.from_csv("1984, George Orwell, 1949") 
    Livro.from_csv("Entendendo Algoritmos,Aditya Bhargava,2017")

def main() -> None:
    try:
        popular_biblioteca()
        print(f"📚 Total de livros cadastrados: {len(Livro.livros)}")
    except ValueError as e:
        print(f"Erro Crítico na Importação: {e}")
        return

    # Cenário de Teste
    target = Livro.livros[2] # Arquitetura Limpa (2017)
    print(f"\n--- Emprestando: {target.titulo} ---")
    target.emprestar()
    
    ano_busca = 2017
    print(f"\n--- 🔍 Buscando disponíveis de {ano_busca} ---")
    # Deve trazer 'Entendendo Algoritmos', mas NÃO 'Arquitetura Limpa'
    resultados = Livro.verificar_disponibilidade(ano_busca)

    if resultados:
        for livro in resultados:
            print(livro)
    else:
        print(f"Nenhum livro disponível encontrado para {ano_busca}.")


if __name__ == "__main__":
    main()