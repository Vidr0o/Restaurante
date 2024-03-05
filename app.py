from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

Restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida('Suco de melancia', 5.00, 'grande')
bebida_suco.aplicar_desconto()
prato_pão = Prato ('Pão', 2.00, 'Melhor pão da cidade')
prato_pão.aplicar_desconto()
Restaurante_praca.adicionar_no_cardapio(bebida_suco)
Restaurante_praca.adicionar_no_cardapio(prato_pão)


def main():
    Restaurante_praca.exibir_cardapio


if __name__ == '__main__':
    main()


