#Top 100 Schools worldwide

import pandas as pd 
import datetime as dt
df = pd.read_excel("C:\\What\\You\\Have\\Your\\Path\\As\\College.xlsx")


#-Added a decorator to track the time it took to run to completion 
def check_time(function):
    def wrapper(**kwargs): #later on ill be calling a number of functions so kwargs avoided having to type each one in 
        starting_time = dt.datetime.now() #getting current starting time
        print(f"Starting time: {starting_time}")
        result = function(**kwargs) #return the result of each function since they feed into one another
        ending_time = dt.datetime.now() #getting end time
        time_elapsed = ending_time - starting_time #getting total run time
        print(f'Ending time: {ending_time}')
        print(f'Time Elapsed: {time_elapsed}')
        return result
    return wrapper
  
#-Simply getting users name
def get_name():
    while True: #added a while loop which really wasn't necessary but added it for an earlier iteration and never removed it
        try:
            name = input("Hi, I'm here to help you find a school. Press Q to exit. What's your name? ").capitalize()
            if name == 'Q' or name == 'Quit':
                return None
            else:
                return name
        except Exception as e:
            print(f'Error: {e}')
            
#-country block, used to get the users preferred country to study
def get_country(df, name):
    country_list = list(df['Country'].unique()) #getting the name of all unique countries in original df
    for number, country in enumerate(country_list, start=1): #creating an enumerated list
        print(f'{number}: {country}')
    
    while True: #start of while loop
        try:
            country_index = int(input(f"{name}, using the menu above choose a country: ")) #prompting user for their selection
            country = country_list[country_index - 1] #had to subtract by 1 to counter the start = 1
            print(f"You chose {country}, that's a great option, with a vivid history and tons of opportunities to continue your academic education.")
            return country #returning country selection for later use
        except ValueError: #These were the common errors I got when running this so passed them and added a general catch all
            print("Please enter a valid number.")
        except IndexError:
            print("Please enter a number within the specified range.")
        except Exception as e:
            print(f"Error: {e}")
            
#- Block that displays selected countries institutions information. Originally this was a lot more in depth but settled on a simpler 
#implementation. More detailed version is available upon request.
def get_country_information(name, country, df):
    country_info = df[df['Country'] == country]
    country_tuition = country_info['Tuition'].mean() #I did comparisons so saved averages in variables
    general_tuition = df['Tuition'].mean()
    country_score = country_info['Cumlative Score'].mean()
    general_score = df['Cumlative Score'].mean()

    #calling them later on(in earlier iterations if country had more than 5 schools we filtered by one of the columns) 
    print(f"{name} {country} is a great choice, there are {len(country_info)} institutions there.")
    print(f"Average tuition: ${country_tuition:,.2f}, average score: {country_score:.2f}% compared to world average of ${general_tuition:,.2f} and {general_score:.2f}%.")


#- main application
@check_time #decorator to get start and end time
def main():
    df = df = pd.read_excel("C:\\Users\\vturn\\OneDrive\\College.xlsx") #reloading in df within the function
    name = get_name() #calling the get_name() function 
    if name: #You'll see this throughout the function and I just learned how to use it so want to make sure I explain
             #before moving on it essentially means if name == anything: as long as name isnt an empty variable itll run.
             #for example 
             #X = []
             #if X:
             #  print("Hi World!")
             
             #the Hi world block wont be triggered  because X is empty but if we changed it to 
             #X = 9
             #if X:
             # print("Hi World!")
             #it would print "Hi World!" 
             
             #essentially as long as the variable isnt empty it will be triggered
             
        country = get_country(df, name)
        if country: #same thing here because we stored the result of the get_country function in country it is no longer empty
                    #triggering the next block the get_country_information function
            get_country_information(name, country, df)


main()