import this
import Operacoes #Acessando a classe operações
this.opcao = -1 #Declaração de variável global
this.num1  = 0
this.num2  = 0

def mostrarMenu():
    print('Escolha uma das opções abaixo: \n' +
          '1. Soma\n'                         +
          '2. Subtração\n'                    +
          '3. Multiplicação\n'                +
          '4. Divisão\n'                      +
          '0. Sair\n\n')
    this.opcao = int(input())#Entrada de dados

def coletarNum1():
    print('Informe o primeiro número: ')
    this.num1 = float(input()) #Convertendo um texto em número com vírgula

def coletarNum2():
    print('Informe o segundo número: ')
    this.num2 = float(input())#Convertendo um texto em número com vírgula

def executar():
    while(this.opcao != 0):
        mostrarMenu() #Chamando o método que mostra opções para o usuário

        if this.opcao == 1:
            coletarNum1() #Pegando o primeiro número
            coletarNum2() #Pegando o segundo número
            print('A soma entre {} e {} = {}'.format(this.num1, this.num2, Operacoes.soma(this.num1, this.num2)))
        elif this.opcao == 2:
            coletarNum1()
            coletarNum2()
            print('A subtração entre {} e {} = {}'.format(this.num1, this.num2, Operacoes.subtrair(this.num1, this.num2)))
        elif this.opcao == 3:
            coletarNum1()
            coletarNum2()
            print('A multiplicação entre {} e {} = {}'.format(this.num1, this.num2, Operacoes.multiplicar(this.num1, this.num2)))
        elif this.opcao == 4:
            coletarNum1()
            coletarNum2()
            print('A Divisão entre {} e {} = {}'.format(this.num1, this.num2,Operacoes.dividir(this.num1, this.num2)))
        else:
            print('Obrigado!')
            this.opcao = 0