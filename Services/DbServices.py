import os
from Services import ConnectionServices
import datetime
from Commons import QueryToDict

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
                      values['Status']
                    ))
        con.commit()
    except Exception as e:
        msg = False
    return msg

def GetValuesByCardName(CardName):
    cur = connection.cursor
    AddValues = open(os.path.join("Queries","GetIdCard.sql")).read()
    cur.execute(AddValues.format("'"+CardName+"'"))
    CardId = QueryToDict.QueryToDict(cur.fetchall())
    return CardId

def GetValuesById(id):
    cur = connection.cursor
    AddValues = open(os.path.join("Queries","GetSimpleById.sql")).read()
    cur.execute(AddValues.format("'"+id+"'"))
    CardId = QueryToDict.SimpleQueryToDict(cur.fetchall())
    return CardId

def GetCards():
    cur = connection.cursor
    GetValues = open(os.path.join("Queries", "GetCards.sql")).read()
    cur.execute(GetValues)
    CardId = QueryToDict.CardsQueryToDict(cur.fetchall())
    return CardId

def GetCardsNames():
    cur = connection.cursor
    GetValues = open(os.path.join("Queries", "GetCardsNames.sql")).read()
    cur.execute(GetValues)
    CardNames = QueryToDict.CardsNamesQueryToDict(cur.fetchall())
    return CardNames

def GetValuesByMonth(Month, Year):
    cur = connection.cursor
    AddValues = open(os.path.join("Queries","GetByMonth.sql")).read()
    cur.execute(AddValues.format("'"+Month+"'", "'"+Year+"'"))
    values = QueryToDict.SimpleQueryToDict(cur.fetchall())
    return values

def GetDebtsSum(Month, Year):
    cur = connection.cursor
    SumValues = open(os.path.join("Queries","GetSumDebts.sql")).read()
    cur.execute(SumValues.format("'"+Month+"'", "'"+Year+"'"))
    values = QueryToDict.SimpleSumQueryToDict(cur.fetchall())
    return values

def GetCardsSum(Month, Year):
    cur = connection.cursor
    SumValues = open(os.path.join("Queries","GetSumCards.sql")).read()
    cur.execute(SumValues.format("'"+Month+"'", "'"+Year+"'"))
    values = QueryToDict.SimpleSumQueryToDict(cur.fetchall())
    return values

def GetValuesByCurrentMonth():
    CurrentDate = datetime.datetime.now()
    Month = str(CurrentDate.month)
    Year = str(CurrentDate.year)
    cur = connection.cursor

    GetDebtValues = open(os.path.join("Queries", "GetByMonth.sql")).read()
    GetCardDebtValues = open(os.path.join("Queries", "GetCardDebtsByMonth.sql")).read()

    cur.execute(GetDebtValues.format("'" + Month + "'", "'" + Year + "'"))
    Debtsvalues = QueryToDict.SimpleQueryToDict(cur.fetchall())

    cur.execute(GetCardDebtValues.format("'" + Month + "'", "'" + Year + "'"))
    CardDebtsvalues = QueryToDict.CardQueryToDict(cur.fetchall())

    return [Debtsvalues, CardDebtsvalues]