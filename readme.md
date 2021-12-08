# Hamiltonian Path
OUTLINE:
- NP-Complete Problem
- Hamilton’s Game
- Hamiltonian Path
- Hamiltonian Circuit/Cycle
- Applications

NP-COMPLETE PROBLEM:
	Any of a class of computational problems for which no efficient solution algorithm has been found. Many significant computer-science problems belong to this class – e.g., the traveling salesman problem, satisfiability problems, and graph-covering problems. So-called easy, or tractable, problems can be solved by computer algorithms that run in polynomial time; i.e., for a problem of size n, the time or number of steps needed to find the solution is a polynomial function of n. Algorithms for solving hard, or intractable, problems, on the other hand, require times that are exponential functions of the problem size n. Polynomial-time algorithms are considered to be efficient, while exponential-time algorithms are considered inefficient, because the execution times of the latter grow much more rapidly as the problem size increases. A problem is called NP (nondeterministic polynomial) if its solution can be guessed and verified in polynomial time; nondeterministic means that no particular rule is followed to make the guess. If a problem is NP and all other NP problems are polynomial-time reducible to it, the problem is NP-complete. Thus, finding an efficient algorithm for any NP-complete problem implies that an efficient algorithm can be found for all such problems, since any problem belonging to this class can be recast into any other member of the class. It is not known whether any polynomial-time algorithms will ever be found for NP-complete problems, and determining whether these problems are tractable or intractable remains one of the most important questions in theoretical computer science. When an NP-complete problem must be solved, one approach is to use a polynomial algorithm to approximate the solution; the answer thus obtained will not necessarily be optimal but will be reasonably close[^1].
	
HAMILTON'S GAME:
	William Rowan Hamilton invented the Icosian Game in 1857. He is known as one of Ireland’s greatest scholars who also invented quaternions. The aim of this puzzle game is to look for a way around the edges of a dodecahedron so that every corner (vertex) is visited once and only once (Hamiltonian path)[^2].

HAMILTONIAN PATH:
	A Hamiltonian path in a graph G is a path which contains every vertex of G.

HAMILTONIAN CIRCUIT/CYCLE:
	A Hamiltonian cycle (or Hamiltonian circuit) in a graph G is a cycle which contains every vertex of G.

APPLICATIONS:
	Hamiltonian cycles has real applications in diverse fields such as computer graphics, electronic circuit design, mapping genomes, and operations research[^3].

SUMMARY:
- NP-complete problems uses polynomial algorithm to approximate the solution.
- A Hamiltonian Path in a graph G is a path which contains every vertex of G.
- Spanning trees may not necessarily have a Hamiltonian path.
- A Hamiltonian cycle has a Hamiltonian path that begins and end with the same vertex.
- Depth-First Search and Backtracking is utilized in finding a Hamiltonian path/cycle[^4].
- Complete graphs do have Hamilton circuits[^5].

REFERENCES:
[^1]: The Editors of Encyclopædia Britannica, (n.d.). NP-complete problem. Encyclopædia Britannica. Retrieved November 25, 2021, from [https://www.britannica.com/science/NP-complete-problem](https://www.britannica.com/science/NP-complete-problem).
[^2]: Darling, D. (n.d.). Icosian game. Icosian Game. Retrieved November 27, 2021, from [https://www.daviddarling.info/encyclopedia/I/Icosian_Game.html](https://www.daviddarling.info/encyclopedia/I/Icosian_Game.html).
[^3]: Stephanie. (2021, November 30). Hamiltonian cycle: Simple definition and example. Statistics How To. Retrieved December 8, 2021, from [https://www.statisticshowto.com/hamiltonian-cycle/](https://www.statisticshowto.com/hamiltonian-cycle/). 
[^4]: Hamiltonian cycle using backtracking. Pencil Programmer. (n.d.). Retrieved December 2, 2021, from [https://pencilprogrammer.com/algorithms/hamiltonian-cycle-using-backtracking/](https://pencilprogrammer.com/algorithms/hamiltonian-cycle-using-backtracking/). 
[^5]: Libretexts. (2021, September 5). 6.4: Hamiltonian circuits. Mathematics LibreTexts. Retrieved December 3, 2021, from [https://math.libretexts.org/Bookshelves/Applied_Mathematics/Book%3A_College_Mathematics_for_Everyday_Life_(Inigo_et_al)/06%3A_Graph_Theory/6.04%3A_Hamiltonian_Circuits](https://math.libretexts.org/Bookshelves/Applied_Mathematics/Book%3A_College_Mathematics_for_Everyday_Life_(Inigo_et_al)/06%3A_Graph_Theory/6.04%3A_Hamiltonian_Circuits). 
