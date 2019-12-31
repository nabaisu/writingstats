import pygsheets, time, random, csv, re, sys, os
from glob import glob
from os.path import isfile
from datetime import timedelta, date
import datetime

dayss= 15
start_date = date.today()-datetime.timedelta(days=dayss)
#start_date = date(2018, 01, 10)

print("\033c")
####
# COMO e QUE FUNCIONA ISTO?
#Day,	Word Count, 	Sum,	Number of Days, 	Average

fim = '\033[0m'
verde = '\033[1m\033[92m'
verdeclaro = '\033[92m'
azul = '\033[94m'

path = os.path.dirname(os.path.abspath(__file__))+"/writings/"
num_rows = 0

contatotal = 0

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

def countwords(fp):
   with open(fp) as fh:
       return len(fh.read().split())

##ABRIR O FICHEIRO DO GOOGLE
print "\n[-] Opening Connection to Google Sheets..."
try:
    gc = pygsheets.authorize(outh_file='credentials.json')
except Exception, e:
    print >> sys.stderr, "Something went wrong..."
    sys.exit(1)

print verdeclaro+"[+] Successfully Connected to Google Sheets"+fim
print "[-] Opening Spreadsheet..."
try:
    sh = gc.open('journaling-word-count')
except Exception, e:
    print >> sys.stderr, "Something went wrong..."
    sys.exit(1)

print verdeclaro+"[+] Spreadsheet Found\n"+fim
wks = sh.sheet1
#FIND OUT THE NUMBER OF ROWS
for row in wks:
    num_rows+=1

##End Date Today
#end_date = date.today()
##End Date Tomorrow
end_date = date.today()+datetime.timedelta(days=1)
print "[-] Starting day: " + azul + str(start_date) + fim
print "[-] Ending day:   " + azul + str(end_date)+ '\n' + fim
print "[-] Checking table entries:"

for single_date in daterange(start_date, end_date):
    dia = single_date.strftime("%Y-%m-%d")
    contagem = sum(map(countwords, filter(isfile, glob(path+str(single_date)+"*.txt") ) ) )
    contatotal += contagem

    #ENCONTRA NO FICHEIRO A DATA
    c1 = wks.find(str(dia), matchCase=True,matchEntireCell=True, cols=(1,1), rows=(num_rows-dayss,num_rows+5))
    for cl in c1:
        coluna = cl.row
    #SE FOR VAZIO (OU SEJA, SE NAO EXISTIR) ENTAO ADICIONA A LINHA INTEIRA
    if not c1:
        print verde + "[+] Adding new day:            "+fim+ str(dia) + '\t| '+str(contagem)+ ' words'+ '\t| cell '+str(num_rows+1)
        formula1 = '=B'+str(num_rows+1)+'+C'+str(num_rows)
        formula2 = '=D'+str(num_rows)+'+1'
        formula3 = '=round(C'+str(num_rows+1)+'/D'+str(num_rows+1)+',0)'
        wks.append_table(values=[dia,contagem,formula1,formula2,formula3])
        #ADICIONA MAIS UMA ROW PARA VERMOS SE ELE DA O QUE QUERO, QUE E
        #FAZER COM QUE SE EU FICAR 2 DIAS SEM ESCREVER SE ELE ME ADICIONA TUDO
        num_rows += 1
    #SE EXISTIR INDEED, ACTUALIZAR O VALOR
    else:
        for cl in c1:
            c2 = cl.neighbour('right')
            valor_dia = c2.value

        if int(valor_dia) != contagem:
            print verdeclaro + "[*] Updating Day Word Count:   "+fim+ str(dia) + '\t| '+str(contagem) + ' words' + '\t| cell '+str(coluna)
            cq = wks.cell('B'+str(coluna))
            cq.value = contagem

        else:
            print azul+"[-] Day WC Already Correct:    "+fim+ str(dia) + '\t| '+str(contagem)+ ' words'+ '\t| cell '+str(coluna)

print "\n[*] Total Words Written in last "+str(dayss+1)+" days   \t=>\t"+str(contatotal) +" words"
print "[*] Average Words Written in last "+str(dayss+1)+" days \t=>\t"+str(contatotal/(dayss+1))+" words"
print "[*] Words needed to 1000/day \t\t\t=>\t"+str(((dayss+1)*1000) - contatotal)+" words\n"
