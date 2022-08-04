from inspect import trace
import random

print('Welcome to the day trip generator! Lets get started so you can be on your way. ')


destinations_for_trip = ['Ohio', 'Miami', 'Atlanta', 'California', 'Mexico', 'Puerto rico']
random_destination = random.choice(destinations_for_trip)
print(f'Would yo like to go to {random_destination}? ')




user_choice = ('yes')

while user_choice == ('yes'):

    if user_choice == input('Do you want to go here, yes or no? '):        
        
        user_choice = 'no' 
        
        print(f'Great, lets go to {random_destination}')
    else:
        random_destination = random.choice(destinations_for_trip)
        print(f'You dont want to go there how about {random_destination}? ')







Restaurants_for_trip = ('Chic fil a', 'Five guys', 'Taco truck', 'Italian restaurant','Indian restaurant')
random_restaurants = random.choice(Restaurants_for_trip)
print(f'Would you like to eat at an, {random_restaurants} while there ')

restaurant_choice = 'yes'

while restaurant_choice == 'yes':
    if restaurant_choice == input('Yes or no? ' ):
        restaurant_choice = 'no'
        print(f'Perfect lets go for the {random_restaurants}')
    else: 
        random_restaurants = random.choice(Restaurants_for_trip)
        
        print(f'Ok, so you dont want to eat there, how about {random_restaurants}? ')
        


Mode_of_transportation = ('car', 'train', 'taxi', 'bus', 'plane')
random_type_of_transportation = random.choice(Mode_of_transportation)
print(f'Would like to get there by, {random_type_of_transportation}? ' )

transportation_types = 'yes'
while transportation_types == 'yes':
    if transportation_types == input('yes or no? '):
        transportation_types = 'no'
        print(f'We will get there by {transportation_types}')
    else:
        random_type_of_transportation = random.choice(Mode_of_transportation)
        print(f'Ok so you dont want to get by the kind of transportation, would you like to go by {random_type_of_transportation}? ')



Entertainment = ('sight seeing', 'ski diving', 'water skiing', 'dirt biking', 'bungee jumping')
random_types_of_entertainment = random.choice(Entertainment)
print(f'While there, for your entertainment would you like to {random_types_of_entertainment}? ')

entertainment_choice = 'yes'
while entertainment_choice == 'yes':
    if entertainment_choice == input('yes or no '):
        print(f'Great lets do {random_types_of_entertainment} when we get there')
        entertainment_choice = 'no'
    else:
        random_types_of_entertainment = random.choice(Entertainment)
        print(f'Oh thats not entertaining to you, how about {random_types_of_entertainment}? ')

print(f'Congratulations, we have generated your day trip, now lets just confirm that this is the trip you wanted.')
input()

print('The trip we have generated for you is')
print(f'Destination: {random_destination}')
print(f'Restaurant: {random_restaurants}')
print(f'Mode of transportaion: {random_type_of_transportation}')
print(f'Form of entertainment {random_types_of_entertainment}')

print(f'would you like to finalize this trip')
input('yes? ')
print(f'Prepare for your exciting vacation! You will be going to {random_destination}, you will be arriving by {random_type_of_transportation}, where you will spend your time {random_types_of_entertainment}, and then going to {random_restaurants}.')
input()