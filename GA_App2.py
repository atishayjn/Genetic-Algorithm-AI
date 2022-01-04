import random, csv, time

# Methods to modify
# 1. Champions (Elitism)
# 2. More than 2 parents
# 3. Slicing smartly - Slicing from middle, generate two children at least.
# 4. Mutating differently
# 5. Taking just best 2 to generate new population.
# 6. Start smartly.
# Look at each function for improvements.

# Rn just applied condition on child

class GA_App2:
    def __init__(self, pop_size):
        self._pop_size = pop_size
        self._population = self.randomSolutions(pop_size)
        self._champions = list()

    def randomSolutions(self, k):   # k = population size/ Number of Models

        models = list()

        for i in range(k):
            model = list()
            for j in range(1, 51):  # n = 50
                model.append(j if random.choice(range(2)) else -j) # can optimize by using 0/1 instead, change isSAT too
            models.append(model)
        
        return models

    def isSAT(self, clause, model):
        for symbol in clause:
            num = int(symbol)       # convert string to num
            # print("------ (DEBUG) In SAT : Model len ---------")
            # print(len(model))
            # print(num)
            if ((num < 0)):
                if (model[(-num) - 1] > 0):
                    return False
            else:
                if (model[num - 1] < 0):
                    return False
        return True

    def fitness(self, sentence, model):

        num_clause = len(sentence)
        count = 0

        for clause in sentence:
            if (self.isSAT(clause, model)):
                    count += 1
    
        fit = (count / num_clause)*100

        return fit
    
    def getWeights(self, population, sentence):
        weights = list()

        for model in population:
            weights.append(self.fitness(sentence, model))

        return weights

    def crossOver(self, parent1, parent2, sentence):
        pos = random.choice(range(1, 50))

        # print ("DEBUG - Slicing Position = ", pos)
        s1 = parent1[0:pos]
        s2 = parent2[pos:]
        child1 = s1 + s2

        s1 = parent2[0:pos]
        s2 = parent1[pos:]
        child2 = s1 + s2
        
        if (self.fitness(sentence, child1) > self.fitness(sentence, child2)):
            return child1
        else:
            return child2

    def mutate(self, child):
        pos = random.choice(range(50))
        child[pos] = -child[pos]    #change this for 0/1 representation of model.
        return child

    def nextGen(self, sentence, population):

        pop_size = len(population)

        # assign weights
        fit_arr = self.getWeights(population, sentence)

        children = list()

        for i in range(pop_size):
            # choose two parents according to weights
            parent1, parent2 = random.choices(population, weights = fit_arr, k=2)

            # reproduce
            child = self.crossOver(parent1, parent2, sentence)

            # mutate
            if (self.fitness(sentence, child) < 40):
                child = self.mutate(child)

            children.append(child)

        return children 

    def runGA(self, sentence, population):

        t_end = time.time() + 2
        while time.time() < t_end:
            children = self.nextGen(sentence, population)
            population = children
        return population
    

def main():
    solver = GA_App2(20)

    with open('CNF2.csv') as csvfile:
        rows = csv.reader(csvfile)
        rows = list(rows)
    sentence = [[int(i) for i in ro] for ro in rows]
    
    # model = solver.randomSolutions(1)[0]

    # print(sentence)
    # print(model)

    # print(solver.fitness(sentence, model))
    # print(solver.randomSolutions(2))

    print("\n==============PARENT============")
    # for model in solver._population:
    #     print(model)
    
    parent_fit = solver.getWeights(solver._population, sentence)
    avg = sum(parent_fit)/len(parent_fit)
    print("\nFitness = ", parent_fit)
    print("Fitness Average= ", avg)
    children = solver.runGA(sentence, solver._population)
    
    print("\n==============CHILDREN============")
    children_fit = solver.getWeights(children, sentence)
    avg = sum(children_fit)/len(children_fit)
    print("\nFitness = ", children_fit)
    print("Fitness Average = ", avg)

    # for model in children:
    #     print(model)
    
if __name__=='__main__':
    main()