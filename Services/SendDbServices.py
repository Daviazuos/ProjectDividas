import os

def SendSimpleDebts(connection, values):
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
        print(e)
        msg = False
    return msg