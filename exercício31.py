def quociente_inteiro(dividendo, divisor):

    if divisor ==0:
        raise ZeroDivisionError('O divisor não pode ser zero:') 
    sinal = -1 if (dividendo < 0) ^ (divisor < 0) else 1 
    dividendo_abs = abs(dividendo)
    divisor_abs = abs(divisor)

    quociente = 0 

    while dividendo_abs >= divisor_abs:
        dividendo_abs -= divisor_abs
        quociente += 1 

    return quociente * sinal

num1 = int(input('Digite um numero:'))
num2 = int(input('Digite um numero:')) 

resultado = quociente_inteiro(num1, num2) 

print(resultado)