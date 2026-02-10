from models.restaurante import Restaurante
from models.cardapio import (Prato,Bebida)
from rich.traceback import install
install()

# <-------- DRIVER CODE (TESTE DE UNIDADE) -------->
if __name__ == "__main__":
    # 1. Instanciação do Restaurante
    restaurante = Restaurante("Sabor da vovó", "Tradicional Nordestino")
    restaurante.toggle_active()
    
    # 2. Adicionando carga de dados para teste de média (Reputação)
    restaurante.receive_evaluation("Ana Mariana", 10.0)
    restaurante.receive_evaluation("Mario Armario", 6.0)
    restaurante.receive_evaluation("Julia Nuvem", 2.0)
    restaurante.receive_evaluation("Dev Cloud", 9.5)
    
    # 3. Adicionando Itens ao Cardápio (Polimorfismo e Composição)
    suco_uva = Bebida("Suco de Uva", 12.5, "500ml", "Suco integral sem açúcar")
    vinho_tinto = Bebida("Vinho Tinto", 85.0, "750ml", "Reserva especial")
    baiao_dois = Prato("Baião de Dois", 45.0, "Arroz, feijão de corda, queijo coalho e carne de sol")
    moqueca = Prato("Moqueca", 78.0, "Peixe fresco com leite de coco e azeite de dendê")
    bolo = Prato("Bolo", 78.0, "Bolo de milho fresco, feito na hora")
    coca_zero = Bebida("Coca Zero", 6.5, "350ml", "Coca zero açúcar")
    restaurante.adicionar_item(suco_uva)
    restaurante.adicionar_item(vinho_tinto)
    restaurante.adicionar_item(baiao_dois)
    restaurante.adicionar_item(moqueca)
    restaurante.adicionar_item(bolo)
    restaurante.adicionar_item(coca_zero)
    
    # 4. Saída formatada no console (Visão Geral)
    print("\n" + "="*75)
    print(f"{'NOME'.ljust(25)} | {'CATEGORIA'.ljust(20)} | {'STATUS'.ljust(12)} | {'MÉDIA'}")
    print("-" * 75)
    print(restaurante)
    print("="*75 + "\n")
    
    # 5. Exibição do Cardápio Detalhado (Rich Table)
    restaurante.ver_cardapio()
