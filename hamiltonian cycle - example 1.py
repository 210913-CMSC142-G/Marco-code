#python code for Hamiltoninan cycle
#source: pencilprogrammer.com
#with hamiltonian cycle

class Hamiltonian:
  def __init__(self, start):
    #start (& end) vertex
    self.start = start

    #list to store the cycle path
    self.cycle = []

    #variable to mark if graph has the cycle
    self.hasCycle = False

  #method to inititate the search of cycle
  def findCycle(self):
    #add starting vertex to the list
    self.cycle.append(self.start)

    #start the search of the hamiltonian cycle
    self.solve(self.start)

  #recursive function to implement backtracking
  def solve(self, vertex):
    #Base condition: if the vertex is the start vertex
    #and all nodes have been visited (start vertex twice)
    if vertex == self.start and len(self.cycle) == N+1:
      self.hasCycle = True

      #output the cycle
      self.displayCycle()

      #return to explore more cycles
      return

    #iterate through the neighbor vertices
    for i in range(len(vertices)):
      if adjacencyM[vertex][i] == 1 and visited[i] == 0:
        #nbr is the variable for neighbor
        nbr = i
        #visit and add vertex to the cycle
        visited[nbr] = 1
        self.cycle.append(nbr)

        #traverse the neighbor vertex to find the cycle
        self.solve(nbr)

        #Backtrack
        visited[nbr] = 0
        self.cycle.pop()

  #function to display the hamiltonian class
  def displayCycle(self):
    names = []
    for v in self.cycle:
      names.append(vertices[v])
    print(names)
      


if __name__ == '__main__':
  vertices = ['A', 'B', 'C', 'D', 'E']
  adjacencyM = [[0, 1, 1, 0, 1],
                [1, 0, 1, 1, 0],
                [1, 1, 0, 1, 1],
                [0, 1, 1, 0, 1],
                [1, 0, 1, 1, 0,]]
  #list mapping of vertices to mark vertex visited
  visited = [0 for x in range(len(vertices))]

  #number of vertices in the graph
  N = 5

  #Driver code
  hamiltonian = Hamiltonian(0)
  hamiltonian.findCycle()

  #if the graph doesn't have any Hamiltonian Cycle
  if not hamiltonian.hasCycle:
    print("No Hamiltonian Cycle is found")
