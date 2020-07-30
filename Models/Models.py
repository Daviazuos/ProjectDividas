import uuid
from Services import DbPostServices, CredCardServices, DbGetServices
import Validators
from Commons import Functions

def AddReceivedModels(args):
    UniqueId = str(uuid.uuid1())

    AddReceived = {
        'Date': args['Date'],
        'Valor': args['Valor'],
        'Tipo': args['Tipo'],
        'Status': True
    }

    # Manda pra validação!

    return AddReceived, UniqueId

def AddDebtsValuesModels(args):
    UniqueId = str(uuid.uuid1())
    AddSimpleValues = []
    if args['TipoDeDivida'] == "fixa" or args['TipoDeDivida'] == "simples":
        args['QuantidadeParcelas'] = 0

        AddSimpleValues.append({
            'Name': args['Name'],
            'Valor': args['Valor'],
            'Vencimento': args['Vencimento'],
            'NumeroParcelas': args['QuantidadeParcelas'],
            'TipoDeDivida': args['TipoDeDivida'],
            'Status': '',
            'QuantidadeParcelas': args['QuantidadeParcelas']
        })

    elif args['TipoDeDivida'] == "Parcelada":
        listArgs = Functions.CreateParcels(args)

        for args in listArgs:
            AddSimpleValues.append({
                'Name': args['Name'],
                'Valor': args['Valor'],
                'Vencimento': args['Vencimento'],
                'NumeroParcelas': args['Parcel'],
                'TipoDeDivida': args['TipoDeDivida'],
                'Status': 'Active',
                'QuantidadeParcelas': args['QuantidadeParcelas']
            })

    # Manda pra validação!

    #AddSimpleValues, result = Validators.AddDebtsValid(AddSimpleValues)
    result = True
    return AddSimpleValues, UniqueId, result

def AddCredCardModels(args):
    UniqueIdCred = str(uuid.uuid1())

    AddCredCard = {
        'CardName': args['CardName'],
        'Vencimento': args['Vencimento'],
        'Fechamento': args['Fechamento'],
        'Status': True
    }

    # Manda pra validação!

    return AddCredCard, UniqueIdCred

def AddValuesCredCard(args):
    UniqueIdValue = str(uuid.uuid1())
    AddValue = []

    if args['TipoDeDividaCartao'] == "fixa" or args['TipoDeDividaCartao'] == "simples":
        args['QuantidadeDeParcelasCartao'] = 0

        args = AddValuesCredCardModels(args)

        AddValue.append({
            "CardId": args['CardId'],
            "CardName": args['CardName'],
            "NumeroParcelas": int(args['QuantidadeDeParcelasCartao']),
            "Valor": args['Valor'],
            "Vencimento": args['Vencimento'],
            "Status": "Active",
            "TipoDeDivida": args["TipoDeDividaCartao"],
            "descricao": args['Descricao'],
            "quantidadeparcelas": int(args['QuantidadeDeParcelasCartao'])
        })

    elif args['TipoDeDividaCartao'] == "Parcelada":
        args = AddValuesCredCardModels(args)

        listArgs = Functions.CreateParcelsCard(args)

        for args in listArgs:
            AddValue.append({
                "CardId": args['CardId'],
                "CardName": args['CardName'],
                "NumeroParcelas": args['Parcel'],
                "Valor": args['Valor'],
                "Vencimento": args['Vencimento'],
                "Status": "Active",
                "TipoDeDivida": args["TipoDeDividaCartao"],
                "descricao": args['Descricao'],
                "quantidadeparcelas": args['QuantidadeDeParcelasCartao']
            })

    return AddValue, UniqueIdValue

def AddValuesCredCardModels(args):
    ValuesCardDb = DbGetServices.GetValuesByCardName(args['CardName'])
    AdjustFechamento = CredCardServices.CredCardLogic(args, ValuesCardDb)
    return AdjustFechamento