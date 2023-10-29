from models.produto import Produto

ps4 = Produto('Playstation 4', 1789.44,quantidade_estoque=5)
xbox = Produto('Xbox 360', 1699, quantidade_estoque=5)
print(ps4)
print(xbox)
xbox.retirar_quantidade_estoque(3)
print(xbox)
print(xbox)
