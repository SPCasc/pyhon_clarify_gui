def divisao(a, b):
    try:
        # Tentando dividir dois números normalmente.
        resultado = a / b
        print(f'O resultado da divisão de {a} por {b} é {resultado}')
    except ZeroDivisionError:
        # Se houver um erro de divisão por zero o código dentro do except é executado
        print('Erro: Não é possível dividir por zero.')
    except TypeError:
        # Caso os parametros fornecidos não sejam números o código dentro desse except é executado
        print('Erro: Ambos os valores devem ser números.')
    except Exception as e:
        # Captura qualquer outro tipo de exceção que não tenha sido tratada nos excepts anteriores
        print(f'Erro inesperado {e}')
    else:
        # O bloco else é executado se o código dentro do try for bem sucedido (sem erros)
        print('Divisão realizada com sucesso!')
    finally:
        # Independente do que aconteça, sempre vai mostrar o finally. Sempre será mostrado
        print('Processo de divisão concluído.')
    
# Teste 01: Divisão normal
print('\n ---- Teste 01 ----\n')
divisao(10,2)

# Teste 02: Divisão por 0
print('\n ---- Teste 02 ----\n')
divisao(10,0)

# Teste 03: Divisão com tipos inválidos
print('\n ---- Teste 03 ----\n')
divisao(10,'dois')

# Teste 04: Divisão com erro inesperado
print('\n ---- Teste 04 ----\n')
divisao('dez', 2)

