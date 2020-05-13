import json
import uuid
import Validators

def AddDebtsValuesModels(args):
    UniqueId = str(uuid.uuid1())

    # Aqui faremos um dict of dict (a chave será sempre o UniqueId)
    # com os dados sendo validados um a um e colocando o status de ativo
    if args['TipoDeDivida'] == "fixa":
        args['QuantidadeParcelas'] = 0

    AddSimpleValues = {UniqueId: {
        'Id': UniqueId,
        'Name': args['Name'],
        'Valor': args['Valor'],
        'Vencimento': args['Vencimento'],
        'TipoDeDivida': args['TipoDeDivida'],
        'NumeroParcelas': args['QuantidadeParcelas'],
        'Status': 'Active'
    }}

    # Manda pra validação!

    return AddSimpleValues, UniqueId




