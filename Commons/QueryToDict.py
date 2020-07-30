from Commons import Functions

def QueryToDict(query):
    values = query[0]
    DictQuery = {
        "UniqueId": values[0],
        "CardName": values[1],
        "Vencimento": values[2],
        "Fechamento": values[3],
        "Status": values[4]
    }
    return DictQuery

def CardsQueryToDict(query):
    Array = []
    for values in query:
        DictQuery = {
            "Cardid": values[0],
            "Cardname": values[1],
            "Vencimento": values[2],
            "Fechamento": values[3],
            "Status": values[4]
        }
        Array.append(DictQuery)
    return Array

def ReceivedQueryToDict(query):
    Array = []
    for values in query:
        DictQuery = {
            "Date": values[0],
            "Value": values[1],
            "Type": values[2]
        }
        Array.append(DictQuery)
    return Array

def CardsNamesQueryToDict(query):
    Array = []
    for values in query:
        DictQuery = {
            "Cardname": values[1]
        }
        Array.append(DictQuery)
    return Array

def SumByCardNameQueryToDict(query):
    Array = []
    for values in query:
        DictQuery = {
            "Cardname": values[0],
            "Sum": str(values[1]),
            "DueDate": values[2]
        }
        Array.append(DictQuery)
    return Array

def SimpleQueryToDict(query):
    Array = []
    for values in query:
        DictQuery = {
            "name": values[1],
            "numeroparcelas": values[2],
            "parcela": values[5],
            "valor": str(values[6]),
            "vencimento": str(values[7]),
            "TipoDeDivida": values[8],
            "Status": values[9]
        }
        Array.append(DictQuery)
    return Array

def SimpleSumQueryToDict(query):
    Array = []
    Array.append({"Sum": str(query[0][0])})
    return Array

def SumAllQueryToDict(debts, cards):
    Array = []
    cardValue = cards[0][0]
    debtValue = debts[0][0]
    if cardValue is None:
        cardValue = 0.00
    if debtValue is None:
        debtValue = 0.00
    Array.append({"Sum": str(float(cardValue) + float(debtValue))})
    return Array

def CardSumQueryToDict(query):
    Array = []
    Array.append({"Sum": str(query[0][0])})
    return Array

def CardQueryToDict(query):
    Array = []
    for values in query:
            DictQuery = {
                "name": values[1],
                "parcela": values[7],
                "valor": str(values[8]),
                "vencimento": str(values[9]),
                "TipoDeDivida": values[10],
                "Status": values[11],
                "numeroparcelas": values[12],
                "Descricao": values[13]
            }
            Array.append(DictQuery)
    return Array

def SumValuesToDict(query, fixedvalues):
    Array = []
    DictQuery = {
        "sum": [],
        "month": []
    }
    for values in query:
        DictQuery["sum"].append(str(values[0]+fixedvalues[0][0]))
        DictQuery["month"].append(Functions.MonthNameByNumber(values[1]))
    Array.append(DictQuery)
    return Array

def SumQueryToDict(simple, card):
    for month in card.keys():
        if month in simple:
            simple[month] += card[month]
    return card
