
def AddDebtsValid(Dict):
    msg = "The Value {} is not compatible with the specifications"
    DictValidation = {}
    if Dict['Name'] is None or Dict['Name'] == "":
        DictValidation['Name'] = msg.format(Dict['Name'])
    if Dict['Valor'] is None or Dict['Valor'] == "":
        DictValidation['Valor'] = msg.format(Dict['Valor'])
    if Dict['Vencimento'] is None or Dict['Vencimento'] == "":
        DictValidation['Vencimento'] = msg.format(Dict['Vencimento'])
    if Dict['NumeroParcelas'] is None or Dict['NumeroParcelas'] == "":
        DictValidation['NumeroParcelas'] = msg.format(Dict['NumeroParcelas'])
    if Dict['TipoDeDivida'] is None or Dict['TipoDeDivida'] == "":
        DictValidation['TipoDeDivida'] = msg.format(Dict['TipoDeDivida'])
    if DictValidation:
        return DictValidation, False
    else:
        return Dict, True