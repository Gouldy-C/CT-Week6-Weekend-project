# Project Overview:

### You will be creating a Flask application that serves as a Pokédex. Users will be able to log in, collect Pokémon via the PokeAPI, add and remove Pokémon from their Pokédex (profile), and display their Pokémon. You will also create an API blueprint that can get, post and delete Pokémon.

### For extra credit, implement a feature that allows users to battle their Pokémon.

## Project Requirements:

1. User Authentication: Implement user registration and login functionality. Users should be able to register with a username and password, and log in to their account.

2. MCV Architecture: Your application should follow the Model-View-Controller (MVC) architecture.

3. Blueprints: Use blueprints to organize your application into distinct components.

4. Pokémon Collection: Users should be able to collect Pokémon using the PokeAPI. This will involve making GET requests to the PokeAPI and processing the returned data to store in your database as needed.

5. Database Management: Store the Pokémon collected by the user in a database. This will involve creating a model for Pokémon and using SQLAlchemy to add, retrieve, and delete Pokémon.

6. Pokédex Management: Users should be able to add and remove Pokémon from their Pokédex. This will involve creating POST and DELETE routes in your Flask application.

7. Display Pokémon: Users should be able to view the Pokémon in their Pokédex. This will involve creating a GET route that retrieves and displays the user's Pokémon.

8. RESTful API: Create an API blueprint that can post (add a Pokémon to a user's Pokédex) and delete (remove a Pokémon from a user's Pokédex).

## Extra Credit:

1. Pokémon Battles: Implement a feature that allows users to battle their Pokémon. This could involve comparing the stats of two Pokémon and determining a winner. Maybe make it so you can battle other peoples!

#### Remember, the goal of this project is to reinforce the Flask concepts you've learned this week.
#### These are all things you have accomplished in the in-class project and homework. 
#### So make sure to reference those often!