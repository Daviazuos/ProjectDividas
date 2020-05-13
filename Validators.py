
def AddDebtsValid(Dict):
    msg = "The Value {} is not compatible with the specifications"
    DictValidation = {}
    if Dict['Nome'] is not None and Dict['Nome'] != "":
        DictValidation[Dict['Nome']] = msg.format(Dict['Nome'])
    if Dict['Valor'] is not None and Dict['Valor'] != "":
        DictValidation[Dict['Valor']] = msg.format(Dict['Valor'])
    if Dict['Vencimento'] is not None and Dict['Vencimento'] != "":
        DictValidation[Dict['Vencimento']] = msg.format(Dict['Vencimento'])
    if Dict['NumeroParcelas'] is not None and Dict['NumeroParcelas'] != "":
        DictValidation[Dict['NumeroParcelas']] = msg.format(Dict['NumeroParcelas'])
    if Dict['Fixa'] is not None and Dict['Fixa'] != "":
        DictValidation[Dict['Fixa']] = msg.format(Dict['Fixa'])
    if Dict['Simples'] is not None and Dict['Simples'] != "":
        DictValidation[Dict['Simples']] = msg.format(Dict['Simples'])
    if Dict['Parcelado'] is not None and Dict['Parcelado'] != "":
        DictValidation[Dict['Parcelado']] = msg.format(Dict['Parcelado'])