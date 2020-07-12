from datetime import datetime
from dateutil.relativedelta import relativedelta

def MonthNameByNumber(number):
    monthName = {
        1: "Janeiro",
        2: "Fevereiro",
        3: "Março",
        4: "Abril",
        5: "Maio",
        6: "Junho",
        7: "Julho",
        8: "Agosto",
        9: "Setembro",
        10: "Outubro",
        11: "Novembro",
        12: "Dezembro"
    }
    return monthName[number]

def CreateParcels(args):
    comboParcel = []
    plano = int(args['QuantidadeParcelas']) + 1
    for parcelnumber in range(1, plano):
        newParcel = dict(args)
        newParcel['Parcel'] = parcelnumber
        newParcel['Vencimento'] = AdjustDates(newParcel)
        comboParcel.append(newParcel)
    return comboParcel

def CreateParcelsCard(args):
    comboParcel = []
    plano = int(args['QuantidadeDeParcelasCartao']) + 1
    for parcelnumber in range(1, plano):
        newParcel = dict(args)
        newParcel['Parcel'] = parcelnumber
        newParcel['Vencimento'] = AdjustDates(newParcel)
        comboParcel.append(newParcel)
    return comboParcel

def AdjustDates(values):
    if values['Parcel'] != 1:
        Vencimento = datetime.strptime(values['Vencimento'], '%Y-%m-%d')
        newVencimento = Vencimento + relativedelta(months=+ (values['Parcel']-1))
        return newVencimento.strftime('%Y-%m-%d')
    elif values['Parcel'] == 1:
        return values['Vencimento']


