# ## ATIVIDADES:

# ### 1 - Crie um programa para efetuar a leitura de um número inteiro e apresentar o resultado do quadrado deste número.

# ### 2 - Crie duas variáveis para armazenar seu primeiro nome e sobrenome. Em seguida, concatene-as para formar seu nome completo e exiba o resultado.

# ### 3 - Peça ao usuário para digitar dois números inteiros e armazene-os em variáveis. Realize a concatenação desses números como strings e exiba o resultado.

# ### 4 - Crie uma variável para armazenar a palavra "Python". Em seguida, adicione um número inteiro ao final da palavra usando a concatenação e exiba o resultado.

# ### 5 - Declare uma variável contendo uma frase. Em seguida, peça ao usuário para digitar uma palavra e concatene essa palavra no final da frase. Exiba o resultado.

# # 1

# numero = int(input('digite um numero'))

# print('seu numero é ', numero)

# print('o quadradi do seu numero é', numero ** 2)


# #2 ---------------------------------------

# nome = input('Digite seu primeiro nome: ')
# sobrenome = input('Digite seu sobrenome: ')

# nome_completo = ('seu nome completo é', nome + sobrenome)

# print(str(nome_completo))


# #3 ----------------------------

# n1 = int(input('digite um numero: '))
# n2 = int(input('digite outro numero: '))

# print('numeros inteiros', n1, n2)

# int_para_string = (str(n1), str(n2))

# print('numeros int para str - >', int_para_string)

# #4 -----------------------------

# linguagem = 'Phyton'

# print(linguagem, n1)

# #5 ----------------------

# frase = 'o dia esta bonito'
# print(frase)

# frase_do_usuario = input('digite uma frase que se conecte com essa frase')


# frase_completa = (frase + frase_do_usuario)

# print(frase_completa)