import config

nucleotides_map = {'A': 1, 'T': 2, 'C': 3, 'G': 4, 'a': 1, 't': 2, 'c': 3, 'g': 4, '-': 5}

class GA:
    def __init__(self,sequences):
        self.sequences = sequences
        self.population_size = config.GA_POPULATION_SIZE
        self.number_iterations = config.GA_NUM_ITERATION
        self.population = []
        self.population_score = []

    #Generate population for the Genetic Algorithm
    def generate_population(self):
        for i in range(self.population_size):
            self.population.append([[nucleotides_map[self.sequences[i][j]] for j in range(len(self.sequences[i]))] for i in range(len(self.sequences))])

    #Sum-of-pairs
    def calculate_fitness_score(self):
        self.population_score = []
        for index_chromosome,chromosome in enumerate(self.population):
            num_sequences = len(chromosome)
            score = 0
            for i in range(len(chromosome[0])):
                for j in range(num_sequences):
                    for k in range(j + 1, num_sequences):
                        if chromosome[j][i] == 5 or chromosome[k][i] == 5:
                            score += config.GAP_PENALTY
                        elif chromosome[j][i] == chromosome[k][i]:
                            score += config.MATCH_REWARD
                        elif chromosome[j][i] != chromosome[k][i]:
                            score += config.MISMATCH_PENALTY
            self.population_score.append((index_chromosome,score))
    
    def selection_and_crossover(self):
        #Selection
        #Sort the population based on the score
        population_score_sorted = sorted(self.population_score, key=lambda x: x[1], reverse=True)
        #Get the index of the most fitted individuals
        most_fitted_indexes = [item[0] for item in population_score_sorted[:config.GA_NUM_MOST_FIT_FOR_ITER]]
        #Delete individuals with the worst score 
        for index in sorted(most_fitted_indexes,reverse=True):
            self.population.pop(index)
        
        
        #Calculation of the mean length of a sequences, to calculate the position in which we cut every sequence in a chromosome
        number_of_nucleotides = []
        for genes in self.population[0]:
            number_of_nucleotides.append(len(genes))
        mean_length = int((sum(number_of_nucleotides) / len(number_of_nucleotides)) / 2)
        
        #Crossover
        new_individuals = []
        for j in range(2): #Repeat two times to have a costant number of population (with one iteration we generate only the half of GA_NUM_MOST_FIT_FOR_ITER individuals)

            for i in range(0, len(self.population) - 1,2):
                parent1 = self.population[i]
                parent2 = self.population[i+1]
                first_half_parent1 = []
                second_half_parent2 = []

                #First half of genes from parent1
                for genes in parent1:
                    first_half = genes[:mean_length]
                    first_half_parent1.append(first_half)

                #Second half of genes from parent2
                for genes in parent2:
                    second_half = genes[mean_length:]
                    second_half_parent2.append(second_half)
                
                #Contruct the new individual
                new_chromosome = []
                for k in range(len(first_half_parent1)):
                    new_chromosome.append(first_half_parent1[k] + second_half_parent2[k])
                new_individuals.append(new_chromosome)

        #Update the population with new individals
        new_population = self.population + new_individuals
        self.population = new_population

'''
#Test

import dataset3

dataset = dataset3 

ga = GA(dataset.test2)

ga.generate_population()

ga.calculate_fitness_score()

ga.selection_and_crossover()
'''