# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
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
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state
        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state
        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take
        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.
    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.
    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    
    starting_node = problem.getStartState()
    c = problem.getStartState()
    visited_nodes = []
    visited_nodes.append(starting_node)
    states = util.Stack()
    state_tuple = (starting_node, [])
    states.push(state_tuple)
    while not states.isEmpty() and not problem.isGoalState(c):
        state, actions = states.pop()
        visited_nodes.append(state)
        successor = problem.getSuccessors(state)
        # for cost in problem.getSuccessors(starting_node):
        #     print(cost)
        for i in successor:
            neighbours = i[0]
            if not neighbours in visited_nodes:
                c = i[0]
                path = i[1]
                states.push((neighbours, actions + [path]))
    
    return actions + [path]
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    
    starting_node = problem.getStartState()
    visited_nodes = []
    visited_nodes.append(starting_node)
    states = util.Queue()
    state_tuple = (starting_node, [])
    states.push(state_tuple)
    while not states.isEmpty():
        state, action = states.pop()
        if problem.isGoalState(state):
            return action
        successor = problem.getSuccessors(state)
        for i in successor:
            neighbour = i[0]
            if not neighbour in visited_nodes:
                path = i[1]
                visited_nodes.append(neighbour)
                states.push((neighbour, action + [path]))
    return action
    
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    
    starting_node = problem.getStartState()
    visited_nodes = []
    states = util.PriorityQueue()
    states.push((starting_node, []) ,0)
    while not states.isEmpty():
        state, actions = states.pop()
        if problem.isGoalState(state):
            return actions
        if state not in visited_nodes:
            successors = problem.getSuccessors(state)
            for i in successors:
                neighbours = i[0]
                if neighbours not in visited_nodes:
                    path = i[1]
                    newCost = actions + [path]
                    states.push((neighbours, actions + [path]), problem.getCostOfActions(newCost))
        visited_nodes.append(state)
    
    return actions
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    
    starting_node = problem.getStartState()
    visited_nodes = []
    states = util.PriorityQueue()
    states.push((starting_node, []), nullHeuristic(starting_node, problem))
    nCost = 0
    while not states.isEmpty():
        state, actions = states.pop()
        if problem.isGoalState(state):
            return actions
        if state not in visited_nodes:
            successors = problem.getSuccessors(state)
            for i in successors:
                neighbours = i[0]
                if neighbours not in visited_nodes:
                    path = i[1]
                    nActions = actions + [path]
                    nCost = problem.getCostOfActions(nActions) + heuristic(neighbours, problem)
                    states.push((neighbours, actions + [path]), nCost)
        visited_nodes.append(state)
    return actions
    
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch