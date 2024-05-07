# Explicação:

1. **aiohttp.ClientSession():** Utiliza a biblioteca aiohttp para fazer requisições HTTP assíncronas. Isso permite que a execução não seja bloqueada enquanto espera pela resposta da rede.

2. **async with session.get(url) as response:** Faz uma requisição GET para a URL especificada de forma assíncrona.

3. **await response.text():** Espera pela resposta do servidor e obtém o texto da resposta de forma assíncrona.

## _Por que fazer dessa maneira? Em aplicações web e outras que dependem de I/O de rede, realizar operações de I/O de forma assíncrona evita bloqueios e permite que o servidor ou cliente execute outras tarefas enquanto espera pelas respostas da rede, otimizando o uso de recursos e melhorando a performance._