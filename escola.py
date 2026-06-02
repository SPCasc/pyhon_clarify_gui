tipoEscola = input('Tipo da Escola: \n [1] Publico \n [2] Particular \nR: ')
mediaAluno = input('Qual a média do aluno?\nR: ')
freqAluno = input('Qual a frequência do aluno?\nR: ')
mediaAluno = int(mediaAluno)
freqAluno = int(freqAluno)


if tipoEscola == '2' :
    print('--------- ESCOLA PARTICULAR DESFOCO -----------')
    if mediaAluno >= 7 and freqAluno >= 70 :
        print ('Aprovado')
    else :
        print ('Reprovado') 
        
        
if tipoEscola == '1' :
    print('-----------ESCOLA PUBLICA DESFOCADISSIMA -----------')
    if mediaAluno >= 7 or freqAluno >=70 :
        print('Aprovado')
    else :
        print('Reprovado')
        
print('Fim da aplicação')
        

# python365.vercel.app