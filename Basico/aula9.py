"""
Aprender a ler e escrever arquivos
Manipular informações dos arquivos
Copiar e mover arquvivos
"""
import shutil

def escrever_arquivo(texto):
    diretorio = 'C:/Users/arsilva/Desktop/Aulas_Digital/teste.txt'
    #arquivo = open('teste.txt', 'w') # Sobreescreve todo arquivo existente
    arquivo = open(diretorio, 'a') # Atualiza arquivo existente
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(nome_arquivo,texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()
    
def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r') # 'r' read - leitura
    texto = arquivo.read()
    print(texto)
    
def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    #print(aluno_nota)
    aluno_nota = aluno_nota.split('\n')
    #print(aluno_nota)
    lista_media = []
    for x in aluno_nota:
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        lista_notas.pop(0)
        #print(aluno)
        #print(lista_notas) 
        media = lambda notas: sum([int(i) for i in notas])/4 # Lista compreenhision
        #print(f'Media: {media(lista_notas)}\n')
        lista_media.append({aluno:media(lista_notas)})
    return lista_media

def copia_arquivo(nome_arquivo):
    shutil.copy(nome_arquivo, 'C:/Users/arsilva/Desktop/Aulas_Digital/notas_alunos.txt')
    
def mover_arquivo(nome_arquivo):
    shutil.move(nome_arquivo, 'C:/Users/arsilva/Desktop/Aulas_Digital/')

if __name__ == '__main__':
    mover_arquivo('notas.txt')
    #copia_arquivo('notas.txt')
    #lista_media = media_notas('notas.txt')
    #print(lista_media)
    #escrever_arquivo('Primeira linha\n')
    #aluno = 'Cesar,8,6,5,5\n'
    #atualizar_arquivo('notas.txt', aluno)
    #ler_arquivo('teste.txt')
    