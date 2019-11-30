<b>Trabalho de Inteligência Artificial</b>

Docente: Arleys Castro

Aluno:
Raique Carvalho Queiroz
RA - 162030146
Engenharia da Computação

Neste trabalho, o agente Pacman tem que encontrar caminhos no labirinto, tanto para chegar a um destino quanto para coletar
comida eficientemente. O objetivo do trabalho será programar algoritmos de busca e aplicá-los ao cenário do Pacman.

O que deve ser entregue:
  Os arquivos search.py e searchAgents.py que serão modificados no trabalho.
  Vídeo no YouTube com as aplicações do código

<b>Parte 1:</b>
  Encontrando comida em um ponto fixo usando algoritmos de busca

Passo 1 (2 pontos):
  Implemente o algoritmo de busca em profundidade (DFS) na função de pthFirstSearch do arquivo search.py.
  Para que a busca seja completa, implemente a versão de DFS que não expande estados repetidos (seção 3.5 do livro).
  (depth-first search = DFS)

  Códigos de teste:
  
    <p><code>python pacman.py -l tinyMaze -p SearchAgent</code>
    <p><code>python pacman.py -l mediumMaze -p SearchAgent</code>
    <p><code>python pacman.py -l bigMaze -z .5 -p SearchAgent</code>

Pergunta 1:
  A ordem de exploração foi de acordo com o esperado?
  O Pacman realmente passa por todos os estados explorados no seu caminho para o objetivo?

 Pergunta 2:
  Essa é uma solução ótima?
  Senão, o que a busca em profundidade está fazendo de errado?

Passo 2 (2 pontos):
  Implemente o algoritmo de busca em extensão (BFS) na função breadthFirstSearch do arquivo search.py.
  De novo, implemente a versão que não expande estados que já foram visitados.
  
  Códigos de teste:
  
    <p><code>python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs</code>
    <p><code>python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5</code>

Pergunta 3:
  A busca BFS encontra a solução ótima?
  Senão, verifique a sua implementação. Se o seu código foi escrito de maneira correta,
  ele deve funcionar também para o quebra-cabeças de 8 peças (seção 3.2 do livro-texto) sem modificações.
  
  <p><code>python eightpuzzle.py</code>

<b>Parte 2:</b>
  Variando a função de custo
 
Passo 3 (2 pontos):
  Implemente o algoritmo de busca de custo uniforme (checando estados repetidos) na função uniformCostSearch do arquivo search.py.
  
  Teste seu código executando os comandos a seguir, onde os agentes tem diferentes funções de custo
  (os agentes e as funções são dados):
  
    <p><code>python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs</code>
    <p><code>python pacman.py -l mediumDottedMaze -p StayEastSearchAgent</code>
    <p><code>python pacman.py -l mediumScaryMaze -p StayWestSearchAgent</code>

<b>Parte 3:</b>
  A* Search

Passo 4 (2 pontos):
  Implemente a busca A* (com checagem de estados repetidos) na função aStarSearch do arquivo search.py.
  A busca A* recebe uma heurística como parâmetro. Heurísticas tem dois parâmetros: um estado do problema de busca
  (o parâmetro principal), e o próprio problema. A heurística implementada na função nullHeuristic do arquivo search.py
  é um exemplo trivial.
  
  Teste sua implementação de A* no problema original de encontrar um caminho através de um labirinto para uma posição
  fixa usando a heurística de distância Manhattan (implementada na função manhattanHeuristic do arquivo searchAgents.py):
  
    <p><code>python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic</code>

A busca A* deve achar a solução ótima um pouco mais rapidamente que a busca de custo uniforme
(549 vs. 621 nós de busca expandidos na nossa implementação).

Pergunta 4:
  O que acontece em openMaze para as várias estratégias de busca?

<b>Parte 4:</b>
  Coletando comida
 
Passo 5 (2 pontos):
  Implemente uma heurística admissível foodHeuristic no arquivo searchAgents.pypara o problema FoodSearchProblem.
  
  Teste seu agente no problema trickySearch:
  
    <p><code>python pacman.py -l trickySearch -p AStarFoodSearchAgent</code>

Material preparado pelo curso Berkeley de <i>Inteligência Artificial</i>.
