# AlgoritmoGenetico
Jaler Samuel Zago - 108352
Sistemas Inteligentes
setembro de 2019
Adaptação de código em python para uso de torneio
INTRODUÇÃO
Nas últimas aulas de Sistemas Inteligentes tem-se mostrado algoritmos genéticos e a suas aplicações na área da computação. O score é uma métrica, que leva em consideração várias características e é usado para medir os critérios de modo a escolher sempre os indivíduos que melhor se adaptam ao meio. Dentre algumas das técnicas possíveis para fazer uma escolha mais eficaz e obter os indivíduos mais adaptados, ou seja, seleção natural, encontra-se o método do torneio, que será utilizado neste trabalho para substituir a aleatoriedade já implementada no algoritmo original. Também, será disponibilizado um vídeo com a execução do algoritmo que pode ser acompanhado clicando no seguinte link: 
https://www.youtube.com/watch?v=fIoXO0OkYmI&feature=youtu.be
DESCRIÇÃO
Foi apresentado para a turma, um algoritmo genético programado em python que dá uma ideia ampla de como funciona a seleção natural. O objetivo desse algoritmo é, determinar a menor média fitness, ou seja, dado um conjunto de genes (inteiros) somados - “sum” e um “target”. Fazer uma média do resultado de toda a população.  
Inicialmente o algoritmo dá valores as variáveis e cria uma população com o número de genes pré definido e selecionados de forma aleatória. A quantidade de indivíduos na população também é pré definida. Em seguida, ele calcula a primeira média fitness e adiciona a “fitness_history”.

Figura 1: Iniciação dos valores das variáveis, determinação da população inicial e cálculo da primeira média geral de fitness.


	Figura 2: Funções usadas para determinar uma população com genes aleatórios.


Figura 3: Funções usadas respectivamente para determinar a fitness de um indivíduo e para determinar a média fitness da população inteira.

Depois disso, é chamado um laço de iteração para a quantidade de épocas que foi pré definido o algoritmo. Nesse laço, a nova população será sempre o “return” da função “evolve”. A cada nova população, uma nova média fitness é criada e adicionada a “fitness_history”. 

Figura 4: Laço de iteração determinado pelo número de épocas.

Na função “evolve”, o fitness de cada indivíduo é calculado e guardado na lista “graded”, então é usado a função interna do python “sorted” para ordenar eles, do menor para o maior. Baseado na porcentagem escolhida para a variável retain, o top da lista “graded” é adicionado à lista de pais - Elitismo.

Figura 5: Função “evolve”, representando o elitismo.

Além da elite selecionada por classificação de score, no algoritmo apresentado em aula, uma parte do restante da população é aleatoriamente, utilizando a probabilidade de acontecer (random_select), escolhida para fazer parte dos pais também.

Figura 6: Iteração que garante à população, não selecionados no elitismo, ter random_select % de chance de ser colocada na lista de pais. 

Após selecionados os pais para a próxima geração, aplica-se uma mutação em apenas 1 gene do indivíduo, determinada se vai ou não acontecer pela variável “mutate”.

Figura 7: Iteração que realiza a mutação nos genes dos pais.

Após a mutação, determina-se quantos pais já foram adicionados a lista e quantos filhos terão que ser adicionados para completar o número total da população.
Com o número de filhos que precisam ser gerados calculado, é selecionado aleatoriamente duas posições na lista de pais, uma para ser pai e outra para ser mãe. Garante-se que o número sorteado não seja o mesmo, então gera-se um filho com a metade inicial de genes do pai, e a metade final de genes da mãe. Depois, adiciona-se o filho gerado, a lista de filhos. Esse processo repete-se até que o número de indivíduos pertencentes a população seja satisfeita.

Figura 8: Representação do nascimento de um filho com genes do pai e da mãe, respectivamente .

Enfim, a lista de filhos é incorporada a lista de pais e retornada ao usuário como uma nova população. Nesse processo os pais selecionados na figuras 5 e 6, foram clonados para a próxima geração. 

