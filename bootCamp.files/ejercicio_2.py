import time
# Puedes responder en francés y portugues tambíen, proximamente, aceptará otros idiomas
print('¡Bienvenido a una calculadora facíl!')
time.sleep(1)
print('Vamos a hacer operaciones, puedes elegir cual hacer:')
time.sleep(1)
print('(+) para sumar')
time.sleep(1)
print('(-) para restar')
time.sleep(1)
print('(* o **) para restar o elevar potencia')
time.sleep(1)
print('(/ o //) para hacer divisiones o divisiones enteras')
time.sleep(1)
print('¡Ten cuidado con los operadores de suma y resta, ya')
time.sleep(1)
print('que no funcionarán de forma doble')
time.sleep(1)
elección = 'si'
new_elección = ''
while elección == 'si' or 's' or 'yes':
    elección = new_elección
    a = int(input('Elije un número a para la operación: '))
    time.sleep(1)
    signo = ''
    time.sleep(1)
    while len(signo) > 2 or len(signo) == 0:
        signo = input('Seleccione el operador para la operación: ')
        time.sleep(1)
    time.sleep(1)
    b = int(input('Elije un número b para poder desarrollar la operación: '))
    time.sleep(1)
    print('Estamos cargando tu resultado...')
    time.sleep(3)
    resultado = 0
    def operaciónMatemática(a, signo, b):
        if signo == '+':
            time.sleep(1)
            print('¡Esto se lee: {} más {}!'.format(a,b))
            return a + b
        elif signo == '-':
            time.sleep(1)
            print('¡Esto se lee: {} menos {}!'.format(a,b))
            return a - b
        elif signo == '*':
            time.sleep(1)
            print('¡Esto se lee: {} por {}!'.format(a,b))
            return a * b
        elif signo == '**':
            time.sleep(1)
            print('¡Esto se lee: {} elevado a la {}!'.format(a,b))
            return a ** b
        elif signo == '/':
            time.sleep(1)
            print('¡Esto se lee: {} dividido entre {}!'.format(a,b))
            return a ** b
        elif signo == '//':
            time.sleep(1)
            print('¡Esto se lee: {} dividido entre {}!'.format(a,b))
            return a ** b
        else:
            return 'un error'
    
    time.sleep(1)
    resultado = operaciónMatemática(a, signo, b)
    print('El resultado final de {} {} {} es'.format(a, signo, b), resultado)
    time.sleep(1)
    print('¿Quieres hacer otra operación?')
    new_elección = input('¿Si o No?: ')
    if new_elección == 'si' or 's' or 'yes':
        continue
    if new_elección == 'no' or 'n' or 'not':
        break

print('¡Nos despedimos aquí!')
print('¡Nos veremos en una próxima vez!')