#encoding = 'utf-8'

import csv

#Utilize o código que você desejar, pode ser o seu próprio código interno,
#ou código de barras do produto, SKU, Modelo do produto, etc.
codigo = input("\nDigite o código do produto: ")

marca = input("\nDigite a marca do produto: ")

#Exibe quais categorias você quer utilizar, estas foram criadas como exemplo
print("\nEscolha um dos códigos abaixo: ", 
      "\nAcessórios Informática = 1", 
      "\nAcessórios Celulares = 2", 
      "\nAcessórios Games = 3", 
      "\nGames Retro = 4")

#Você deve digitar o código exato da categoria correspondente
cod_cat = int(input("Digite o código da categoria:"))

#A variável categoria estará vazi e nela será armazenado
#A descrição da categoria escolhida a partir do código
categoria = ""

#Esta condição irá gravar na variável "categoria" o valor
#correspondente de acordo com o código escolhido, você pode
#criar mais categorias se quiser
if cod_cat == 1: categoria = "Acessórios Informática"
if cod_cat == 2: categoria = "Acessórios Celulares"
if cod_cat == 3: categoria = "Acessórios Games"
if cod_cat == 4: categoria = "Games retro"

#Digite uma breve descrição do produto, exemplo: "Teclado USB com fio"
descricao = input("Digite a descrição do produto: ")

#Vai exibir todos os dados que você digitou
print("\nCódigo: {}, \nMarca: {}, \nCategoria: {}, \nDescrição: {}" .format(codigo, marca, categoria, descricao))

#Este comando vai abrir o arquivo 'cadastro.csv' em modo de edição e armazená-lo na 
#variável "bd_cadastro"
bd_cadastro = open('cadastro.csv', 'a+', newline = '', encoding='utf-8')
#A adição de dados ao arquivo .csv ocorrerar a partir da variável 'w'
w = csv.writer(bd_cadastro)

#Escreve uma linha no arquivo cadastro.csv contido na variável 'bd_cadastro', serão utilizados os 
# dados que foram armazenados nas variáveis "codigo, marca, cod_cat, categoria e descricao"
#Cada variável ocupará uma coluna na linha.
w.writerow([codigo, marca, cod_cat, categoria, descricao])

#O arquivo 'cadastro.csv' será salvo e fechado com os dados que foram incluídos.
bd_cadastro.close()

#Exibe uma mensagem de finalização
print('\nDados Gravados com sucesso no arquivo cadastro.csv', 
      "\nAbaixo será feita e leitura e exibição de todos os dados contidos no arquivo.",
      "\nCaso prefira, é possível abrir o arquivo no LibreOffice Calc ou Microsoft Excel.")

#Cria uma tabela, nela serão armazenados para exibição na tela os dados contidos no
#arquivo cadastro.csv, há alguns dados que já foram preenchidos, fique atento na
#última linha que deverá conter o último dado armazenado, isto irá ocorrer toda vez
#que uma nova informação for adicionada e salva no arquivo .csv
tabela = []
#Será um contador de linhas
i = 0

#Abre o arquivo cadastro.csv no modo leitura e armazena na variável "ler"
with open('cadastro.csv', 'r') as f:
      ler = csv.DictReader(f)
      #Cada linha do arquivo será inserida na variável 'tabela'
      for linha in ler:
          tabela.insert(i, list((tuple(linha.values())))) #Coloca os dados em uma tabela
          #O contador 'i' indica qual a posição/linha na variável 'tabela' a linha do arquivo .csv
          #será armazenada
          i = i +1
#Será dado um print para cada linha contida na variável 'tabela'
for linha in tabela:
     print("\n",linha)

