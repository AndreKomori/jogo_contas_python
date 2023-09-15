from random import randint


class Calcular:
    def __init__(self: object, dificuldade: int, /) -> None:
        self.__dificuldade: int = dificuldade
        self.__valor1: int = self._gerar_valor
        self.__valor2: int = self._gerar_valor
        self.__operacao: int = randint(1, 3)  # 1 = Somar, 2 = Subtrair, 3 = Multiplicar
        self.__resultado: int = self._gerar_resultado

    @property
    def dificuldade(self):
        return self.__dificuldade

    @property
    def valor1(self):
        return self.__valor1

    @property
    def valor2(self):
        return self.__valor2

    @property
    def operacao(self):
        return self.__operacao

    @property
    def resultado(self):
        return self.__resultado

    def __str__(self: object) -> str:
        op: str = ''
        if self.operacao == 1:
            op = 'Somar'
        elif self.operacao == 2:
            op = 'Subtrair'
        elif self.operacao == 3:
            op = 'Multiplicar'
        else:
            op = 'Operação Inválida'
        return f'Valor 1: {self.valor1} \nValor 2: {self.valor2} \nDificuldade: {self.dificuldade} \nOperação: {op}'

    @property
    def _gerar_valor(self: object) -> int:
        if self.dificuldade == 1:
            return randint(1, 10)
        elif self.dificuldade == 2:
            return randint(10, 100)
        elif self.dificuldade == 3:
            return randint(100, 1000)
        else:
            return randint(1000, 10000)

    @property
    def _gerar_resultado(self: object) -> int:
        if self.operacao == 1:
            return self.valor1 + self.valor2
        elif self.operacao == 2:
            return self.valor1 - self.valor2
        else:
            return self.valor1 * self.valor2

    @property
    def simbolo(self: object) -> str:
        if self.operacao == 1:
            return '+'
        elif self.operacao == 2:
            return '-'
        else:
            return '*'

    def checar_resultado(self: object, resposta: int) -> bool:
        certo: bool = False

        if self.resultado == resposta:
            print('Resposta Certa!')
            certo = True
        else:
            print('Resposta Errada!')
        print(f'{self.valor1} {self.simbolo} {self.valor2} = {self.resultado}')
        return certo

    def mostra_operacao(self: object) -> None:
        print(f'{self.valor1} {self.simbolo} {self.valor2} = ?')
