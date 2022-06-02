from models.calculate import Calculate

def main() -> None:
    points: int = 0
    play(points)

def play(points: int) -> None:
    difficulty: int = int(input("Informe o nível de dificuldade desejado [1, 2, 3 ou 4]: "))

    calc = Calculate(difficulty)

    print("Informe o resultado para a seguinte operação: ")
    calc.show_operation()

    result: int = int(input())

    if calc.check_result(result):
        points += 1

    print(f"Você tem {points} ponto(s).")

    keep: int = int(input("Deseja continuar jogando? [1 - Sim, 0 - Não]: "))

    if keep:
        play(points)
    else:
        print(f"Você finalizou com {points} ponto(s).")
        print("Até a próxima!")




if __name__ == "__main__":
    main()

