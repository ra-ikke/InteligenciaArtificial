# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first [p 85].

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm [Fig. 3.7].

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    # cria uma Pilha que guardara os nos que serao explorados
    pilha = util.Stack()

    # cria uma colecao de itens que irao guardar as coordenadas dos nos ja visitados
    visitado = set()

    # comeco recebe as coordenadas iniciais do pacman
    comeco = problem.getStartState()

    # iremos preencher a pilha com os seguintes dados:
    # (coordenadas,caminho), sendo o caminho a sequencia
    # de direcoes que o pacman deve seguir para chegar ate
    # a coordenada
    pilha.push((comeco, []))

    while not pilha.isEmpty():

        # a pilha sera preenchida com os nos sucessores de cada no visitado
        # fazendo uma analise ate que encontre o caminho ou ate que encontre
        # um no que ja foi visitado, ou ate terminar um caminho sem resultado
        # executando assim um backtracking

        proximoNo = pilha.pop()
        coordenada = proximoNo[0]
        caminho = proximoNo[1]
        # se a coordenada em que o pacman esta for o objetivo
        # iremos retornar o caminho (sequencia de direcoes que
        # o pacman deve percorrer para chegar ate o fim do labirinto)
        if problem.isGoalState(coordenada):
            print caminho
            return caminho
        # verifica-se a coordenada que estamos analisando ja foi visitada,
        # se tiver sido, o no sai da pilha e um proximo no podera ser analisado
        if coordenada not in visitado:
            visitado.add(coordenada)
            # A funcao getSuccessors retorna os seguintes dados:
            # [0]: Coordenadas do no sucessor ao no que estava na pilha
            # [1]: Qual direcao foi tomada para chegar ate essa coordenada
            for sucessor in problem.getSuccessors(coordenada):
                # verifica-se o no sucessor ja foi visitado, se nao tiver sido,
                # ele envia a coordenada do no sucessor juntamente com o caminho
                # que foi tomado para chegar ate essa coordenada
                if sucessor[0] not in visitado:
                    pilha.push((sucessor[0], caminho + [sucessor[1]]))
    # util.raiseNotDefined()

def breadthFirstSearch(problem):
    "Search the shallowest nodes in the search tree first. [p 81]"
    "*** YOUR CODE HERE ***"

    # cria uma Fila que guardara os nos que serao explorados
    fila = util.Queue()

    # cria uma colecao de itens que irao guardar as coordenadas dos nos ja visitados
    visitado = set()

    # comeco recebe as coordenadas iniciais do pacman
    comeco = problem.startingState()

    # iremos preencher a fila com os seguintes dados:
    # (coordenadas,caminho), sendo o caminho a sequencia
    # de direcoes que o pacman deve seguir para chegar ate
    # a coordenada
    fila.push((comeco, []))

    while not fila.isEmpty():

        proximoNo = fila.pop()
        coordenada = proximoNo[0]
        caminho = proximoNo[1]

        # verifica-se a coordenada que estamos analisando e o objetivo,
        # se for, retornaremos o caminho (sequencia de direcoes que o
        # pacman deve percorrer para chegar ate o fim do labirinto)
        if problem.isGoal(coordenada):
            print caminho
            return caminho

        # verifica-se a coordenada que estamos analisando ja foi visitada,
        # se tiver sido, o no sai da fila e um proximo no podera ser analisado
        if coordenada not in visitado:
            visitado.add(coordenada)
            # A funcao getSuccessors retorna os seguintes dados:
            # [0]: Coordenadas do no sucessor ao no que estava na pilha
            # [1]: Qual direcao foi tomada para chegar ate essa coordenada
            for sucessor in problem.successorStates(coordenada):
                # verifica-se o no sucessor ja foi visitado, se nao tiver sido,
                # ele envia a coordenada do no sucessor juntamente com o caminho
                # que foi tomado para chegar ate essa coordenada
                if sucessor[0] not in visitado:
                    fila.push((sucessor[0], caminho + [sucessor[1]]))
    # util.raiseNotDefined()

def uniformCostSearch(problem):
    "Search the node of least total cost first. "
    "*** YOUR CODE HERE ***"

    # cria uma Fila de Prioridades que guardara os nos que serao explorados
    filaPrioridade = util.PriorityQueue()

    # cria uma colecao de itens que irao guardar as coordenadas dos nos ja explorados
    visitado = set()

    comeco = problem.startingState()

    # iremos preencher a fila com os seguintes dados:
    # (coordenadas,caminho,custo)

    filaPrioridade.push((comeco, []), 0)

    while not filaPrioridade.isEmpty():
        proximoNo = filaPrioridade.pop()
        coordenada = proximoNo[0]
        caminho = proximoNo[1]

        if problem.isGoal(coordenada):
            print caminho
            return caminho
        if coordenada not in visitado:
            visitado.add(coordenada)
            for sucessor in problem.successorStates(coordenada):
                if sucessor[0] not in visitado:
                    # precisamos entao calcular uma nova prioridade e para isso
                    # calculadmos o custo para chegar nesse novo no
                    custo = problem.actionsCost(caminho + [sucessor[1]])
                    filaPrioridade.push((sucessor[0], caminho + [sucessor[1]]), custo)
    # util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
