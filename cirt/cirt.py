#Calcula o Salario Base apos faltas
def calcula_salario_base_apos_faltas(salario_base : float, faltas: int, dias_uteis : int) -> float:
    valor_por_falta = salario_base/dias_uteis
    sal_base_apos_faltas = salario_base-valor_por_falta*faltas
    return round(sal_base_apos_faltas, 2)
#Calcula o Subsidio de Alimentacao Total
def calcula_subsidio_de_alimentacao(subsidio_de_alimentacao_por_dia : float, dias_uteis : int) -> float:
    subsidio_de_alimentacao_total = subsidio_de_alimentacao_por_dia*dias_uteis
    return round(subsidio_de_alimentacao_total, 2)
#Calcula o Subsidio de Transporte Total
def calcula_subsidio_de_transporte(subsidio_de_transporte_por_dia : float, dias_uteis : int) -> float:
    subsidio_de_transporte_total = subsidio_de_transporte_por_dia*dias_uteis
    return round(subsidio_de_transporte_total, 2)
#Calcula o Desconto da Seguranca Social
def calcula_descontos_da_seguranca_social(salario_base : float, subsidio_de_alimentacao : float, subsidio_de_transporte : float, premios : float) -> float:
    salario_bruto = salario_base+subsidio_de_alimentacao+subsidio_de_transporte+premios
    descontos_seguranca_social = salario_bruto*0.03
    return round(descontos_seguranca_social, 2)
#Calcula o Imposto Sobre Rendimento de Trabalho
def calcula_imposto_sobre_rendimento_de_trabalho(salario_base : float, subsidio_de_alimentacao : float, subsidio_de_transporte: float, premios : float) -> float:

    subsidios_tributaveis = 0
    if (subsidio_de_alimentacao > 30000.00):
        subsidios_tributaveis = subsidios_tributaveis + (subsidio_de_alimentacao-30000.00)
    if (subsidio_de_transporte > 30000.00):
        subsidios_tributaveis = subsidios_tributaveis + (subsidio_de_transporte-30000.00)
    salario_base_total = salario_base + subsidios_tributaveis
    if salario_base_total <= 100000.00:
        parcela_fixa = 0
        taxa = 0
        limite = 0
    elif (100001.00 <= salario_base_total <= 150000.00) :
        parcela_fixa = 0
        taxa = 0.13
        limite = 100001.00
    elif (150001.00 <= salario_base_total <= 200000.00) :
        parcela_fixa = 12500.00
        taxa = 0.16
        limite = 150001.00
    elif (200001.00 <= salario_base_total <= 300000.00) :
        parcela_fixa = 31250.00
        taxa = 0.18
        limite = 200001.00
    elif (300001.00 <= salario_base_total <= 500000.00) :
        parcela_fixa = 49250.00
        taxa = 0.19
        limite = 300001.00
    elif (500001.00 <= salario_base_total <= 1000000.00) :
        parcela_fixa = 87250.00
        taxa = 0.20
        limite = 500001.00
    elif (1000001.00 <= salario_base_total <= 1500000.00) :
        parcela_fixa = 187249.00
        taxa = 0.21
        limite = 1000001.00
    elif (1500001.00 <= salario_base_total <= 2000000.00) :
        parcela_fixa = 292249.00
        taxa = 0.22
        limite = 1500001.00
    elif (2000001.00 <= salario_base_total <= 2500000.00) :
        parcela_fixa = 402249.00
        taxa = 0.23
        limite = 2000001.00
    elif (2500001.00 <= salario_base_total <= 5000000.00) :
        parcela_fixa = 517249.00
        taxa = 0.24
        limite = 2500001.00
    elif (5000001.00 <= salario_base_total <= 10000000.00) :
        parcela_fixa = 1117249.00
        taxa = 0.245
        limite = 5000001.00
    elif (10000001.00 <= salario_base_total) :
        parcela_fixa = 2342248.00
        taxa = 0.25
        limite = 10000001.00
    materia_colectavel = salario_base + subsidios_tributaveis - calcula_descontos_da_seguranca_social(salario_base,subsidio_de_alimentacao, subsidio_de_transporte, premios)
    imposto_sobre_rendimento_de_trabalho = parcela_fixa+(materia_colectavel-limite)*taxa
    if imposto_sobre_rendimento_de_trabalho < 0:
        imposto_sobre_rendimento_de_trabalho = 0
    return round(imposto_sobre_rendimento_de_trabalho, 2)
#Calcula o Salario Liquido apos todos incrementos e descontos
def calcula_salario_liquido_apos_incrementos_descontos(salario_base : float, subsidio_de_alimentacao : float, subsidio_de_transporte : float, premios : float, faltas : int, dias_uteis : int) -> float:
    salario_base_apos_faltas = calcula_salario_base_apos_faltas(salario_base, faltas, dias_uteis)
    desconto_seguranca_social = calcula_descontos_da_seguranca_social(salario_base_apos_faltas, subsidio_de_alimentacao,subsidio_de_transporte, premios)
    descontos_IRT = calcula_imposto_sobre_rendimento_de_trabalho(salario_base_apos_faltas, subsidio_de_alimentacao, subsidio_de_transporte, premios)
    salario_liquido_apos_incrementos_descontos = salario_base_apos_faltas+subsidio_de_alimentacao+subsidio_de_transporte+premios - desconto_seguranca_social - descontos_IRT
    return round(salario_liquido_apos_incrementos_descontos, 2)