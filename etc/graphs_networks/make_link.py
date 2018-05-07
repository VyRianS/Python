#!/usr/bin/python3.6

# Graphs & Networks

# Social Networks, Maps, Relationships

# Our Goal: Shortest Path

# What is a graph / network
## - Node
## - Edges

# How to make a Graph/Network in Python?

GRAPH = {}

def make_link(Graph, node1, node2):
  # A graph will be a dictionary containing nodes.
  # These nodes will be a dictionary of neighbor nodes.
  # The node's dict. key will be the neighbor node and its value will be 1.

  # In other words, we insert values into dictionaries to model the graph.

  # Check that nodes are registered in Graph
  if node1 not in Graph:
    Graph[node1] = {}
  if node2 not in Graph:
    Graph[node2] = {}

  # Add information about the nodes themselves
  (Graph[node1])[node2] = 1
  (Graph[node2])[node1] = 1

  return Graph

def marked_node(Graph, node, marked):
  # node is the STARTING NODE
  # Mark node if it is unmarked
  marked[node] = 'True'
  total_marked = 1
  # Check Graph information to find neighboring nodes.
  # Graph = {'LAX':{'DAE':1}, 'DAE':{'LAX':1,'ORD':1} ... }
  # BASE CASE: When it reaches the ends of the graph.
  for n_node in Graph[node]:
    if n_node not in marked:
      total_marked += marked_node(Graph, n_node, marked)
  return total_marked
        
def list_node_sizes(Graph):
  marked = {} #??
  for node in Graph.keys():
    if node is not in marked:
      print('Graph ',Graph,' containing', node, ':', marked_node(Graph, node, marked))

def is_connected(Graph, node1, node2):
  # Start from node1 to node2, returning TRUE or FALSE
  marked = {}
  # Mark all the nodes with the same function
  marked_node(Graph,node,marked)
  if node2 in marked:
    return 'TRUE'
  else:
    return 'FALSE'

def construct_graph(Graph):
  flights = []
  # Insert TUPLE values!
  flights.append(('LAX','DFW'))
  flights.append(('SAE','LAX'))
  flights.append(('ORD','LAX'))
  flights.append(('ORD','SAE'))
  
  for (x,y) in flights:
    make_link(Graph,x,y)
  
  return Graph

if __name__ == '__main__':
  construct_graph(GRAPH)

