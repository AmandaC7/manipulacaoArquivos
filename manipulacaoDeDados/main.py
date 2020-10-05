def readFile(filename):
    infile = open(filename, 'r')
    content = infile.read()
    infile.close()
    wordList = content.split()
    print(wordList)
    print("A quantidade de palavras é:",len(wordList), "A quantidade de caracteres é:", len(content))


leitura = readFile('Documento.txt')
