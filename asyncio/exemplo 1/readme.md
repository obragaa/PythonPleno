# Explicação:

1. **async def main():** Define uma coroutine chamada main. Coroutines são funções que podem ser pausadas e retomadas, e são a base da programação assíncrona em Python.

2. **print("Olá"):** Executa uma operação de impressão imediatamente.

3. **await asyncio.sleep(1):** A palavra-chave await é usada para pausar a execução da coroutine até que a função asyncio.sleep(1) (que faz uma pausa assíncrona de 1 segundo sem bloquear o thread principal) seja concluída.

4. **print("Mundo"):** Esta linha é executada após a pausa de 1 segundo.

## _Por que fazer dessa maneira? Usar await permite que outras operações sejam executadas durante a pausa, o que é essencial em ambientes de I/O, como servidores web, onde bloquear a execução enquanto espera por uma resposta ou uma pausa pode levar a ineficiências significativas._