**Trabalho de Inteligência Artificial**

Docente: Arleys Castro

Aluno:
Raique Carvalho Queiroz
RA - 162030146
Engenharia da Computação

**LINK VÍDEO YOUTUBE:** https://www.youtube.com/watch?v=FJW52Qn33fE

*RESPOSTAS PARA AS QUESTÕES DO TRABALHO SE ENCONTRAM ABAIXO:*

 A respeito da *Busca em Profundidade*
 
**(Pergunta 1)**

A ordem de exploração foi de acordo com o esperado?

**R:** Sim, para uma busca em profundidade, onde encontramos o "nó" objetivo percorrendo uma árvore ou um grafo com uma busca em ordem, os nós foram explorados corretamente.

O Pacman realmente passa por todos os estados explorados no seu caminho para o objetivo?

**R:** Não, pois a busca explorou vários caminhos até chegar até o objetivo, porém o Pacman percorre apenas o caminho final, ignorando o resto dos nós explorados.

**(Pergunta 2)**

Essa é uma solução ótima? Senão, o que a busca em profundidade está fazendo de errado?

**R:** Não. A Busca em Profundidade não percorre todos os nós possíveis dentro do labirinto, isso faz com que o caminho para chegar até o objetivo possa ser um caminho mais longo do que o esperado.

 A respeito da *Busca em Largura*
 
 **(Pergunta 3)**

A busca BFS encontra a solução ótima? 

**R:** A resposta para essa pergunta é um pouco relativa, essa busca lhe retorna o melhor caminho para chegar até o objetivo, porém esse algoritmo é muito custoso, pois pode explorar todos os nós do labirinto. Desta forma, se desprezarmos o custo computacional do algoritmo, a solução seria sim ótima.

 A respeito da *Busca em A**

**(Pergunta 4)**

O que acontece em openMaze para as várias estratégias de busca?

**R:** 
 
*Busca em Profundidade*
 
![OpenMaze BFS](https://i.imgur.com/ZnZ19ay.png?1)

Na busca de profundidade, foi possível perceber nitidademente que não obtivemos o caminho mais curto até o objetivo. O Pacman acabou percorrendo um caminho muito longo pois seguia a forma em que os nós eram desempilhados da pila. Porém o custo de exploração dos nós foi bem menor comparado aos 2 próximos exemplos.

*Busca em Largura*
 
![OpenMaze DFS](https://i.imgur.com/vMWtQye.png?1)
 
Já na busca em largura, obitivemos um caminho mais curto como esperado. Porém por ser um algoritmo que analisa praticamente todos os nós, como é possível ver na imagem acima, ele é bem custoso.

*Busca de Custo Uniforme*
 
![OpenMaze UCS](https://i.imgur.com/f9cNReS.png?1)
 
Apresenta as mesmas caracteristicas da Busca em Largura, como o custo de ir de uma coordenada para uma coordenada sucessora é unitaria, não conseguimos perceber uma diferença entre ambas as buscas.

*Busca A**
 
![OpenMaze ASTAR](https://i.imgur.com/0I4PClv.png?1)

Podemos classificar esta busca, dentre as 4 buscas trabalhadas neste projeto, como a busca que apresenta o melhor resultado, tanto em termos de custo de exploração de nós, quanto no custo do caminho encontrado para chegar até o objetivo. É possível observar na imagem que grande parte do labirinto não foi sequer explorado por conta da adição do valor herustico obtido.

**A respeito do trabalho:**

Neste trabalho, o agente Pacman tem que encontrar caminhos no labirinto, tanto para chegar a um destino quanto para coletar
comida eficientemente. O objetivo do trabalho será programar algoritmos de busca e aplicá-los ao cenário do Pacman.

O que deve ser entregue:
  Os arquivos search.py e searchAgents.py que serão modificados no trabalho.
  Vídeo no YouTube com as aplicações do código

**Parte 1:**
  Encontrando comida em um ponto fixo usando algoritmos de busca

Passo 1 (2 pontos):
  Implemente o algoritmo de busca em profundidade (DFS) na função de pthFirstSearch do arquivo search.py.
  Para que a busca seja completa, implemente a versão de DFS que não expande estados repetidos (seção 3.5 do livro).
  (depth-first search = DFS)

  Códigos de teste:
  
  ``python pacman.py -l tinyMaze -p SearchAgent``
  
  ``python pacman.py -l mediumMaze -p SearchAgent``
  
  ``python pacman.py -l bigMaze -z .5 -p SearchAgent``

Passo 2 (2 pontos):
  Implemente o algoritmo de busca em extensão (BFS) na função breadthFirstSearch do arquivo search.py.
  De novo, implemente a versão que não expande estados que já foram visitados.
  
  Códigos de teste:
  
  <p><code>python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs</code>
  <p><code>python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5</code>

  Se o seu código foi escrito de maneira correta,
  ele deve funcionar também para o quebra-cabeças de 8 peças (seção 3.2 do livro-texto) sem modificações.
  
  ``python eightpuzzle.py``

**Parte 2:**
  Variando a função de custo
 
Passo 3 (2 pontos):
  Implemente o algoritmo de busca de custo uniforme (checando estados repetidos) na função uniformCostSearch do arquivo search.py.
  
  Teste seu código executando os comandos a seguir, onde os agentes tem diferentes funções de custo
  (os agentes e as funções são dados):
  
  ``python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs``
  
  ``python pacman.py -l mediumDottedMaze -p StayEastSearchAgent``
  
  ``python pacman.py -l mediumScaryMaze -p StayWestSearchAgent``

**Parte 3:**
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

**Parte 4:**
  Coletando comida
 
Passo 5 (2 pontos):
  Implemente uma heurística admissível foodHeuristic no arquivo searchAgents.pypara o problema FoodSearchProblem.
  
  Teste seu agente no problema trickySearch:
  <p><code>python pacman.py -l trickySearch -p AStarFoodSearchAgent</code>

Material preparado pelo curso Berkeley de *Inteligência Artificial*.
