import os
from Services import ConnectionServices

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
    result = True

    cur = connection.cursor
    con = connection.conn

    AddParcel = open(os.path.join("Queries","AddParcels.sql")).read()
    AddDebts = open(os.path.join("Queries","AddDebts.sql")).read()

    try:
        cur.execute(AddDebts, (values[0]['Name'], values[0]['QuantidadeParcelas']))
        id = cur.fetchone()[0]
        con.commit()

        for value in values:
            cur.execute(AddParcel,
                        (
                          id,
                          value['NumeroParcelas'],
                          value['Valor'],
                          value['Vencimento'],
                          value['TipoDeDivida'],
                          value['Status']
                        ))
        con.commit()
    except Exception as e:
        print(e)
        result = False
    return result

def SendCredCard(values):
    msg = True
    cur = connection.cursor
    con = connection.conn
    AddValues = open(os.path.join("Queries","AddCredCard.sql")).read()
    try:
        cur.execute(AddValues,
                    (
                      values['CardName'],
                      values['Vencimento'],
                      values['Fechamento'],
                      values['Status']
                    ))
        id = cur.fetchone()[0]
        con.commit()
    except Exception as e:
        print(e)
        msg = False
    return msg

def SendCardsValues(values):
    result = True

    cur = connection.cursor
    con = connection.conn

    AddParcel = open(os.path.join("Queries", "AddParcelsCard.sql")).read()

    for value in values:
        cur.execute(AddParcel,
                    (
                        value['CardId'],
                        value['NumeroParcelas'],
                        value['Valor'],
                        value['Vencimento'],
                        value['TipoDeDivida'],
                        value['Status'],
                        value['quantidadeparcelas'],
                        values['descricao']
                    ))
    con.commit()
    return result