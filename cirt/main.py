# main.py

import argparse
from cirt import *

def main():
    parser = argparse.ArgumentParser(description="Calculate salary details")
    parser.add_argument("salario_base", type=float, help="Base salary")
    parser.add_argument("-d", "--dias_uteis", type=int, default=22, help="Workdays in the month (default: 22)")
    parser.add_argument("-f", "--faltas", type=int, default=0, help="Absences (default: 0)")
    parser.add_argument("-a", "--subs_alim", type=float, default=0, help="Food subsidy per day (default: 0)")
    parser.add_argument("-t", "--subs_transp", type=float, default=0, help="Transport subsidy per day (default: 0)")
    parser.add_argument("-p", "--premios", type=float, default=0, help="Other bonuses (default: 0)")

    args = parser.parse_args()

    salario_base = args.salario_base
    dias_uteis = args.dias_uteis
    faltas = args.faltas
    subs_alim = args.subs_alim
    subs_transp = args.subs_transp
    premios = args.premios

    salario_base_apos_faltas = calcula_salario_base_apos_faltas(salario_base, faltas, dias_uteis)
    subsidio_de_alimentacao_total = calcula_subsidio_de_alimentacao(subs_alim, dias_uteis)
    subsidio_de_transporte_total = calcula_subsidio_de_transporte(subs_transp, dias_uteis)
    salario_liquido = calcula_salario_liquido_apos_incrementos_descontos(salario_base, subsidio_de_alimentacao_total, subsidio_de_transporte_total, premios, faltas, dias_uteis)
    desconto_seguranca_social = calcula_descontos_da_seguranca_social(salario_base_apos_faltas, subsidio_de_alimentacao_total, subsidio_de_transporte_total, premios)
    descontos_IRT = calcula_imposto_sobre_rendimento_de_trabalho(salario_base_apos_faltas, subsidio_de_alimentacao_total, subsidio_de_transporte_total, premios)

    print(f"Salário base: {salario_base:.2f}\n")
    print("== Incrementos ==")
    print(f"Sub Alimentação: {subsidio_de_alimentacao_total:.2f}")
    print(f"Sub Transporte: {subsidio_de_transporte_total:.2f}")
    print(f"Prémios: {premios:.2f}\n")
    print("== Descontos ==")
    print(f"Salário base apos faltas: {salario_base_apos_faltas:.2f}")
    print(f"Segurança Social: {desconto_seguranca_social:.2f}")
    print(f"IRT: {descontos_IRT:.2f}\n")
    print(f"Salário Líquido: {salario_liquido:.2f}")

if __name__ == "__main__":
    main()

