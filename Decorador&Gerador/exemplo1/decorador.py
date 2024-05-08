def logger(func):
    # O decorador recebe uma função como argumento.
    def wrapper(*args, **kwargs):
        # A função 'wrapper' é a função que substitui a função original.
        # Ela pode executar código antes e depois da função original.
        
        result = func(*args, **kwargs)
        # Chamamos a função original com os argumentos fornecidos.

        print(f"{func.__name__} foi chamada com {args}, {kwargs} e retornou {result}")
        # Registramos informações sobre como a função foi chamada e o que ela retornou.

        return result
        # O resultado da função original é retornado.
    
    return wrapper
    # Retornamos a função 'wrapper' modificada.

@logger
def soma(a, b):
    return a + b
    # Uma função simples que soma dois números.

soma(5, 3)
# A função 'soma' agora está decorada com a funcionalidade de logging.
