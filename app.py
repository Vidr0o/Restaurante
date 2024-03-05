from modelos.restaurante import Restaurante


Restaurante_praca = Restaurante('praça', 'Gourmet')


Restaurante_praca.receber_avaliacao('gui', 5)
Restaurante_praca.receber_avaliacao('lais', 8)
Restaurante_praca.receber_avaliacao ('victor', 2)




def main():
    Restaurante.listar_restaurantes()


if __name__ == '__main__':
    main()


