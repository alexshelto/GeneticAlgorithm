/*
Alexander Shelton
6/7/19
Simple C++ Genetic algorithm program


Randomizes first 225 digits of e




Genetic Algorithm Outline:
--------------------------
1.) Random Initialize populations
2.) Determine fitness of population
3.) Until convergence, repeat:
    a.) Select parents from population
    b.) Crossover and generate new populations
    c.) Preform mutation on new populations 
    d.) Calculate fitness for new population
*/



#include <iostream>
#include <random>
#include <string>
#include <algorithm>
#include "time.h"
using namespace std;



const int  POPULATION_SIZE = 150;

// Valid Genes 
const string GENES = "0123456789."; 

//string to be generated
const string Target = "2.71828182845904523536028747135266249775724709369995957496696762772407663035354759457138217852516642742746639193200305992181741359662904357290033429526059563073813232862794349076323382988075319525101901157383418793070215408914";
//"2.718281828459045235360287471352662497757247093699959574966967627724076630353";

//Function generates random numbers in a given range
int randomNum(int start, int end);
//create random genes for mutation 
char mutated_genes();

//create string of genes:
string create_gnome();



class Individual{
    public:
    string chromosome;
    int fitness;
    Individual(string chromosome);
    Individual mate(Individual parent2);
    int calculateFitness();
};

Individual::Individual(string chromosome){
    this -> chromosome = chromosome;
    fitness = calculateFitness();
}

//mating to produce new offspring:
Individual Individual::mate(Individual parent2){
    //chromosome for offspring:
    string child_chromosome = "";

    int len = chromosome.size();

    for(int i = 0; i < len; i++){
        //random probablility
        float p = randomNum(0, 100)/100; //mutation rate calc
        if( p < .45) //if probablility is < .45 insert gene from parent 1
            child_chromosome += parent2.chromosome[i];
        else if(p < 0.80)//if prob is between .45 and .90 insert gene from parent 1
            child_chromosome += chromosome[i];
        else
            child_chromosome += mutated_genes();
    }
    //create new individual offspring
    //by creating a new instance of an individual with the selected chromosomes
    return Individual(child_chromosome);
}


//calculating fitness scorre is the number of characters in the string that
//are the same or different
int Individual::calculateFitness(){
    int len = Target.size();
    int fitness = 0;
    for(int i = 0; i < len; i++){
        if(chromosome[i] != Target[i])
            fitness++;
    }
    return fitness;
}

bool operator < (const Individual &i1, const Individual &i2){
    return i1.fitness < i2.fitness;
}




int main(){

    clock_t t1,t2;

    t1 = clock();
    srand((unsigned)(time(0)));

    //current generation:
    int generation = 0;
    vector<Individual> population;
    bool found = false;

    //create initial population:
    for(int i = 0; i < POPULATION_SIZE; i++){
        string gnome = create_gnome();
        population.push_back(Individual(gnome)); //population is an array of elements, elements are individual letters -dna-
    }

    while( ! found)
    {
        //arrange population in order of fitness score:
        sort(population.begin(), population.end());

        //if an individual has a fitness of 0 we know we have found it:
        if(population[0].fitness <= 0){
            found = true;
            break;
        }
        //create new generation:
        vector<Individual> new_gen;

        //survival of the fittest: 15% of offspring make it to next gen
        int s = (15*POPULATION_SIZE)/100;
        for(int i = 0; i < s; i++)
            new_gen.push_back(population[i]);

        //mating
        s = (95*POPULATION_SIZE)/100;
        for(int i = 0; i < s; i++){
            //int len = population.size();
            int r = randomNum(0,50);
            Individual parent1 = population[r];
            r = randomNum(0,50);
            Individual parent2 = population[r];

            Individual offspring = parent1.mate(parent2);
            new_gen.push_back(offspring);
        }
        cout << "pass";
        population = new_gen;
        cout << "Generation: " << generation << "\n";
        cout << "String: " << population[0].chromosome << "\n";
        cout << "Fitness: " << population[0].fitness << "\n";

        generation++; //incrementing the population
    }

    t2 = clock();
    float diff ((float)t2-(float)t1);
    float sec = diff / CLOCKS_PER_SEC;



    cout << "\n\n================== RESULT ==================" << endl;
    cout << "Generation: " << generation << "\n";
    cout << "String: " << population[0].chromosome << "\n";
    cout << "Fitness: " << population[0].fitness << "\n";

    cout << "\n\nExecution time: " << sec << endl;
    return 0;
}


int randomNum(int start, int end){
    int range = (end - start)+1;
    int randomInt = start+(rand()%range);
    return randomInt;
}

char mutated_genes(){
    int len = GENES.size();
    int random = randomNum(0, len-1);
    return GENES[random];
}

string create_gnome(){
    int len = Target.size();
    string gnome = "";
    for(int i = 0; i < len; i++)
        gnome += mutated_genes();
    return gnome;
}





