import asyncio

async def contar(descricao, ate):
    for i in range(1, ate + 1):
        print(f"{descricao} {i}")
        await asyncio.sleep(1)

async def main():
    # Cria tasks para executar coroutines simultaneamente
    task1 = asyncio.create_task(contar("Task 1 contando até 3", 3))
    task2 = asyncio.create_task(contar("Task 2 contando até 6", 6))

    # Aguarda todas as tasks serem concluídas
    await task1
    await task2

asyncio.run(main())
