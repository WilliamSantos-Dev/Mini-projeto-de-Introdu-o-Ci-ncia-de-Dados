import random  # para gerar numeros aleatorios
import time  # para testes de velocidade de processamento
import os  # apenas para limpar a tela

controle_loop = 0  # Controla o loop, faz com que o programa repita até o usuario querer sair


class ExtratorDeProbabilidades:

    def __init__(self, nome_database):
        self.autorizar_inicio = 0  # para autorizar inicio apenas quando inserir uma base de dados
        self.database, self.numero_aleatorios = [], []
        self.linhas = 1
        self.nome_database = nome_database
        arquivo = open(self.nome_database, encoding="cp437")  # arquivo aberto
        self.linha_1 = arquivo.readline().strip("\n").split(',')
        for linha in arquivo:
            self.linhas += 1
        arquivo.close()  # arquivo fechado

    def gerador_de_linhas_aleatorias(self,
                                     quantidade):  # essa função gera uma lista de numero que seram usados para selecionar
        self.intervalo = quantidade
        aux = quantidade  # linhas do arquivo csv, isso deixou o codigo 5000% mais rapido (de acordo com os testes)
        list_aux = []  # O tempo de geração para 1000 numeros é de 0.203125 segundos
        for i in range(self.linhas):
            list_aux.append(i)
        self.numero_aleatorios = random.sample(list_aux, quantidade)

    def carregar_colunas(self, lista_colunas, quantidade):
        Probabilidade.gerador_de_linhas_aleatorias(quantidade)
        posicoes_colunas_user, base_temp_coluna, colunas_n_encontradas, colunas_encontradas = [], [], [], []
        i = 0
        while i < len(self.linha_1):  # esse lindo while acha a posicao das colunas q o usuario pediu
            for coluna in lista_colunas:
                if coluna == self.linha_1[i]:
                    posicoes_colunas_user.append(i)
                    colunas_encontradas.append(coluna)
            i += 1
        i = 0
        for coluna in lista_colunas:  # Este loop verifica as colunas que não foram encontradas
            t = 0
            for coluna_2 in colunas_encontradas:
                if coluna == coluna_2:
                    t = 1
            if t == 0:
                colunas_n_encontradas.append(coluna)
        if len(colunas_n_encontradas) > 0:
            os.system("cls")
            cabecalho()
            print("| Colunas Não Encontradas: ")
            print(f"| {colunas_n_encontradas}")
            print("|")
            print("| Colunas Encontradas: ")
            print(f"| {colunas_encontradas}")
            print("|")
            os.system("pause")
            print("| Aguarde enquanto as colunas encontradas são carregadas!")

        arquivo = open(self.nome_database, encoding="cp437")  # arquivo aberto
        porc_2 = 0
        for linha in arquivo:  # O cp437 vem para evitar erros com caracteres não reconhecidos # foi necessario usar após erros em bases de dados diferentes
            x = self.numero_aleatorios.count(i)  # O tempo de processamento para 1000 linhas é de 0.375000 segundos
            if x == 1:
                porc = int(i / self.linhas * 100)
                if porc % 1 == 0 and porc > porc_2:
                    porc_2 = porc
                    os.system("cls")
                    print(f" carregando... {porc}% Concluido.")
                line = linha.strip('"').strip("\n").split(",")
                y, z = 0, 0
                line_temp = []
                for valor in line:
                    y = posicoes_colunas_user.count(z)
                    if y == 1:
                        line_temp.append(line[z])
                    z += 1
                self.database.append(line_temp)
            i += 1
        arquivo.close()  # arquivo fechado
        for valor in self.linha_1:  # ordenar as colunas na ordem correta
            for valor_2 in lista_colunas:
                if valor == valor_2:
                    base_temp_coluna.append(valor)
        self.todas_colunas_planilha_ofc = self.linha_1
        self.linha_1 = base_temp_coluna  # modifica as colunas para so as que a pessoa pediu
        base_temp_coluna = []

    def descarregar(self):
        os.system("cls")
        cabecalho()
        print("| Limpando os dados...                                 |")
        self.database.clear()
        self.linha_1.clear()
        self.linhas = 1
        self.intervalo = 0
        time.sleep(2)
        print("| Dados descarregados com sucesso!                     |")
        print("|______________________________________________________|")
        os.system("pause")

    def probabilidade_apriori(self, caracteristica, valor):
        i, contador_caracteristica = 0, 0
        posicao_caracteristica = 9999999999999  # so pra controle, evitar erros
        for coluna in self.linha_1:
            if coluna == caracteristica:
                posicao_caracteristica = i
            i += 1
        if posicao_caracteristica != 9999999999999:
            for linha in self.database:
                if len(linha) > posicao_caracteristica and len(self.linha_1) > posicao_caracteristica:
                    if linha[posicao_caracteristica] == valor and linha[posicao_caracteristica] != self.linha_1[
                        posicao_caracteristica]:
                        contador_caracteristica += 1
        else:
            contador_caracteristica = 0
        prob = float(contador_caracteristica / self.intervalo * 100.00)
        os.system("cls")
        print(" ______________________________________________________________\n")
        print("                SRWP - Sistema RW de Probabilidade         \n\n")
        print(f"       A probabilidade de encontrar {valor} em {caracteristica}")
        print(f"                    é de: {prob:.2f}%")
        print(f"\n\nForam levados em consideração {self.intervalo} {caracteristica}. ")
        print(f"Para testar outro intervalo insira um novo arquivo no menu inicial. ")
        print("______________________________________________________________\n\n")
        os.system("pause")

    def probabilidade_apriori_intervalo(self, caracteristica, inicio, fim):
        i, contador_caracteristica, espaco_vazio, erros, contador_erros = 0, 0, 0, 0,0
        posicao_caracteristica = 9999999999999  # so pra controle, evitar erros
        for coluna in self.linha_1:
            if coluna == caracteristica:
                posicao_caracteristica = i
            i += 1
        j = posicao_caracteristica

        if posicao_caracteristica != 9999999999999:
            for linha in self.database:
                erros = 0
                if len(linha) > j and len(self.linha_1) > j:
                    if linha[j] != self.linha_1[j] and linha[j] != '':  # nao vai contar com a linha das colunas
                        if len(linha[j]) > 0:  # evita que linhas vazias entrem
                            if len(linha[j]) > 0 and (len(linha) > j and len(self.linha_1) > j):
                                for letra in linha[j]:  # verifica erros de ter linhas com dados errado (letras ao inves de caracteres)
                                    if ord(letra) < 48 or ord(letra) > 57:
                                        erros += 1
                                        contador_erros += erros
                                        break
                            if erros == 0:
                                if float(linha[j]) > float(inicio)-0.0001  and float(linha[j]) < float(fim)+0.0001 :
                                    contador_caracteristica += 1
                        else:
                            espaco_vazio += 1
        else:
            contador_caracteristica = 0
        prob = float(contador_caracteristica / self.intervalo * 100.00)
        os.system("cls")
        print(" ______________________________________________________________\n")
        print("                SRWP - Sistema RW de Probabilidade         \n\n")
        print(f"       A probabilidade de encontrar {caracteristica} entre {inicio} e {fim}   ")
        print(f"                    é de: {prob:.2f}%")
        if espaco_vazio > 0:
            print(f"\nOBS: Durante a verificação o nosso sistema encontrou {espaco_vazio} espaço(s) vazio(s).")
        if contador_erros > 0:
            print(f"     Durante a verificação foi encontrado {contador_erros} erros! ")
            print("  foram encontrado Caracteres onde era esperado um números")
        print(f"\n\nForam levados em consideração {self.intervalo} {caracteristica}. ")
        print(f"Para testar outro intervalo insira um novo arquivo no menu inicial. ")
        print("______________________________________________________________\n\n")
        os.system("pause")

    def probabilidade_condicional(self, caracteristica_1, valor_1, caracteristica_2, valor_2):

        i, contador_caracteristica, erros = 0, 0, 0
        posicao_caracteristica_1, posicao_caracteristica_2 = 9999999999999, 9999999999999  # so pra controle, evitar erros
        for coluna in self.linha_1:
            if coluna == caracteristica_1:
                posicao_caracteristica_1 = i
            if coluna == caracteristica_2:
                posicao_caracteristica_2 = i
            i += 1
            a = posicao_caracteristica_1
            b = posicao_caracteristica_2
        if posicao_caracteristica_1 != 9999999999999 and posicao_caracteristica_2 != 9999999999999:
            for linha in self.database:
                if len(linha) > a and len(self.linha_1) > a and len(linha) > b and len(self.linha_1) > b:
                    if linha[a] == valor_1 and linha[a] != self.linha_1[a] and linha[b] == valor_2:
                        contador_caracteristica += 1
        else:
            contador_caracteristica = 0
        if contador_caracteristica == 0 or self.intervalo:
            prob = 0.0
        else:
            prob = float(contador_caracteristica / self.intervalo * 100.00)
        os.system("cls")
        print(" ______________________________________________________________\n")
        print("                SRWP - Sistema RW de Probabilidade         \n\n")
        print(f"  A probabilidade de encontrar [{caracteristica_1} = {valor_1}] e [{caracteristica_2} = {valor_2}] ")
        print(f"                    é de: {prob:.2f}%")
        print(f"\n\nForam levados em consideração {self.intervalo} casos. ")
        print(f"Para testar outro intervalo insira um novo arquivo no menu inicial. ")
        print("______________________________________________________________\n\n")
        os.system("pause")

    # A classe acaba aqui

    def aprior_com_condicional(self, caracteristica, valor_1, caracteristica_2, inicio, fim):
        i, contador_caracteristica, contador_caracteristica_1, espaco_vazio, erros, contador_erros = 0, 0, 0, 0, 0,0
        posicao_caracteristica, posicao_caracteristica_2 = 9999999999999, 9999999999999  # so pra controle, evitar erros
        for coluna in self.linha_1:
            if coluna == caracteristica:
                posicao_caracteristica = i
            if coluna == caracteristica_2:
                posicao_caracteristica_2 = i
            i += 1
        if posicao_caracteristica != 9999999999999:
            for linha in self.database:
                if len(linha) > posicao_caracteristica and len(self.linha_1) > posicao_caracteristica:
                    if linha[posicao_caracteristica] == valor_1 and linha[posicao_caracteristica] != self.linha_1[
                        posicao_caracteristica]:
                        contador_caracteristica_1 += 1
        if posicao_caracteristica != 9999999999999:
            for linha in self.database:
                erros = 0
                if len(linha) > posicao_caracteristica and len(self.linha_1) > posicao_caracteristica:
                    if type(linha) != '' and len(linha) > 0:
                        if linha[posicao_caracteristica] == valor_1 and linha[posicao_caracteristica] != self.linha_1[
                            posicao_caracteristica]:
                            if len(linha[posicao_caracteristica_2]) > 0 and (
                                    len(linha) > posicao_caracteristica_2 and len(
                                self.linha_1) > posicao_caracteristica_2):
                                for letra in linha[
                                    posicao_caracteristica_2]:  # verifica erros de ter linhas com dados errado (letras ao inves de caracteres)
                                    if ord(letra) < 48 or ord(letra) > 57:
                                        erros += 1
                                        contador_erros +=erros
                                        break
                                if erros == 0:
                                    if float(linha[posicao_caracteristica_2]) > float(inicio)-0.001  and float(linha[posicao_caracteristica_2]) < float(fim)+0.0001 :
                                        contador_caracteristica += 1
        else:
            contador_caracteristica = 0
        if contador_caracteristica == 0 or contador_caracteristica_1 == 0:
            prob = 0.0
        else:
            prob = float(contador_caracteristica / contador_caracteristica_1 * 100.00)
        os.system("cls")
        print(" ______________________________________________________________\n")
        print("                SRWP - Sistema RW de Probabilidade         \n\n")
        print(f"    A probabilidade de encontrar {valor_1} em {caracteristica}")
        print(f"    onde {caracteristica_2} esta entre {inicio} e {fim}   ")
        print(f"                    é de: {prob:.2f}%")
        if espaco_vazio > 0:
            print(f"\nOBS: Durante a verificação o nosso sistema encontrou {espaco_vazio} espaço(s) vazio(s).")
        if contador_erros > 0:
            print(f"\n\n     Durante a verificação foi encontrado {contador_erros} erros! ")
            print("  foram encontrado Caracteres onde era esperado um números")
        print("")
        print(f"Para testar outro intervalo insira um novo arquivo no menu inicial. ")
        print("______________________________________________________________\n\n")
        os.system("pause")


