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
    cur.execute(createcardcred)
    cur.execute(createcaddiv)
    con.commit()

def SendDebtsValues(values):
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
                      values['TipoDeDivida'],
                      values['descricao'],
                      values['iscardcred']
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
    AddValues = open(os.path.join("Queries","GetValuesByMonth.sql")).read()
    cur.execute(AddValues.format("'"+Month+"'", "'"+Year+"'"))
    values = QueryToDict.SimpleQueryToDict(cur.fetchall())
    return values

def GetAllDebtsSum(Month, Year):
    cur = connection.cursor
    SumDebtsValues = open(os.path.join("Queries","GetSumDebts.sql")).read()

    cur.execute(SumDebtsValues.format("'"+Month+"'", "'"+Year+"'"))
    DebtsValues = QueryToDict.SimpleSumQueryToDict(cur.fetchall())

    return [{"Sum": DebtsValues[0]['Sum']}]

def GetAllDebtsByMonth(year):
    cur = connection.cursor
    SumDebtsValues = open(os.path.join("Queries","GetAllDebtsSumByMonth.sql")).read()

    cur.execute(SumDebtsValues.format("'"+year+"'"))
    DebtsValues = cur.fetchall()

    AllValues = QueryToDict.SumValuesToDict(DebtsValues)

    return AllValues

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

    GetDebtValues = open(os.path.join("Queries", "GetDebtsByMonth.sql")).read()

    cur.execute(GetDebtValues.format("'" + Month + "'", "'" + Year + "'"))
    Debtsvalues = QueryToDict.SimpleQueryToDict(cur.fetchall())

    return Debtsvalues