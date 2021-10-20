resp = 'S'
media = 0
soma = 0
quant = 0
maior = 0
menor = 0
# ou media = soma = quant = maior = menor = 0

while resp == 'S': #ou posso  while resp in 'Ss'
    num = int(input('Digite Um numero: '))
    soma = soma + num
    quant =  quant + 1
    if quant == 1 :
        maior = menor = num
    else:
        if num > maior :
            maior = num
        if num < menor :
            menor = num
    resp = str(input('Quer continuar ? , [S/N]')).upper().strip()[0]
print('acabou')
media = soma / quant

print('  Voce digitou {} numeros, e a meidia foi de {:.2f} '.format(quant,media))
print('Maior {} menor {} '.format(maior,menor))

