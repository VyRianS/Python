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

if __name__ == '__main__':
  flights = []
  # Insert TUPLE values!
  flights.append(('LAX','DFW'))
  flights.append(('SAE','LAX'))
  flights.append(('ORD','LAX'))
  flights.append(('ORD','SAE'))
  
for (x,y) in flights:
  print(make_link(GRAPH,x,y))


