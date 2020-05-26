import json
import uuid
from Services import DbServices, CredCardServices
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

def AddCredCardModels(args):
    UniqueIdCred = str(uuid.uuid1())

    # Aqui faremos um dict of dict (a chave será sempre o UniqueId)
    # com os dados sendo validados um a um e colocando o status de ativo

    AddCredCard = {
        'CardId': UniqueIdCred,
        'CardName': args['CardName'],
        'Vencimento': args['Vencimento'],
        'Fechamento': args['Fechamento'],
        'CardStatus': 'Active'

    }

    # Manda pra validação!

    return AddCredCard, UniqueIdCred

def AddValuesCredCard(args):
    UniqueIdValue = str(uuid.uuid1())

    args = AddValuesCredCardModels(args)

    AddValue = {
            "Id": UniqueIdValue,
            "CardName": args['CardName'],
            "NumeroParcelas": args['QuantidadeDeParcelas'],
            "Valor": args['Valor'],
            "Vencimento": args['VencimentoAjustado'],
            "Status": "Active",
            "TipoDeDivida": args["TipoDeDivida"],
            "Descricao": args['Descricao']
    }

    return AddValue, UniqueIdValue

def AddValuesCredCardModels(args):
    ValuesCardDb = DbServices.GetValuesByCardName(args['CardName'])
    AdjustFechamento = CredCardServices.CredCardLogic(args, ValuesCardDb)
    return AdjustFechamento