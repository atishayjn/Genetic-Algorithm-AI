# CSF407-Genetic-Algorithm
Modified Genetic Algorithm developed for the course CS F407 Artificial Intelligence

## Problem: Genetic Algorithm to solve 3-CNF SAT Problem
Given a propositional logic formula in 3-CNF form, find a model that maximizes the
percentage of satisfied clauses in the formula. The propositional logic formula will be built using
50 variables.

##  Modifications made in the Genetic Algorithm
With a large number of hit and trial experimentation and some
calculated guesses, a good number of changes were made that improved the algorithm.
### Approaches that improved the algorithm:
1. Generate both the children in cross-over
2. Selective Mutation (and removed the condition for mutation)
3. Preserving the Elite Parents
4. Crossing Over in the Middle
5. Mutate and check before culling

### Approaches that failed to give results:
1. Multi-parent Cross Over
2. Weighted random choice for next best population
3. Selective mutation of Elites

### Difficulty of Satisfying a 3-CNF sentence with n variables.
It is observed that for a given number of variables/symbols, 3-CNF sentences become more
difficult to satisfy with the increase in the number of clauses (m). This is for two reasons:
1. With higher values of m, the probability of a 3-CNF sentence to be satisfiable is less as
there are more number of clauses ( and hence more propositional constraints) to be
satisfied by a single model.
2. The complexity to check satisfiability increases with an increase in m.
However, if the number of variables (n) and the number of clauses (m) are less, then 3-CNF is
relatively easier to solve as the complexity is greatly reduced

## Getting Started
1. Refer "question1.pdf" for complete problem statement.
2. Refer "AI A-1 - 2018B5A70908G_Atishay.pdf" for detailed explanation and analysis of the solution.
3. Code for Modified Genetic Algorithm: "GA_App2.py"