Figura 9: Clonagem dos pais e retorno para uma nova população.

Após reproduzir todas as gerações, e adicionar todas as média fitness à lista “fitness_history” como representado na figura 4, o algoritmo mostra ao usuário as médias fitness de todas as gerações calculadas.

Figura 10: Mostra das médias fitness adquiridas em todas as gerações.
PROBLEMA
O problema consiste em retirar o método de seleção totalmente aleatório e implementar o método de torneio. 
O torneio é um método consideravelmente eficaz para selecionar indivíduos de melhor score. De maneira geral, ele seleciona aleatoriamente n indivíduos e os compara, o que tiver o melhor score será utilizado. O n é pré definido.

RESOLUÇÃO
Para implementação do método proposto, inicialmente desenvolvi uma função “torneio” onde os parâmetros de entrada são: a lista na qual os indivíduos devem ser sorteados, a posição a partir de onde, na lista, deve ser iniciado o sorteio, a posição até onde o sorteio deve ir, o “target” como métrica de avaliação, e o número de indivíduos sorteados por torneio.
O algoritmo consiste em sortear um indivíduo e colocá-lo na lista “listaSorteio”. Então, pega-se a fitness dele e compara-se com a do indivíduo de melhor fitness. Se esse for o melhor (menor, neste caso), o melhor valor de fitness é atualizado e o “n” atual é guardado. Essa sorteio é repetido “n” vezes.
Após realizar “n” iterações, teremos o melhor “n” guardado, então basta pegar a “listaSorteio” na posição do melhor “n” guardado e teremos a posição do indivíduo que ganhou o sorteio, ou seja, o vencedor do torneio. Então basta-se retornar essa posição.

Figura 11: Função “torneio”, explicada previamente.

Na função “evolve” utilizei três vezes a chamada da função torneio para substituir a escolha aleatória. 
A primeira chamada acontece após selecionar a elite para determinar quais indivíduos, não contidos na elite, também devem ser pais. É ocupado a mesma iteração do algoritmo original, como mostrado na figura 6, para garantir que todo o resto da população tenha chance de ser pai, porém antes de colocar aleatoriamente um indivíduo na lista de pais é aplicado o método torneio para que, dentre “n”, só o melhor seja selecionado.

Figura 12: Modificação feita para garantir que a população restante seja elegida por meio de torneio.

As outras duas chamadas da função ocorrem ao selecionar um pai e uma mãe na lista de pais, que era anteriormente aleatório. Agora faz-se um torneio, seleciona-se a melhor posição dentre os sorteados (tanto para o pai, quanto para a mãe) e verifica se o torneio não elegeu o mesmo indivíduo. Se a escolha for diferente, então é buscado os genes de ambos e cruzado, de forma a ser a primeira metade do pai e a segunda metade da mãe.

Figura 13: Modificação feita para selecionar, por meio de torneio, um pai e uma mãe.
CONCLUSÃO
A fim de testar o algoritmo e como solicitado no exercício,usei os três últimos dígitos da minha matrícula (352) como “target”, fiz um teste e apresento as saídas a seguir:
Na primeira execução, usando n=3 para fazer o torneio e o número de épocas igual a 100 obtive valores que variaram de 4706,58 na primeira época, até 617,00 na centésima época.

Figura 14: Primeira execução do algoritmo modificado.

Na segunda execução, utilizei o mesmo n, porém mudei para 300 épocas. Percebi grandes melhorias, de uma primeira época com 4595,73, ele foi para 2,21 na trecentésima época.

Figura 15: Segunda execução do algoritmo modificado.

Por último, mantive as 300 épocas e alterei o n para 8. O resultado final não expressou ganho significativo, mas os resultados intermediários melhoraram mais rápido. Isso é explicado por que quanto maior o número de participantes de um torneio, maior a chance de um indivíduo com score alto aparecer.

Figura 16: Terceira execução do algoritmo modificado.
