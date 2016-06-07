# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for 
# educational purposes provided that (1) you do not distribute or publish 
# solutions, (2) you retain this notice, and (3) you provide clear 
# attribution to UC Berkeley, including a link to 
# http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero 
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and 
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


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
    return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    #print "Start:", problem.getStartState()
    #print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    #print "Start's successors:", problem.getSuccessors(problem.getStartState())
    
    frontier=util.Stack()  # LIFO Stack, stores all leaf nodes available for expansion
    frontier.push((problem.getStartState(),[])) # initialize the frontier using the initial state of problem 
    explored=set()      # initialize the explored set to be empty
    if problem.isGoalState(problem.getStartState()):   # check wether the start state is the goal state
        return []    
    while not frontier.isEmpty():  # if the frontier is not empty then do
        leaf_node, path=frontier.pop()  # choose a leaf node and remove it from the frontier       
        if problem.isGoalState(leaf_node): # if the node contains a goal state then return the corresponding solution
            return path
        if leaf_node not in explored:
           explored.add(leaf_node) # add the node to the explored set
        # expand the chosen node, adding the resulting nodes to the frontier
           for successor,action,stepCost in problem.getSuccessors(leaf_node):
                if successor not in explored:
                    frontier.push((successor, path+[action] ))
    
    return []    
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    """
    "*** YOUR CODE HERE ***"
    frontier=util.Queue()  # FIFO Queue,stores all leaf nodes available for expansion
    frontier.push((problem.getStartState(),[])) # initialize the frontier using the initial state of problem 
    explored=[]    # initialize the explored set to be empty
    if problem.isGoalState(problem.getStartState()):   # check wether the start state is the goal state
        return []
 # loop    
    while not frontier.isEmpty():  # if the frontier is not empty then do
        leaf_node,path=frontier.pop()  # choose a leaf node and remove it from the frontier       
        if problem.isGoalState(leaf_node): # if the node contains a goal state then return the corresponding solution
            return path
        if not leaf_node in explored:
           explored.append(leaf_node) # add the node to the explored set
        # expand the chosen node, adding the resulting nodes to the frontier
           for successor,action,stepCost in problem.getSuccessors(leaf_node):
              frontier.push((successor, path+[action] ))
    return []    
    util.raiseNotDefined()

def uniformCostSearch(problem):
    "Search the node of least total cost first. "
    "*** YOUR CODE HERE ***"
    
    frontier=util.PriorityQueue()  # priority Queue, explore node with lowest cost
    frontier.push((problem.getStartState(),[]),0) # initialize the frontier using the initial state of problem 
    explored=[]      # initialize the explored set to be empty
    if problem.isGoalState(problem.getStartState()):   # check wether the start state is the goal state
        return []
 # loop    
    while not frontier.isEmpty():  # if the frontier is not empty then do
        leaf_node,path=frontier.pop()  # choose a leaf node and remove it from the frontier       
        if problem.isGoalState(leaf_node): # if the node contains a goal state then return the corresponding solution
            return path
        if leaf_node in explored:
           continue
        explored.append(leaf_node) # add the node to the explored set
        # expand the chosen node, adding the resulting nodes to the frontier
        for successor,action,stepCost in problem.getSuccessors(leaf_node):
            if not successor in explored:
     #           totalCost=problem.getCostOfActions(path)+stepCost
                frontier.push((successor, path+[action] ),problem.getCostOfActions(path)+stepCost)
    return []    
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."
    "*** YOUR CODE HERE ***"
    
    frontier=util.PriorityQueue()  # priority Queue
   # startState=problem.getStartState()
    gcost=0  # path cost from the start node to node n
    hcost=heuristic(problem.getStartState(),problem) #estimated cost of the cheapest path from n to the goal
    fcost=gcost+hcost    # A* evaluates nodes by combining hcost and gcost
    frontier.push((problem.getStartState(),[]),fcost) # initialize the frontier using the initial state of problem,and fcost
    explored=[]      # initialize the explored set to be empty
    if problem.isGoalState(problem.getStartState()):   # check wether the start state is the goal state
        return []
 # loop 
    while not frontier.isEmpty():  # if the frontier is not empty then do
        leaf_node,path=frontier.pop()  # choose a leaf node and remove it from the frontier       
        if problem.isGoalState(leaf_node): # if the node contains a goal state then return the corresponding solution
            return path
        if leaf_node in explored:
           continue
        explored.append(leaf_node)  # add the node to the explored set
        
        # expand the chosen node, adding the resulting nodes to the frontier
        for successor,action,stepCost in problem.getSuccessors(leaf_node):
            if not successor in explored:
     #           totalCost=problem.getCostOfActions(path)+stepCost
                frontier.push((successor, path+[action] ),problem.getCostOfActions(path)+stepCost+heuristic(successor,problem))
    return []    
    
    
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
