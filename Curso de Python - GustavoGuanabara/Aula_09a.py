frase = 'Curso em Vídeo Python'
print(frase.count('o'))
print(frase.upper().count('O'))
print(len(frase))
print(len(frase.strip())) # REMOVE OS ESPAÇOS ANTES E DEPOIS DA FRASE.
print(frase.replace('Python','Android'))
print('Curso' in frase)
print(frase.find('Vídeo')) # VAI EXIBIR A PARTIR DE QUAL POSIÇÃO ESTÁ 'CURSO'
print(frase.find('video')) # VAI EXIBIR ERRO [-1] PORQUE O PYTHON DESTINGUI LETRAS MAIÚSCULAS E MINÚSCULAS
print(frase.lower().find('vídeo'))
print(frase.split())
dividido = frase.split()
print(dividido[0]) # O PYTHON VAI CONSIDERAR 'CURSO' A LISTA [0]
print(dividido[0][3]) # O PYTHON SEMPRE VAI INICIAR A CONTAGEM DO ZERO.
