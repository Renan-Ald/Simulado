import xlrd

tabela = xlrd.open_workbook("b.xls")
sheet = tabela.sheet_by_index(0)

lista = []
lista2 = []

for i in range(sheet.nrows):
    for j in range(2):
        lista.append(sheet.cell_value(i,j))
        
    lista2.append(lista)
    lista = []


lista4 = []
alunos = []

for linha in lista2:
    if linha[1] not in alunos: alunos.append(linha[1])


a = []

for i in range(len(alunos)):
    lista4.append(alunos[i])
    for j in range(len(lista2)):
        if alunos[i] == lista2[j][1]:
            lista4.append(lista2[j][0])
    a.append(lista4)
    lista4 = []


simulados = []


visitado = []
iguais = []
temp = []
for item in a:
    if item[0] not in visitado:
        temp.append(item[0])
        visitado.append(item[0])
        # print(item[0])
        for item2 in a:
            if item2[0] not in visitado:
                if item[0] != item2[0]:
                
                    if item[1:len(item)] == item2[1:len(item2)]:
                        temp.append(item2[0])
                        visitado.append(item2[0])

        iguais.append(temp)
        temp = []



# print(a[0])

# for i in iguais:
#     print(i)

l = []
for i in range(len(iguais)):
    for j in range(len(a)):
        if iguais[i][0] == a[j][0]:
            l.insert(0,"Simulado {}".format(i+1))
            for k in range(2,len(a[j])):
                l.append(a[j][k])

            simulados.append(l)
        l = []


# for i in simulados:
#     print(i)

#Salva em .txt
arquivo = open('arq01.txt','w')
for i in range(len(simulados)):
    arquivo.write("-----------"+'\n')
    arquivo.write("Simulado {}".format(i+1)+'\n')
    arquivo.write("-----------"+'\n')

    for j in range(1,len(simulados[i])):
        arquivo.write('    '+str(simulados[i][j])+'\n\n')
arquivo.close()