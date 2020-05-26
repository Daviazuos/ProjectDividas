
# parser.add_argument('CardName', type=str)
# parser.add_argument('Valor', type=float)
# parser.add_argument('QuantidadeDeParcelas', type=int)
# parser.add_argument('TipoDeDivida', type=str)
# parser.add_argument('DataCompra', type=str)

def CredCardLogic(args, valuesdb):
    DiaCompra = int(args['DataCompra'][-2:])
    if DiaCompra < valuesdb['Fechamento']:
        valuesdb['Valor'] += args['valor']
    elif DiaCompra > valuesdb['Fechamento']:
        