def cabecalho():  # funcção so pra deixar no grau, lindão
    print(" ______________________________________________________")
    print("|          SRWP - Sistema RW de Probabilidade          |")
    print("|                                                      |")


def main():
    global Probabilidade
    referencia = ''
    opcao_interna_main, opcao = 0, 0
    while opcao != 9:
        os.system("cls")
        cabecalho()
        print("| 1 - Escolher um arquivo                              |")
        print("| 2 - Calcular Proba. Apriori (característica, valor)  |")
        print("| 3 - Calcular Prob. Intervalo (caract., (inicio,fim)) |")
        print("| 4 - Calcular Prob. condicional (com Duas caractert. )|")
        print("| 5 - Calcular Prob. (Apriori + Intervalo)             |")
        print("| 6 - Visualizar informações sobre o arquivo           |")
        print("| 7 - Descarregar database                             |")
        print("| 9 - SAIR                                             |")
        print("|______________________________________________________|")

        entrada_user = input("| INFORME A OPCAO:")

        if ord(entrada_user[0]) >= 48 and ord(entrada_user[0]) <= 57 and len(entrada_user) == 1:
            opcao = int(entrada_user)
        else:
            opcao = 99

        if opcao == 1:
            os.system("cls")
            if referencia != '':
                cabecalho()
                print(f"| Você Já Tem a tabela ({referencia}) selecionada, deseja alterar?")
                opcao_interna_main = int(input("| 1 - Sim \n| 2 - Não\n|"))
                if opcao_interna_main == 1:
                    referencia = ''

            if referencia == '':  # Envia a referencia e cria o extartor de probabilidades e suas colunas
                cabecalho()
                referencia = input("| Qual o nome do arquivo?\n| ")
                print("| \n| Verificando Arquivo, aguarde!")
                Probabilidade = ExtratorDeProbabilidades(referencia)
                print("| Arquivo verificado!\n|")
                Probabilidade.autorizar_inicio = 1
                quant_linhas = int(input("| Quantas linhas você deseja carregar?"))
                if quant_linhas > Probabilidade.linhas:
                    os.system("cls")
                    cabecalho()
                    print("| Quantidade de linhas invalidas!\n|")
                    quant_linhas = int(input(f"| Informe um numero de 1 a {Probabilidade.linhas}\n| "))
                    print("|______________________________________________________|")

                os.system("cls")
                cabecalho()
                opcao_user_lista = int(input(
                    "| Esolha uma Opção:\n| 1 - Carregar todas as colunas do arquivo\n| 2 - Escolher colunas:\n| "))
                if opcao_user_lista == 2:
                    lista_de_colunas = input(
                        "| Informe quais coslunas deseja carregar(separarando por espaço)\n| ").strip(" ").split(' ')
                else:
                    os.system("cls")
                    lista_de_colunas = Probabilidade.linha_1
                os.system("cls")
                cabecalho()
                print(
                    "|          AGUARDE O CARREGAMENTO DOS DADOS!           |\n|                                                      |")
                Probabilidade.carregar_colunas(lista_de_colunas, quant_linhas)
                os.system('cls')
                cabecalho()
                print("|               Carregamento Finalizado!               |\n|______________________________________________________|")
                os.system('pause')
        if opcao > 1 and opcao < 9 and Probabilidade.autorizar_inicio == 0:
            cabecalho()
            print(
                "| É necessario escolher um ARQUIVO para iniciar        |\n|______________________________________________________|")
            time.sleep(2)
        if opcao > 1 and opcao < 9 and Probabilidade.autorizar_inicio == 1:
            if opcao == 2:
                os.system("cls")
                cabecalho()
                caracteristica = input("| Qual a caracteristica?")
                valor = input("| Qual o Valor?")
                Probabilidade.probabilidade_apriori(caracteristica, valor)

            if opcao == 3:
                os.system("cls")
                cabecalho()
                caracteristica = input("| Informe a característica:")
                inicio = input("| Valor inicial:")
                fim = input("| Valor final:")
                Probabilidade.probabilidade_apriori_intervalo(caracteristica, inicio, fim)

            if opcao == 4:
                cabecalho()
                os.system("cls")
                caracteristica_1 = input("| Qual a caracteristica 1?")
                valor_1 = input("| Qual o Valor 1?")
                caracteristica_2 = input("| Qual a caracteristica 2?")
                valor_2 = input("| Qual o Valor 2?")
                Probabilidade.probabilidade_condicional(caracteristica_1, valor_1, caracteristica_2, valor_2)

            if opcao == 5:
                os.system("cls")
                cabecalho()
                caracteristica = input("| Informe a caracteristica a qual deseja verificar: ")
                valor_1 = input("| Informe o valor da caracteristica: ")
                caracteristica_2 = input("| Informe a caracteristica do intervalo: ")
                inicio = input("| Informe o valor inicial do intervalo: ")
                fim = input("| Informe o valor final do intervalo: ")
                Probabilidade.aprior_com_condicional(caracteristica, valor_1, caracteristica_2, inicio, fim)
            if opcao == 6:
                os.system("cls")
                i = 0
                cabecalho()
                print("|                 Informações do Arquivo               |")
                print(f"| Nome do arquivo: {referencia}")
                print(f"| Tamanho do arquivo Original: {Probabilidade.linhas}")
                print(f"| Tamanho do arquivo solicitado: {quant_linhas}")
                print(f"| Tempo de processamento: {(time.process_time())}\n| ")
                print("| 1 - Visualiar banco de dados carregado")
                print("| 2 - Visualizar numeros das linhas sorteadas")
                escolha_user = int(input("| 3 - Voltar\n| Esolha uma opcao: "))
                print("|______________________________________________________|")
                if escolha_user == 1:
                    print(f"| Nome do arquivo: {referencia}")
                    print(f"\n Colunas = {Probabilidade.linha_1}\n")
                    for linha_database in Probabilidade.database:
                        print(f"| Linha: {i} = {linha_database}")
                        i += 1
                    os.system("pause")
                elif escolha_user == 2:
                    print(Probabilidade.numero_aleatorios)
                    os.system("pause")
                else:
                    os.system("cls")
            if opcao == 7:
                referencia = ''
                Probabilidade.autorizar_inicio = 0
                Probabilidade.descarregar()

        elif opcao == 9:
            print("\n\n\n\n")
            os.system("cls" if os.name == "nt" else "clear")
            print("  _____________________________________________________")
            print(" |                                                     |")
            print(" |         SRWP - Sistema RW de Probabilidade          |")
            print(" |_____________________________________________________|")
            print(" |                                                     |")
            print(" |   Universidade Federal do Agrestre de Pernambuco    |")
            print(" |       Bacharelado em Ciencia da Computacao          |")
            print(" |                                                     |")
            print(" | Desenvolvido por:                                   |")
            print(" |                                                     |")
            print(" | Robert Freire de Melo                               |")
            print(" | William Batista Couto dos Santos                    |")
            print(" |                                                     |")
            print(" | Version 18.5.2  Ultimate               25/05/2022   |")
            print(" |_____________________________________________________|")
            time.sleep(5)
            if referencia != '' and len(Probabilidade.database) > 0:
                Probabilidade.descarregar()
            global controle_loop
            controle_loop = 1
            break
        else:
            opcao = 99


