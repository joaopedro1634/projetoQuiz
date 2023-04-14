import random


def menu():
    continuar = 1
    while continuar:
        continuar = int(input('Escolha uma opção\n'
                              '0. Sair \n' +
                              '1. Jogar\n'))
        if continuar:
            jogo_quiz()
        else:
            print('Saindo...')
def jogo_quiz():

    perguntas = {
        'Pergunta 1':{
            'pergunta': 'Qual o nome do feitiço utilizado por Snape em HP 05 para entrar na memória de Harry?',
            'Alternativas':{'a':'Mententrar', 'b':'Estuperfaça', 'c':'Legilimens', 'd':'Protego'},
            'Resposta_Certa': 'c'
        },
        'Pergunta 2': {
            'pergunta': 'Qual o nome dos animais mágicos que são invisíveis em HP 05?',
            'Alternativas': {'a': 'Testrálio', 'b': 'Hypogriffo', 'c': 'Acromântula', 'd': 'Arpéu'},
            'Resposta_Certa': 'a'
        },
        'Pergunta 3': {
            'pergunta': 'Qual é o nome do feitiço usado por Harry no banheiro em HP 06?',
            'Alternativas': {'a': 'Carpe Retractum', 'b': 'Anapneo', 'c': 'Crucio', 'd': 'Sectumsempra'},
            'Resposta_Certa': 'd'
        },
        'Pergunta 4': {
            'pergunta': 'Quantas maldições Imperdoáveis existem?',
            'Alternativas': {'a': '5', 'b': '3', 'c': '2', 'd': 'NDA'},
            'Resposta_Certa': 'b'
        },
        'Pergunta 5': {
            'pergunta': 'Qual o nome do feitiço usado para transformar um objeto comum em uma Chave de Portal?',
            'Alternativas': {'a': 'Accio', 'b': 'Bombarda', 'c': 'Alohomora', 'd': 'Portus'},
            'Resposta_Certa': 'd'
        },
        'Pergunta 6': {
            'pergunta': 'Qual o nome do meio do diretor de Hogwarts?',
            'Alternativas': {'a': 'Dumbledore', 'b': 'Brian', 'c': 'Alvo', 'd': 'Wulfrico'},
            'Resposta_Certa': 'd'
        },
        'Pergunta 7': {
            'pergunta': 'Qual Patronus pertence a Luna Lovegood?',
            'Alternativas': {'a': 'Coelho', 'b': 'Cachorro', 'c': 'Cavalo', 'd': 'Corça'},
            'Resposta_Certa': 'a'
        },
        'Pergunta 8': {
            'pergunta': 'Cedric Diggory enfrentou que raça de dragão no Torneio Tribruxo?',
            'Alternativas': {'a': 'Vipertooth peruano',
                             'b': 'Focinho curto sueco',
                             'c': 'Verde galês comum',
                             'd': 'Ridgeback norueguês'},
            'Resposta_Certa': 'b'
        },
        'Pergunta 9': {
            'pergunta': 'Em que lugar Animais Fantásticos e Onde Habitam, primeiro filme da franquia, se passa?',
            'Alternativas': {'a': 'Londres',
                             'b': 'Nova York',
                             'c': 'Paris',
                             'd': 'Boston'},
            'Resposta_Certa': 'b'
        },
        'Pergunta 10': {
            'pergunta': 'Quando Newt Scamander conhece Tina Goldstein, onde ela trabalhava no Ministério da Magia dos Estados Unidos?',
            'Alternativas': {'a': 'No Departamento de Execução das Leis da Magia',
                             'b': 'No Escritório de Permissão de Varinha',
                             'c': 'No Departamento de Recursos Mágicos',
                             'd': 'No Departamento de Recursos de Vigilância do Congresso Mágico'},
            'Resposta_Certa': 'b'
        },
        'Pergunta 11': {
            'pergunta': 'Que tipo de comércio Jacob Kowalski estava tentando abrir no primeiro filme?',
            'Alternativas': {'a': 'Loja de roupas',
                             'b': 'Loja de sapatos',
                             'c': 'Mercado',
                             'd': 'Padaria'},
            'Resposta_Certa': 'd'
        },
        'Pergunta 12': {
            'pergunta': 'Queenie Goldstein tem uma habilidade mágica bastante peculiar. Qual é?',
            'Alternativas': {'a': 'Ofidioglossia',
                             'b': 'Metamorfomagia',
                             'c': 'Legilimência',
                             'd': 'Mediunidade'},
            'Resposta_Certa': 'c'
        },
        'Pergunta 13': {
            'pergunta': 'Em Animais Fantásticos: Os Crimes de Grindelwald, por que Alvo Dumbledore não pode lutar contra seu rival, Grindelwald?',
            'Alternativas': {'a': 'Porque Dumbledore não quer',
                             'b': 'Porque Grindelwald é mais poderoso do que Dumbledore',
                             'c': 'Porque eles fizeram um pacto de sangue na juventude',
                             'd': 'Porque Dumbledore não quer'},
            'Resposta_Certa': 'c'
        },
        'Pergunta 14': {
            'pergunta': 'Naquela época, Gerardo Grindelwald possuía uma das Relíquias da Morte? Se sim, qual é ela?',
            'Alternativas': {'a': 'A Capa da Invisibilidade',
                             'b': 'A Pedra da Ressurreição',
                             'c': 'A Varinha das Varinhas',
                             'd': 'NDA'},
            'Resposta_Certa': 'c'
        },
        'Pergunta 15': {
            'pergunta': 'Afinal, qual é a família na qual Credence realmente faz parte?',
            'Alternativas': {'a': 'A família Lestrange',
                             'b': 'A família Black',
                             'c': 'A família Dumbledore',
                             'd': 'A família Malfoy'},
            'Resposta_Certa': 'c'
        },
        'Pergunta 16': {
            'pergunta': '"Você se atreve a usar os meus feitiços contra mim? ..." É uma fala de qual livro/filme?',
            'Alternativas': {'a': 'Harry Potter e a Ordem da Fênix',
                             'b': 'Harry Potter e as Relíquias da Morte',
                             'c': 'Harry Potter e o Engima do Príncipe',
                             'd': 'Harry Potter o Prisoneiro de Azkaban'},
            'Resposta_Certa': 'c'
        },
        'Pergunta 17': {
            'pergunta': 'Harry olhou para os pés, mas eles tinham desaparecido. "É uma fala de qual livro/filme?',
            'Alternativas': {'a': 'Harry Potter e a Pedra Filosofal',
                             'b': 'Harry Potter e a Ordem da Fênix',
                             'c': 'Harry Potter o Prisoneiro de Azkaban',
                             'd': 'Harry Potter e o Engima do Príncipe'},
            'Resposta_Certa': 'a'
        },
        'Pergunta 18': {
            'pergunta': 'Potter, você arranjou uma namorada! É uma fala de qual livro/filme?',
            'Alternativas': {'a': 'Harry Potter e o Prisoneiro de Azkaban',
                             'b': 'Harry Potter e a Pedra Filosofal',
                             'c': 'Harry Potter e a Câmara Secreta',
                             'd': 'Harry Potter e o Cálice de Fogo'},
            'Resposta_Certa': 'c'
        },
        'Pergunta 19': {
            'pergunta': 'Qual o Feitiço usado por Barto Crouch Jr, após Harry ser pisoteado em Harry Potter e o Cálice de Fogo',
            'Alternativas': {'a': 'Abaffiato', 'b': 'Colloportus', 'c': 'Morsmordre', 'd': 'Confringo'},
            'Resposta_Certa': 'c'
        },
        'Pergunta 20': {
            'pergunta': 'Qual feitiço utilizado por Dumbledore para parar a queda de Harry da Vassoura?',
            'Alternativas': {'a': 'Deffindio', 'b': 'Dessendio', 'c': 'Diffindo', 'd': 'Arresto Momentum'},
            'Resposta_Certa': 'd'
        },

    }
    perguntas_sortidas = list(perguntas.items())
    random.shuffle(perguntas_sortidas)
    print('Vamos ao QUIZ!!!!!')
    respostas_certas = 0

    for chave_pergunta, valor_pergunta in perguntas_sortidas:

        print(f'{chave_pergunta}: {valor_pergunta["pergunta"]}')
        print('Escolhe a alternativa correta!')

        for chave_alternativa, valor_alternativa in valor_pergunta["Alternativas"].items():
            print(f'{chave_alternativa}): {valor_alternativa}')

        resposta_usuario = input('Sua resposta: ')
        if resposta_usuario == valor_pergunta["Resposta_Certa"]:
            print('Você acertou!')
            respostas_certas += 1
        else:
            print('Você errou!')

        print()

    qtd_perguntas = len(perguntas)
    porcentagem_acerto = respostas_certas / qtd_perguntas * 100
    print('Você acertou {} perguntas de {} do QUIZ'.format(respostas_certas, qtd_perguntas))
    print('Sua porcentagem de acerto foi de: {:.2f}%.'.format(porcentagem_acerto))
    if porcentagem_acerto <= 25:
        print('Você foi MAL')
    elif (porcentagem_acerto <= 50 and porcentagem_acerto > 25):
        print('Você está mediano!!!')
    else:
        print('Você é BRABO')
menu()