# -*- coding: utf-8 -*-
import glob,sys,os
import re
import xml.etree.ElementTree as ET

def quantidadeargs():
	if len(sys.argv) == 1:
		#1 arg
		txt(1)
		
	if len(sys.argv) == 2:
		#2 arg
		txt(2)
		
	if len(sys.argv) > 2:
		print '---Opcoes---'
		print 'python script.py : cria um arquivo caso nao tenha ou sobrescreve o arquivo Historico existente'
		print 'python script.py algum_argumento : cria um outro novo arquivo Historico so que com numeracao maior'
		print '-------------'

def txt(opcao):
	if opcao == 1:
		#regra norma de sobrescrita
		#procura se ja tem algum arquivo
		Contador_de_arquivos = 0
		Booleano_de_nomes = 0
		Contador_de_historicos = 0
		Nome_adt = ''
		
		for adt in glob.glob("*.txt"):
			Contador_de_arquivos = Contador_de_arquivos + 1
			if 'Historico' in adt:
				Contador_de_historicos = Contador_de_historicos + 1
				Nome_adt = adt
				#escrita(1,'')
			else:
				Booleano_de_nomes = 1
			
		if Contador_de_arquivos == 0:
			escrita(2,'')
		if Booleano_de_nomes == 1:
			escrita(2,'')
		
		if Contador_de_historicos > 1:
			count = 0
			for adt in glob.glob("*.txt"):
				n1 = adt.strip('.txt')
				n2 = n1.strip('Historico')
				print str(n2)
				if (n2 > count):
					count = n2
			nomedoarquivo = 'Historico'+str(count)+'.txt'
			apaga_org(nomedoarquivo)
			escrita(1,nomedoarquivo)
			
		if Contador_de_historicos == 1:
			escrita(1,Nome_adt)
		
	else:
		#regra sofisticada
		count = 0
		for adt in glob.glob("*.txt"):
			n1 = adt.strip('.txt')
			n2 = n1.strip('Historico')
			print str(n2)
			if (n2 > count):
				count = n2
				
		count = int(count) + int(1)
		print str(count)
		nomedoarquivo = 'Historico'+str(count)+'.txt'
		escrita(3,nomedoarquivo)

def escrita(opcao2,nome_do_arquivo):
	'''
	1 historico normal
	2 nao existe historico ou arq errados
	3 incremental
	'''

	if opcao2 == 1:
		with open(nome_do_arquivo, "r") as ff1:
			file_data = ff1.read()
			raw = open(nome_do_arquivo, "w")
			for file in glob.glob("*.xml"):
				with open(file) as ff:
					xmlstring = ff.read()
			
					xmlstring = re.sub('\\sxmlns="[^"]+"', '', xmlstring, count=2)
					root = ET.fromstring(xmlstring)
		
					for nct in root.findall('.//nCT'):
						raw.write("Cte: "+nct.text+"\n")
					for obs in root.findall('.//xObs'):
						raw.write("Carga: "+obs.text+"\n")
					for data in root.findall('.//dhEmi'):
						raw.write("Data de emissao: "+data.text+"\n\n")

			raw.close()
			raw.close()
		for file in glob.glob("*.xml"):
			os.remove(file)
		oscomm="notepad.exe Historico1.txt"
		os.system(oscomm)
	if opcao2 == 2:
		raw = open('Historico1.txt','w')
		for file in glob.glob("*.xml"):
				with open(file) as ff:
					xmlstring = ff.read()
			
					xmlstring = re.sub('\\sxmlns="[^"]+"', '', xmlstring, count=2)
					root = ET.fromstring(xmlstring)
		
					for nct in root.findall('.//nCT'):
						raw.write("Cte: "+nct.text+"\n")
					for obs in root.findall('.//xObs'):
						raw.write("Carga: "+obs.text+"\n")
					for data in root.findall('.//dhEmi'):
						raw.write("Data de emissao: "+data.text+"\n\n")
		raw.close()
		for file in glob.glob("*.xml"):
			os.remove(file)
		oscomm="notepad.exe Historico1.txt"
		os.system(oscomm)
	else:
		raw = open(nome_do_arquivo, "w")
		for file in glob.glob("*.xml"):
			with open(file) as ff:
				xmlstring = ff.read()
			
				xmlstring = re.sub('\\sxmlns="[^"]+"', '', xmlstring, count=2)
				root = ET.fromstring(xmlstring)
				for nct in root.findall('.//nCT'):
					raw.write("Cte: "+nct.text+"\n")
				for obs in root.findall('.//xObs'):
					raw.write("Carga: "+obs.text+"\n")
				for data in root.findall('.//dhEmi'):
					raw.write("Data de emissao: "+data.text+"\n\n")

		raw.close()
		raw.close()
		for file in glob.glob("*.xml"):
			os.remove(file)
		oscomm="notepad.exe Historico1.txt"
		os.system(oscomm)
		
def apaga_org(excecao):
	nada = ''
	for adt in glob.glob("*.txt"):
		if 'Historico' in adt:
			if excecao in adt:
				pass

			else:
				os.remove(adt)

def main ():
	quantidadeargs()

if __name__ == '__main__':
	main()