import os
from Services import ConnectionServices

connection = ConnectionServices.conn().ConnPostgres()

def CreateTables():
    cur = connection.cursor
    con = connection.conn
    createcardcred = open(os.path.join("Queries","CreateCadCred.sql")).read()
    createcaddiv = open(os.path.join("Queries","CreateCadDiv.sql")).read()
    createcardcredvalues = open(os.path.join("Queries","CreateCadValuesCred.sql")).read()
    cur.execute(createcardcred)
    cur.execute(createcaddiv)
    cur.execute(createcardcredvalues)
    con.commit()

def SendSimpleDebts(values):
    msg = True
    cur = connection.cursor
    con = connection.conn
    AddValues = open(os.path.join("Queries","AddValues.sql")).read()
    try:
        cur.execute(AddValues,
                    (
                      values['Id'],
                      values['Name'],
                      values['NumeroParcelas'],
                      values['Valor'],
                      values['Vencimento'],
                      values['Status'],
                      values['TipoDeDivida']
                    ))
        con.commit()
    except Exception as e:
        msg = False
    return msg

def SendValuesCredCard(values):
    msg = True
    cur = connection.cursor
    con = connection.conn
    AddValues = open(os.path.join("Queries","AddValuesCredCard.sql")).read()
    try:
        cur.execute(AddValues,
                    (
                      values['Id'],
                      values['CardName'],
                      values['NumeroParcelas'],
                      values['Valor'],
                      values['Vencimento'],
                      values['Status'],
                      values['TipoDeDivida'],
                      values['Descricao']
                    ))
        con.commit()
    except Exception as e:
        msg = False
    return msg

def SendCredCard(values):
    msg = True
    cur = connection.cursor
    con = connection.conn
    AddValues = open(os.path.join("Queries","AddCredCard.sql")).read()
    try:
        cur.execute(AddValues,
                    (
                      values['CardId'],
                      values['CardName'],
                      values['Vencimento'],
                      values['Fechamento'],
                      values['CardStatus']
                    ))
        con.commit()
    except Exception as e:
        msg = False
    return msg

def GetValuesByCardName(CardName):
    cur = connection.cursor
    AddValues = open(os.path.join("Queries","GetIdCard.sql")).read()
    cur.execute(AddValues.format("'"+CardName+"'"))
    CardId = QueryToDict(cur.fetchall())
    return CardId

def GetValuesById(id):
    cur = connection.cursor
    AddValues = open(os.path.join("Queries","GetSimpleById.sql")).read()
    cur.execute(AddValues.format("'"+id+"'"))
    CardId = SimpleQueryToDict(cur.fetchall())
    return CardId

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

def SimpleQueryToDict(query):
    values = query[0]
    DictQuery = {
        "Id": values[0],
        "name": values[1],
        "valor": values[2],
        "numeroparcelas": values[3],
        "vencimento": str(values[4]),
        "TipoDeDivida": values[5],
        "Status": values[6]
    }
    return DictQuery