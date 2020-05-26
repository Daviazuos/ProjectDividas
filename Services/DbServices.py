import os
from Services import ConnectionServices

connection = ConnectionServices.conn().ConnPostgres()

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
                      values['Valor'],
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