def fibonacci(n):
    # Esta função é um gerador que produz os primeiros 'n' números na sequência de Fibonacci.
    a, b = 0, 1
    # Inicia com os dois primeiros números da sequência de Fibonacci.
    for _ in range(n):
        # Repete 'n' vezes para gerar 'n' números de Fibonacci.
        yield a
        # 'yield' pausa a função aqui, retornando o valor de 'a'.
        # Na próxima chamada, a execução continua daqui.
        a, b = b, a + b
        # Atualiza os valores de 'a' e 'b' para os próximos números na sequência.

for num in fibonacci(10):
    print(num)
    # Itera sobre os valores gerados pelo gerador de Fibonacci.
