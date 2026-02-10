class Avaliacao:
    """
    Essa classe é um model para avaliações
    """
    # <-------- CONSTRUTOR -------->
    def __init__(self,cliente: str ,nota: float):
        
        self._cliente = cliente
        self._nota = nota
    # <-------- PROPERTIES -------->

    @property 
    def cliente(self):
        """
        Retorna o atributo cliente
        """
        return self._cliente
    
    @property
    def nota(self):
        """
        Retorna o atributo nota
        """
        return self._nota