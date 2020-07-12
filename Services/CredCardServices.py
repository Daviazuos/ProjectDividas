import datetime

def CredCardLogic(args, valuesdb):
    DiaMesCompra = args['DataCompra'][-5:]
    anoAtual = datetime.datetime.now().year
    mesesFechamento = GetDataFechamento()
    for mes in mesesFechamento:
        mesfechamento = mes.format(str(valuesdb['Fechamento']).zfill(2))
        if DiaMesCompra <= mesfechamento:
            dataAjustada = "{}-{}-{}".format(anoAtual,mesfechamento.split('-')[0],mesfechamento.split('-')[1])
            args['Vencimento'] = dataAjustada
            args['CardId'] = valuesdb['UniqueId']
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