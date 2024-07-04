CIRT - Aplicação CLI para calculo do IRT dos funcionários do grupo A
=====================================================================

Descrição
-----------

CIRT é uma aplicação CLI desenvolvida em Python que permite calcular o salario líquido com base nos descontos, subsídios e prémios.

Uso
----
Certifique-se que tem o Python instalado em sua máquina.

Instalação
------------

Para instalar o CIRT, deve clonar o repositório:
```
git clone https://github.com/Denilson-Simoes/dsimoes-estagio-2024-04
```
Certifique-se de entrar no Directorio *cirt*
```
cd [caminho onde se localiza o ficheiro]/cirt/
```
Execute o comando o seguinte para iniciar a aplicação:
```
python main.py [-d xx] [-f xx] [-a xx] [-t xx] [-p xx] salario base

Tendo como parametros:
```
    •    -d: Dias úteis do mês (padrão: 22)
    •    -f: Faltas (padrão: 0)
    •    -a: Subsídio de alimentação por dia (padrão: 0)
    •    -t: Subsídio de transporte por dia (padrão: 0)
    •    -p: Outros prémios (padrão: 0)
    •    salario base: Salário base (obrigatório)
```
Ex1: python main.py  -d 22 -f 0 -a 1000.00 -t 1000.00 -p 0.00 350000.00 

Obs: Caso o usuário não introduzir algum valor nos parametros, o valor será substituido pelo seu padrão com excessão do salario base que é um parametro obrigatório.
Ex2: python main.py  -a 1100 -t 1100 300000


```
As Informações detalhadas serão exibidas da seguinte forma:

Salário base: xxxx

== Incrementos ==

Sub Alimentação: xx

Sub Transporte: xx

Prémios: xx

== Descontos ==

Salário base apos faltas: xx

Segurança Social: xx

IRT: xx

Salário Líquido: xx

Ex3:Para os valores introduzidos no Ex1, essa seria a saída:
Salário base: 350000.00

== Incrementos ==

Sub Alimentação: 22000.00

Sub Transporte: 22000.00

Prémios: 0.00

== Descontos ==

Salário base apos faltas: 350000.00

Segurança Social: 11820.00

IRT: 56504.01

Salário Líquido: 325675.99

Obs: Os valores serão sempre apresentados com duas casas decimais pela convesão internacional padronizada.

Autor
------
Denilson Simões

