from utils.helper import formata_float_str_moeda

class Produto:
    contador: int = 1

    def __init__(self: object, nome: str, preco: float, quantidade_estoque: int) -> None:
        self.__codigo: int = Produto.contador
        self.__nome: str = nome
        self.__preco: float = preco
        self.__quantidade_estoque: float = quantidade_estoque
        Produto.contador += 1

    @property
    def codigo(self: object) -> int:
        return self.__codigo

    @property
    def nome(self: object) -> str:
        return self.__nome

    @property
    def preco(self: object) -> float:
        return self.__preco

    @property
    def quantidade_estoque(self: object) -> int:
        return self.__quantidade_estoque

    def retirar_quantidade_estoque(self: object, quantidade_retirada: int):
        self.__quantidade_estoque -= quantidade_retirada

    def __str__(self) -> str:
        return f'Código: {self.codigo} \nNome: {self.nome} \nPreço: {formata_float_str_moeda(self.preco)} \n Quantidade em estoque: {self.quantidade_estoque}'