while controle_loop == 0:  # usado para repetir o codigo ate o usuario querer sair
    try:  # Evita que erros comuns aconteção (ex: buscar arquivos que não existe)
        main()  # Evita erros de escrita
    except FileNotFoundError:  # Evita erros ao digitar nomes de arquivos que não existe
        os.system("cls")
        cabecalho()
        print("|  Esse arquivo não foi encontrado. Tente novamente!   |")
        print("|______________________________________________________|")
        time.sleep(2)
    except ValueError: # Evita erros quando o tipo de dado recebido é diferente do esperado
        os.system("cls")
        cabecalho()
        print("|          Opção Invalida. Tente novamente!            |")
        print("|______________________________________________________|")
        time.sleep(3)
    except NameError: # Evita erros de digitar nomes que não existem na base de dados
        os.system("cls")
        cabecalho()
        print("|          Ocorreu um erro. Tente novamente!           |")
        print("|   caso o erro persista digite 9 no menu inicial      |")
        print("|                e tente novamente                     |")
        print("|______________________________________________________|")
        time.sleep(3)
    except IndexError: # Evita erros quando a pessoa informa um valor inesistente na base de dados
        os.system("cls")
        cabecalho()
        print("|          Ocorreu um erro. Tente novamente!           |")
        print("|   caso o erro persista digite 9 no menu inicial      |")
        print("|                e tente novamente                     |")
        print("|______________________________________________________|")
        time.sleep(3)