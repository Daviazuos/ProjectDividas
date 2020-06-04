
def QueryToDict(query):
    values = query[0]
    DictQuery = {
        "UniqueId": values[0],
        "CardName": values[1],
        "Vencimento": values[2],
        "Fechamento": values[3],
        "Valor": values[4],
        "Status": values[5]
    }
    return DictQuery

def CardsQueryToDict(query):
    values = query[0]
    DictQuery = {
        "Cardid": values[0],
        "Cardname": values[1],
        "Vencimento": values[2],
        "Fechamento": values[3],
        "Status": values[4]
    }
    return DictQuery

def SimpleQueryToDict(query):
    Array = []
    for values in query:
        DictQuery = {
            "Id": values[0],
            "name": values[1],
            "valor": values[2],
            "numeroparcelas": values[3],
            "vencimento": str(values[4]),
            "TipoDeDivida": values[5],
            "Status": values[6]
        }
        Array.append(DictQuery)
    return Array

def CardQueryToDict(query):
    Array = []
    for values in query:
        DictQuery = {
            "Id": values[0],
            "name": values[1],
            "valor": values[2],
            "numeroparcelas": values[3],
            "vencimento": str(values[4]),
            "TipoDeDivida": values[5],
            "Status": values[6],
            "Descricao": values[7]
        }
        Array.append(DictQuery)
    return Array