import os
from Commons import QueryToDict
from Services import ConnectionServices
import datetime

connection = ConnectionServices.conn().ConnPostgres()

def GetValuesByCardName(CardName):
    cur = connection.cursor
    AddValues = open(os.path.join("Queries","GetCardByName.sql")).read()
    cur.execute(AddValues.format("'"+CardName+"'"))
    CardId = QueryToDict.QueryToDict(cur.fetchall())
    return CardId

def GetCardidByCardName(CardName):
    cur = connection.cursor
    AddValues = open(os.path.join("Queries","GetIdByCardName.sql")).read()
    cur.execute(AddValues.format("'"+CardName+"'"))
    CardId = cur.fetchall()[0]
    return CardId

def GetCards():
    cur = connection.cursor
    GetValues = open(os.path.join("Queries", "GetCards.sql")).read()
    cur.execute(GetValues)
    CardId = QueryToDict.CardsQueryToDict(cur.fetchall())
    return CardId

def GetCardsNames():
    cur = connection.cursor
    GetValues = open(os.path.join("Queries", "GetCards.sql")).read()
    cur.execute(GetValues)
    CardNames = QueryToDict.CardsNamesQueryToDict(cur.fetchall())
    return CardNames

def GetAllDebtsSum(Month, Year):
    cur = connection.cursor
    SumDebtsValues = open(os.path.join("Queries","GetSumDebts.sql")).read()
    SumCardsValues = open(os.path.join("Queries","GetSumCards.sql")).read()

    cur.execute(SumDebtsValues.format("'"+Month+"'", "'"+Year+"'"))
    debtsSum = cur.fetchall()

    cur.execute(SumCardsValues.format("'"+Month+"'", "'"+Year+"'"))
    cardsSum = cur.fetchall()

    DebtsValues = QueryToDict.SumAllQueryToDict(debtsSum, cardsSum)

    return DebtsValues

def GetAllDebtsByMonth(year):
    cur = connection.cursor
    SumDebtsValues = open(os.path.join("Queries","GetAllDebtsSumByMonth.sql")).read()
    SumFixdValues = open(os.path.join("Queries","GetAllFixedDebts.sql")).read()

    cur.execute(SumDebtsValues.format("'"+year+"'","'"+year+"'"))
    DebtsValues = cur.fetchall()

    cur.execute(SumFixdValues)
    FixedValues = cur.fetchall()

    AllValues = QueryToDict.SumValuesToDict(DebtsValues, FixedValues)

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
    values = QueryToDict.CardSumQueryToDict(cur.fetchall())
    return values

def GetValuesByCurrentMonth():
    CurrentDate = datetime.datetime.now()
    Month = str(CurrentDate.month)
    Year = str(CurrentDate.year)
    cur = connection.cursor

    GetDebtValues = open(os.path.join("Queries", "GetDebtsByMonth.sql")).read()

    cur.execute(GetDebtValues.format("'" + Month + "'", "'" + Year + "'"))
    resultado = cur.fetchall()
    Debtsvalues = QueryToDict.SimpleQueryToDict(resultado)

    return Debtsvalues

def GetCardValuesByCurrentMonth():
    CurrentDate = datetime.datetime.now()
    Month = str(CurrentDate.month)
    Year = str(CurrentDate.year)
    cur = connection.cursor

    GetDebtValues = open(os.path.join("Queries", "GetCardsByMonth.sql")).read()

    cur.execute(GetDebtValues.format("'" + Month + "'", "'" + Year + "'"))
    Debtsvalues = QueryToDict.CardQueryToDict(cur.fetchall())

    return Debtsvalues