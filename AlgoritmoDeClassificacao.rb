require 'classifier-reborn'
#Biblioteca para Classificacao Bayesiana em Ruby

#Gera suas categorias de classificao, no nosso caso Interessante e Desinteressante
classifier = ClassifierReborn::Bayes.new('Interessante', 'Desinteressante')

#Treina com todo aquele conteudo considerado "Interessante"
classifier.train_interessante("A cerveja e a cachaça são os piores inimigos do homem. Mas o homem que foge dos seus inimigos é um covarde.")
classifier.train_interessante("Bota aí um uísque, com uma cerveja para acompanhar. E não poupa no choro, boneca.")
classifier.train_interessante("Na falta de amor e carinho, Cerveja, Cachaça e Vinho")
classifier.train_interessante("Um brinde a cerveja: a solução e a causa de todo os nossos problemas.")
classifier.train_interessante("Só é sexta-feira após o primeiro copo de cerveja.")

#Treina com todo aquele conteudo considerado "Desinteressante"
classifier.train_desinteressante("Se podemos sonhar, também podemos tornar nossos sonhos realidade.")
classifier.train_desinteressante("A vida é como andar de bicicleta. Para ter equilíbrio você tem que se manter em movimento.")

#Apartir de uma entrada a classificao Bayesiana diz com qual grupo a entrada gera o menor MAP
#Ou seja, a frase é Interessante ou Desinteressante segundo o nosso treino?
puts('Frases com Cerveja')
puts(classifier.classify("Frases com Cerveja"))

puts('Frases de Efeito')
puts(classifier.classify("Frases de Efeito"))
