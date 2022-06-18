#Nimna Wijedasa;Mehvish Shakeel
#You may only use built-in Python functions that support compound data structures, user entry, or casting (such as len(), input() or int()).
#You may use other modules such as pandas or csv for importing the data only.
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

class Country:
    """A class used to create a country object.

        Attributes:
            choice (str): String that represents the selected country of the user
            country (arr): an array that contains the country data values
            population (arr): an array that contains the population data values
            threatened (arr): an array that contains the threatned species data values
            country_list (list): a list of countries
    """
    def __init__(self,user_country_choice,country_basic_data_array,population_year_data_array,threatened_species_data_array,country_list):
        self.choice = user_country_choice                              
        self.country = country_basic_data_array
        self.population = population_year_data_array
        self.threatened = threatened_species_data_array
        self.country_list = country_list

    def endangered_species(self,user_threatened_species_choice):
        """A function that prints the number of selected threatned species.

        Parameters: user_threatened_species_choice
        Return: None

        """
    
        for i in range(len(self.country_list)):
            if self.choice == self.threatened[i][0]:
                if user_threatened_species_choice == 'p':
                    print("There are", self.threatened[i][1],"endangered Plants in",self.choice,"." )
                elif user_threatened_species_choice == 'f':
                    print("There are", self.threatened[i][2],"endangered Fish in",self.choice,"." )
                elif user_threatened_species_choice == 'b':
                   print("There are", self.threatened[i][3],"endangered Birds in",self.choice,"." )
                else:
                    print("There are", self.threatened[i][4],"endangered Mammals in",self.choice,"." )

    def gen_info(self,un_region_endangered):
        """A function that returns a list of endangers species in a region.

        Parameters: un_region_endangered
        Return: endangered_by_un_reigeon_list

        """
        un_countries_list = []
        plants = []
        fish = []
        birds = []
        mammals = []

        for i in range(len(self.country_list)):                              
            if un_region_endangered == self.country[i][1]:
                un_countries_list.append(i)

        for i in range(len(un_countries_list)):
            plants.append(self.threatened[un_countries_list[i]][1])
            fish.append(self.threatened[un_countries_list[i]][2])
            birds.append(self.threatened[un_countries_list[i]][3])
            mammals.append(self.threatened[un_countries_list[i]][4])

        endangered_by_un_reigeon_list = [sum(plants),sum(fish),sum(birds),sum(mammals)]
        return endangered_by_un_reigeon_list

    def pop_den_calc(self,pop_year):
        """A function that returns the population density of the selected country.

        Parameters: pop_year
        Return: the population density

        """
        index_year = (pop_year - 1999)
        for i in range(len(self.country_list)):
                if self.choice == self.population[i][0]:
                    return (int(self.population[i][index_year])//int(self.country[i][3]))

    def pop_change_info(self,starting_year,ending_year):
        """A function that prints the change in population over a given time.

        Parameters: starting_year,ending_year
        Return: None

        """
        
        begin_year = (starting_year - 1999)
        end_year = (ending_year-1999)
        for i in range(len(self.country_list)):
                if self.choice == self.population[i][0]:
                    print(int(self.population[i][end_year])-int(self.population[i][begin_year]))
    
    def min_max_avg_cal(self,user_pop_info_choice):
        """A function that prints the minimum/maximum/avg of the selected country.

        Parameters: user_pop_info_choice
        Return: None

        """
        if user_pop_info_choice == 'mn':
            for i in range(len(self.country_list)):
                    if self.choice == self.population[i][0]:
                        minimum_val = min(population_year_data_array[i,1:])
                        print('the minimum population was ',minimum_val) 

        elif user_pop_info_choice == 'mx':
            for i in range(len(self.country_list)):
                    if self.choice == self.population[i][0]:
                        maximum_val = max(population_year_data_array[i,1:])
                        print('the maximum population was ',maximum_val) 

        else:
            for i in range(len(self.country_list)):
                    if self.choice == self.population[i][0]:
                        avg_val = int(np.average(population_year_data_array[i,1:]))
                        print('the average population was ',avg_val) 

def get_graph_val(population_year_data_array,user_country_choice,country_list):  
    """A function that returns an array of the selected country's population trend.

    Parameters: population_year_data_array,user_country_choice,country_list
    Return: population_year_data_array

    """
    for i in range(len(country_list)):
        if user_country_choice == population_year_data_array[i][0]:
            return population_year_data_array[i,1:]

def print_invalid():
    """A function that prints the invalid statement.

    Parameters: None
    Return: None

    """
    print('your input is invalid please select a valid option')      

def UN_country_data(country_basic_data_array,country_list,user_UN_region_choice,user_country_choice):
    """A function that returns an array containing country data.

    Parameters: country_basic_data_array,country_list,user_UN_region_choice,user_country_choice
    Return: data array containing the users choice information

    """
    for i in range(len(country_list)):
        if user_country_choice == country_basic_data_array[i][0]:
            if user_UN_reigeon_choice == 'u':
                return country_basic_data_array[i][1]
            elif user_UN_reigeon_choice == 's':
                return country_basic_data_array[i][2]
            elif user_UN_reigeon_choice == 'a':
                return int(country_basic_data_array[i][3])         
    
country_basic_data = pd.read_csv(r'Country_Data.csv')                      #uses pandas to import files
population_year_data = pd.read_csv(r'Population_Data.csv')
threatened_species_data = pd.read_csv(r'Threatened_Species.csv',sep='\t')

country_basic_data_array = country_basic_data.to_numpy()                   #We use numpy to create an array.
population_year_data_array = population_year_data.to_numpy()
threatened_species_data_array = threatened_species_data.to_numpy()

country_list=(country_basic_data_array[:,0])                               #We slice the array.


# main function


def main():
    users_input_is_valid = False                                               #We create a while loop to ensure a correct country is entered.  
    while users_input_is_valid == False:

        user_country_choice = input("What country would you like to know about?\n")   #We prompt the user to enter country.
        country_class = Country(user_country_choice,country_basic_data_array,population_year_data_array,threatened_species_data_array,country_list)

        if user_country_choice in country_list:                                         
            user_secondary_choice_is_valid = False                                         # We assign false to second boolian variable.
            while user_secondary_choice_is_valid == False:                                 # We start a while loop for the first menu.
                print("\nWhat would you like to know about", user_country_choice ,"?\n ", 
                    "\n  Endangerd species                                        - e\n",
                    " UN Country data                                          - c\n",
                    " Population                                               - p\n",
                    " General inormation about another country (graph)         - g\n",
                    " Compare population trends across two countries (graph)   - pl\n"
                    "  Return to previous menu                                  - q\n")  
                user_country_info_choice = input('Please select the appropirate letter corresponding to your choice (case sensitive) : ')

                if user_country_info_choice == 'q':                                       # We end the loop
                    user_secondary_choice_is_valid = True                                 # We end the loop by asigning false to the second boolean variable

                elif user_country_info_choice == 'g':
                    
                    third_boolean = False
                    while third_boolean == False:                                        # We create another loop by asigning false to the thrid boolean variable.
                        print('What kind of General inormation about another country would you like to know about?\n',   # For second menu with prompt.
                                'Endangered species by UN region                            - r\n',
                                'A comparison of endangered species by UN region (graph)    - c\n'
                                " Return to previous menu                                   - q\n")
                        user_UN_endangered_choice = input('Please select the appropirate letter corresponding to your choice (case sensitive) : ')

                        if user_UN_endangered_choice == 'q':                            
                            third_boolean = True    
                            break                                                        #we end the current loop

                        elif user_UN_endangered_choice == 'r':                         
                            third_boolean = True
                            fourth_boolean = False                                       #We create another loop by asigning the forth boolean as false.

                            while fourth_boolean == False:
                                
                                print("Which UN regeon would you like to know about?\n", #For third menu with prompt.
                                "Asia\n",
                                "Europe\n",
                                "Africa\n",
                                "Americas\n",
                                "Oceania\n",
                                "To return to the previous menu type - 'q'\n")

                                un_region_endangered = input('Please select the appropirate region corresponding to your choice (case sensitive) : ')
                                if un_region_endangered == 'Asia':                       
                                    fourth_boolean = True
                                    user_secondary_choice_is_valid = True
                                    users_input_is_valid = True
                                    threat_list = country_class.gen_info(un_region_endangered) #We use object instance of the class.
                                    print('In',un_region_endangered,'there are',threat_list[0], 'plants',threat_list[1],'fish',threat_list[2],'birds',threat_list[3],'mammals')
                                    
                                elif un_region_endangered == 'Europe':
                                    fourth_boolean = True
                                    users_input_is_valid = True
                                    user_secondary_choice_is_valid = True
                                    threat_list = country_class.gen_info(un_region_endangered)
                                    print('In',un_region_endangered,'there are',threat_list[0], 'plants',threat_list[1],'fish',threat_list[2],'birds',threat_list[3],'mammals')
                                    
                                elif un_region_endangered == 'Africa':
                                    fourth_boolean = True
                                    users_input_is_valid = True
                                    User_secondary_choice_is_valid = True
                                    threat_list = country_class.gen_info(un_region_endangered)
                                    print('In',un_region_endangered,'there are',threat_list[0], 'plants',threat_list[1],'fish',threat_list[2],'birds',threat_list[3],'mammals')
                                    
                                elif un_region_endangered == 'Americas':
                                    fourth_boolean = True
                                    users_input_is_valid = True
                                    User_secondary_choice_is_valid = True
                                    threat_list = country_class.gen_info(un_region_endangered)
                                    print('In',un_region_endangered,'there are',threat_list[0], 'plants',threat_list[1],'fish',threat_list[2],'birds',threat_list[3],'mammals')
                                    
                                elif un_region_endangered == 'Oceania':
                                    fourth_boolean = True
                                    users_input_is_valid = True
                                    user_secondary_choice_is_valid = True
                                    threat_list = country_class.gen_info(un_region_endangered)
                                    print('In',un_region_endangered,'there are',threat_list[0], 'plants',threat_list[1],'fish',threat_list[2],'birds',threat_list[3],'mammals')
                                    
                                elif un_region_endangered == 'q':
                                    fourth_boolean = True
                                else:
                                    print_invalid()

                        elif user_UN_endangered_choice == 'c':     # plots the bar graph for endanged species in each UN region
                            users_input_is_valid = True
                            endangered_species_sum = [sum(country_class.gen_info('Asia')),sum(country_class.gen_info('Europe')),sum(country_class.gen_info('Africa')),sum(country_class.gen_info('Americas')),sum(country_class.gen_info('Oceania'))]
                            reigeon = ['Asia', 'Europe', 'Africa', 'Americas', 'Oceania']
                            fig = plt.figure(figsize = (10, 5))
                            plt.bar(reigeon, endangered_species_sum, color=['orange', 'purple', 'red', 'blue', 'cyan'],width = 0.4)
                            plt.ylabel('number of endangered species') 
                            plt.xlabel('UN region')
                            plt.title("Endangered species by UN region")
                            plt.show()
                            third_boolean = True     
                            user_secondary_choice_is_valid = True                   

                        else:
                            print_invalid()

                elif user_country_info_choice == 'p':            # For the 1st choice population info asks what about the population they would like to know about
                    user_secondary_choice_is_valid = True
                    users_input_is_valid = True
                    secondary_boolean = False
                    while secondary_boolean == False:
                        print(f"What would you like to know about{user_country_choice}'s population?\n",
                        'Change over time                           : ct\n',
                        'Maximum population                         : mn\n',
                        'Minimum population                         : mx\n',
                        'Average population across all years        : ap\n',
                        'Return to previos menu                     : q\n')
        
                        user_pop_info_choice = input('Your choice (letter is case sensitive)\n')  # goes back to the previous menu
                        if user_pop_info_choice == 'q':
                            secondary_boolean = True
                            user_secondary_choice_is_valid = False

                        elif user_pop_info_choice == 'ap':                # prints the average population
                            secondary_boolean = True
                            country_class.min_max_avg_cal(user_pop_info_choice)

                        elif user_pop_info_choice == 'mn':                 # prints the minimum population          
                            secondary_boolean = True
                            country_class.min_max_avg_cal(user_pop_info_choice)

                        elif user_pop_info_choice == 'mx':                # prints the maximum population
                            secondary_boolean = True
                            country_class.min_max_avg_cal(user_pop_info_choice)

                        elif user_pop_info_choice == 'ct':                    # print the population change over time
                            secondary_boolean = True
                            fourth_boolean = False
                            while fourth_boolean == False:
                                print( 'Please enter a starting year and ending year.\n')        # asks for the staring and ending years and verifies that the ending year is after the starting year
                                starting_year = int(input('Starting year:')) 
                                ending_year = int(input('Ending year:'))
                                if (starting_year not in range(1999,2021)) or (ending_year not in range(1999,2021)):
                                        print('Please enter a starting and ending year in the range 2000 - 2020 (inclusive).\n')
                                elif starting_year > ending_year:
                                    print("The starting year can't be grater than the ending year." )
                                else:
                                    fourth_boolean = True
                                    country_class.pop_change_info(starting_year,ending_year) 
                        else:
                            print_invalid()

                elif user_country_info_choice == 'c':
                    user_secondary_choice_is_valid = True       # if the user wishes to know about the country data.
                    users_input_is_valid = True
                    third_boolean = False
                    while third_boolean == False:  # Gives another menu by asigning the the third boolean false.
                        print(f'\nWhat would you like to know about {user_country_choice}\'s UN data?\n please select the appropriate letter' ,
                                "\n  UN region                 - u\n",
                                " UN sub-region             - s\n",
                                " Area                      - a\n",
                                " Population density        - p\n",
                                " Return to previous menu   - q\n")
                    
                        user_UN_reigeon_choice = input('Your choice (letter is case sensitive):\n')
                        if user_UN_reigeon_choice == 'q':   #To return the menu
                            third_boolean = True
                            user_secondary_choice_is_valid = False
                        elif user_UN_reigeon_choice == 'u' : #To find the UN region
                            third_boolean = True
                            print(UN_country_data(country_basic_data_array,country_list,user_UN_reigeon_choice,user_country_choice))
                        elif user_UN_reigeon_choice == 's':  #To find in UN sub region
                            third_boolean = True
                            print(UN_country_data(country_basic_data_array,country_list,user_UN_reigeon_choice,user_country_choice))
                        elif user_UN_reigeon_choice =='a':   #To find area
                            third_boolean = True
                            print(UN_country_data(country_basic_data_array,country_list,user_UN_reigeon_choice,user_country_choice))
                        elif user_UN_reigeon_choice == 'p':  #To find population density 
                            fourth_boolean = False
                            while fourth_boolean == False:
                                pop_year = int(input('Please enter a year you want the population density for:\n')) #Prompt the user to year 
                                if (pop_year not in range(1999,2021)):
                                    print('Please enter a year in the range 2000 - 2020 (inclusive):\n')
                                else:
                                    fourth_boolean = True   
                                    third_boolean = True
                                    print("The population density in",pop_year,"is",country_class.pop_den_calc(pop_year),'people per square Kilometer :')
                        else:
                            print_invalid() 
                            
                elif user_country_info_choice == 'e': #if the user wishes to know about the endangered species.
                    user_secondary_choice_is_valid = True
                    users_input_is_valid = True
                    third_boolean = False
                    while third_boolean == False:
                        print(f"\nWhich endangered species of {user_country_choice} would you like to know about?\n", #Gives another menu by asigning the the third boolean false.
                                "\n  Plants - p\n",
                                " Fish - f\n",
                                " Birds - b\n",
                                " Mammals - m\n",
                                " Return to previous menu - q\n")
                        user_threatened_species_choice = input('Please select the appropirate letter corresponding to your choice (case sensitive) : ')
                        
                        if user_threatened_species_choice == 'q': #To return to the previous menu
                            third_boolean = True
                            user_secondary_choice_is_valid = False
                        elif user_threatened_species_choice == 'p' or 'f' or 'b' or 'm': #To know about Fish, Birds or Mammals
                            country_class.endangered_species(user_threatened_species_choice)
                            third_boolean = True
                        else:
                            print_invalid()

                elif user_country_info_choice == 'pl': #if the user wishes to get a graph comparing population trends across two countries .
            
                    y = get_graph_val(population_year_data_array,user_country_choice,country_list)
                    x=[]
                    for i in range(2000,2021):
                        x.append(i)

                    y_label = user_country_choice
                    plt.suptitle('Comparison of population across two countries') #To plot first graph of users choe. 
                    plt.subplot(2,1,1)
                    plt.plot(x,y, label = user_country_choice)
                    plt.ylabel('population') #Label y axis as population.
                    plt.xlabel('Year') #Label x axis as year.
                    plt.legend()
                    plt.xticks(x,x)

                    third_boolean = False
                    while third_boolean == False:
                        user_compare_plot_choice_country = input('What other country would you like to compare\n') #To plot second graph of the users choice.
                        if user_compare_plot_choice_country in country_list:

                            y = get_graph_val(population_year_data_array,user_compare_plot_choice_country,country_list) #Use the function to get y values to plot.
                            x=[]
                            for i in range(2000,2021):
                                x.append(i)

                            y2_label = user_compare_plot_choice_country
                            plt.subplot(2,1,2)
                            plt.plot(x,y,'r', label = user_compare_plot_choice_country)
                            plt.ylabel("Population") #Label y axis as population
                            plt.xlabel('Year') #Label x axis as year
                            plt.xticks(x,x)
                            plt.legend() 
                            plt.show() #display all the functions
                            third_boolean = True
                        
                        else:
                            print('Please enter a valid country')
                            

                    user_secondary_choice_is_valid = True #Assign the booleans as True to leave th loop
                    users_input_is_valid = True    

                else:
                    print_invalid()

        else:
            print_invalid() 
if __name__ == '__main__':
    main()