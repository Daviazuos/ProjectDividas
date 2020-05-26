import datetime


# parser.add_argument('CardName', type=str)
# parser.add_argument('Valor', type=float)
# parser.add_argument('QuantidadeDeParcelas', type=int)
# parser.add_argument('TipoDeDivida', type=str)
# parser.add_argument('DataCompra', type=str)

def CredCardLogic(args, valuesdb):
    DiaMesCompra = args['DataCompra'][-5:]
    anoAtual = datetime.datetime.now().year
    mesesFechamento = GetDataFechamento()
    for mes in mesesFechamento:
        mesfechamento = mes.format(str(valuesdb['Fechamento']).zfill(2))
        if DiaMesCompra <= mesfechamento:
            dataAjustada = "{}-{}-{}".format(anoAtual,mesfechamento.split('-')[0],mesfechamento.split('-')[1])
            args['VencimentoAjustado'] = datetime.datetime.strptime(dataAjustada, "%Y-%m-%d")
            return args


def GetDataFechamento():
    meses = [
        "01-{}",
        "02-{}",
        "03-{}",
        "04-{}",
        "05-{}",
        "06-{}",
        "07-{}",
        "08-{}",
        "09-{}",
        "10-{}",
        "11-{}",
        "12-{}"
    ]
    return meses