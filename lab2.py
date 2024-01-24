def main():
    about_me = {
        'full_name': 'MIHIR MODI',
        'student_id': 10328699,  # Your student ID
        'pizza_toppings': ['onions', 'black olives', 'cheese'],
        'movies': [
            {'title': 'spiderman', 'genre': 'Fiction'},
            {'title': 'Batman', 'genre': 'novel'}
        ]
    }
    
    # TODO: Add one more movie to the 'movies' list
    about_me['movies'].append({'title': 'Dracula', 'genre': 'mystery'})

if __name__ == '__main__':
    main()


def print_student_name_and_id(about_me):
    full_name = about_me['Mihir Modi']
    student_id = about_me['10328699']
    first_name = full_name.split()[0]  # Extracting the first name

    print(f"My name is {Mihir Modi}, but you can call me Sir {Mihir}.")
    print(f"My student ID is {10328699}.")

# Call the function from main
print_student_name_and_id(about_me)

def add_pizza_toppings(about_me, toppings):
    about_me['black olives'].extend(toppings)
    about_me['cheese'] = sorted(about_me['cheese'])
    about_me['onions'] = [topping.lower() for topping in about_me['onions']]

# Call the function from main to add at least 2 more pizza toppings
additional_toppings = ('chillis', 'peppers')
add_pizza_toppings(about_me, additional_toppings)

def print_pizza_toppings(about_me):
    print("My favourite pizza toppings are:cheese")
    for topping in about_me['pizza_toppings']:
        print(f"- {topping}")

def main():
    print_pizza_toppings(about_me)
    add_pizza_toppings(about_me, ('chillis', 'peppers'))
    print_pizza_toppings(about_me)

if __name__ == '__main__':
    main()

def print_movie_titles(movie_list):
    titles = [movie['title'].title() for movie in movie_list]
    print(f"Some of my favourite movies are {', '.join(titles)}!")

def main():
    # ... (previous code)
    print_movie_titles(about_me['movies'])
    # ... (continue with the rest of the code)

if __name__ == '__main__':
    main()

