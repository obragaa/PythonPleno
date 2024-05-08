# Decorador de Logging em Python

## Descrição

Este repositório contém um exemplo simples de como implementar um decorador de logging em Python. O decorador `logger` é usado para registrar informações sobre as chamadas de funções, incluindo seus argumentos e o valor de retorno.

## Funcionalidade

O decorador `logger` envolve qualquer função com funcionalidade adicional que registra detalhes da chamada da função no console. Isso é útil para debugging e monitoramento de aplicações em desenvolvimento.

## Como usar

1. Clone este repositório.
2. Execute o script Python para ver o decorador em ação.

```bash
python nome_do_script.py
Modifique a função soma no script para testar o decorador com diferentes funções e argumentos.
Exemplo de código
python
Copy code
@logger
def soma(a, b):
    return a + b

soma(5, 3)
```
Este exemplo aplica o decorador logger à função soma, que simplesmente soma dois números e imprime os detalhes da chamada no console.

## Contribuições
Sinta-se à vontade para contribuir com este projeto com novos exemplos de decoradores ou melhorias no decorador existente.