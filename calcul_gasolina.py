print(
    'Vamos calcular a média de seus gastos com deslocamento para o trabalho! Caso você não tenha informações sobre o consumo de seu veículo em km/l, utilizaremos como referência um carro popular com uma eficiência média de 11 km por litro de combustível.'
)
print('')

nome = input('Digite o seu nome: ')
print('')
carro = input('Você sabe a eficiência de seu veículo em km/litro ? Digite o valor ou digite não. ')
carro = carro.lower()
carro = float(carro)

if carro > 0:
    print('Ótimo, vamos nessa!')

if carro == 'não':
    carro = 11
    print(f'Vamos calcular com base em {carro}.')
print(f'{carro}')

distancia = input ('Digite quantos quilômetros entre sua casa e o trabalho (somente números): ')
print('')
qts_vezes_semana = input ('Quantas vezes por semana você trabalha ? ')
print('')
gasolina = input ('Digite o valor da gasolina atual (use ponto no lugar da vírgula, ex.: 5.45): ')

try:
    carro = float(carro)
    distancia = float(distancia)
    gasolina = float(gasolina)
    qts_vezes_semana = int(qts_vezes_semana)

    if qts_vezes_semana > 7:
        print('Você não pode trabalhar mais que 7x por semana.')
    if qts_vezes_semana <= 7:

        # gasto diario
        distancia_ida_vinda_dia = distancia * 2
        valor_gasolina_diaria = (distancia_ida_vinda_dia / carro) * gasolina

        #mensal
        total_dias_por_mes = qts_vezes_semana * 4
        distancia_total_mensal = distancia_ida_vinda_dia * total_dias_por_mes

        #anual
        valor_total_gasolina_mensal = (distancia_total_mensal / carro) * gasolina
        valor_total_gasolina_anual = valor_total_gasolina_mensal *12
        distancia_total_anual = distancia_total_mensal * 12
        print('')
        print(f'{nome}, considerando que seu carro faz uma média de {carro} km/l e o preço da gasolina é R${gasolina:.2f}, seus gastos (ida e volta) são os seguintes:')
        print(f'Gasto diário: R${valor_gasolina_diaria:.2f}')
        print(f'Trabalhando {qts_vezes_semana} vezes por semana, seu custo mensal totaliza R${valor_total_gasolina_mensal:.2f}')
        print(f'Durante o mês, você percorre uma distância total de {distancia_total_mensal:.2f} km.')
        print(f'Ao longo de um ano, suas despesas alcançam R${valor_total_gasolina_anual:.2f}, cobrindo uma distância total de {distancia_total_anual:.2f} km.')



except:
    print('')
    print('Ops! Algo errado, verifique suas informações e tente novamente.')
    print(f'O seu nome é: {nome}, seu carro faz "{carro}" Km/l. ')
    print(f'A distância entre sua casa e seu trabalho é de "{distancia}" Km. ')
    print(f'Você trabalha "{qts_vezes_semana}x" por semana. ')
    print(f'O valor da gasolina é "R${gasolina}". ')
   
