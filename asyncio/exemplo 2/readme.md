# Explicação:

1. **async def contar(descricao, ate):** Uma coroutine que conta até um número especificado, imprimindo uma descrição.

2. **asyncio.create_task():** Enfileira a coroutine para execução no loop de eventos e retorna uma Task, que é um tipo de Future - um objeto que representa um resultado eventual de uma operação assíncrona.

3. **await task1 e await task2:** Espera pela conclusão de cada tarefa.

## _Por que fazer dessa maneira? A criação de tasks permite que múltiplas coroutines sejam executadas concorrentemente. Isso é útil quando você tem várias operações que podem ser realizadas paralelamente, aumentando a eficiência do programa, especialmente em cenários de I/O intensivo._

 