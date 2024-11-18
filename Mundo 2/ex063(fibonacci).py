'''Na matemática, os números de Fibonacci são uma sequência ou sucessão definida como recursiva pela fórmula:
                   F(n + 2) = F(n + 1) + F(n) , com n ≥ 1 e F(1) = F(2) = 1 .
   Os primeiros números de Fibonacci são:
            1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597,...'''

print('----------------------------\n'
      '   Sequencia de Fibonacci   \n'
      '----------------------------\n')

quant = int(input('Quantos números da sequencia você quer ver? '))

print('0 -> 1 -> 1', end=' -> ')
c = 4
fn = 1
fn1 = 1
fn2 = 0
while c <= quant:
    fn2 = fn1 + fn
    print(f'{fn2}', end=' -> ')
    fn = fn1
    fn1 = fn2
    c += 1
print('FIM!')