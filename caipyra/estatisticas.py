# coding: utf-8


dados = {
    'pacoquinha': {
        'desc': 'paçoquinhas',
        'ano': {2016: 400,
                2017: 825}},
    'sonhos': {
        'desc': 'sonhos',
        'ano': {2016: 696000,
                # como não foi informado o valor de sonhos em 2017
                # calculou-se a estimativa da quantidade de sonhos na
                # razão de  crescimento do consumo de paçoquinhas
                2017: 1435500}},
    'quentao': {
        'desc': 'quentão',
        'ano': {2016: 125,
                2017: 30}},

    'carreta_furacao': {
        'desc': 'carreta furacão',
        'ano': {2016: 55,
                2017: 90}}
}


def estatistica(ano):
    msg_titulo = 'Em {0} foram:'.format(ano)
    print(msg_titulo)
    for item in dados:
        msg_ano = dados[item]['ano'][ano]
        msg_item = dados[item]['desc']
        msg_complemento = ''
        if (item == 'quentao'):
            msg_complemento = 'litros de '
        if (item == 'carreta_furacao'):
            msg_complemento = 'pessoas na '
        msg_conteudo = '    {0} {1}{2}!'.format(
            msg_ano, msg_complemento, msg_item)
        print(msg_conteudo)


def pacoquinhas(self):
    print('Juntos somos mais fortes, em 2016 comemos 400 paçoquinhas!')
    print('Em 2017 extrapolamos, comemos 825 paçoquinhas! Precisamos malhar!')


def quentao(self):
    print('Em 2016 bebemos juntos 125 litros de quentão, avante!')
    print('Em 2017 foram apenas 30 litros de quentão :-(')


def sonhos(self):
    print('Em 2016 foram realizados 696 mil sonhos, e não eram os de goiabada')


def carreta_furacao(self):
    print('Em 2016 existiam 55 doidos na carreta furacão.')
    print('Em 2017, 90 doidos faziam isso, socorro!')
