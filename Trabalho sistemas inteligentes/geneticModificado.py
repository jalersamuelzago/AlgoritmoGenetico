from random import randint, random
from operator import add
from functools import reduce

def individual(length, min, max):
    'Create a member of the population.'
    return [ randint(min,max) for x in range(length) ]

def population(count, length, min, max):
    """
    Create a number of individuals (i.e. a population).

    count: the number of individuals in the population
    length: the number of values per individual
    min: the minimum possible value in an individual's list of values
    max: the maximum possible value in an individual's list of values

    """
    return [ individual(length, min, max) for x in range(count) ]

def fitness(individual, target):
    """
    Determine the fitness of an individual. Higher is better.

    individual: the individual to evaluate
    target: the target number individuals are aiming for

    O fitness do individuo perfeito sera ZERO, ja que o somatorio dara o target
    reduce: reduz um vetor a um escalar, neste caso usando o operador add
    """
    sum = reduce(add, individual, 0)
    return abs(target-sum)

def media_fitness(pop, target):
    'Find average fitness for a population.'
    summed = reduce(add, (fitness(x, target) for x in pop))
    return summed / (len(pop) * 1.0)

#####################################################################################################
def torneio(lista,inicioLista,fimLista,target,n):
    'n é o número de sorteados para o torneio'
    listaSorteio=[0]*n
    cont=0
    menorFitness=999999999
    while cont<n:
        'sorteia um numero da lista e coloca na listaSorteio'
        listaSorteio[cont] = randint(inicioLista,fimLista)
        'pega a fitness desse individuo e coloca na lista para fazer o torneio'
        fitnessAtual = fitness(lista[listaSorteio[cont]],target)
        'pega o menor fitness entre os escolhidos pro torneio'
        if (fitnessAtual < menorFitness):
            menorFitness=fitnessAtual
            'guarda a posição do melhor score'
            melhorPosicao=cont
        cont+=1
    'retorna a posicao da lista dentre os n escolhidos, de melhor score'
    return listaSorteio[melhorPosicao]
#####################################################################################################

def evolve(pop, target, retain=0.2, random_select=0.05, mutate=0.01, n=8): 
    'n é o número de individuos no torneio '
    'Tabula cada individuo e o seu fitness'
    graded = [ (fitness(x, target), x) for x in pop]
    'Ordena pelo fitness os individuos - menor->maior'
    graded = [ x[1] for x in sorted(graded)]
    'calcula qtos serao elite'
    retain_length = int(len(graded)*retain)
    'elites ja viram pais'
    parents = graded[:retain_length]
    # randomly add other POUCOS individuals to
    # promote genetic diversity

#####################################################################################################
    for individual in graded[retain_length:]:   
        'garante que a população restante tenha n% de chance de virar pais, mesmo nao sendo elite'
        if random_select > random():
            'seleciona a posição do melhor individuo'
            melhorPosicao=torneio(graded,retain_length,len(graded)-1,target,n)
            'pega os genes do melhor individuo'
            individualMenor = graded[melhorPosicao]
            'adiciona ele a lista'
            parents.append(individualMenor)
#####################################################################################################

    # mutate some individuals
    for individual in parents:
        if mutate > random():
            pos_to_mutate = randint(0, len(individual)-1)
            # this mutation is not ideal, because it
            # restricts the range of possible values,
            # but the function is unaware of the min/max
            # values used to create the individuals,
            individual[pos_to_mutate] = randint(min(individual), max(individual))
    # crossover parents to create children
    parents_length = len(parents)
  
    'descobre quantos filhos terao que ser gerados alem da elite e aleatorios'
    desired_length = len(pop) - parents_length
    children = []
    'comeca a gerar filhos que faltam'
    cont=0
    #####################################################################################################
    while len(children) < desired_length:
        'escolhe a melhor posicao para pai e mae por torneio'
        melhorPosicaoMale = torneio(parents, 0, parents_length-1, target, n)
        melhorPosicaoFemale = torneio(parents, 0, parents_length-1, target, n)
        if melhorPosicaoMale != melhorPosicaoFemale:
            male = parents[melhorPosicaoMale]
            female = parents[melhorPosicaoFemale]
            'calcula metade dos genes'
            half = len(male) // 2
            'gera filho metade de cada'
            child = male[:half] + female[half:]
            'adiciona novo filho a lista de filhos'
            children.append(child)
        cont+=1
#####################################################################################################
    'adiciona a lista de pais (elites) os filhos gerados'
    parents.extend(children)
    return parents
