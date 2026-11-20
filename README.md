Pantry to Plate

Project Overview

Pantry to Plate is a Python-based recipe recommendation application designed to help users find meals using ingredients they already have available.

Users can enter ingredients from their pantry, and the application will recommend recipes based on ingredient matches. Recipes will be ranked by match percentage, allowing users to discover meals they can prepare immediately or with only a few additional ingredients.

Project Objectives

Help users make use of ingredients they already have and reduce waste.

Provide recipe recommendations based on available ingredients.

Calculate recipe match percentages.

Identify missing ingredients for each recommended recipe.

Support more convenient and budget-conscious meal planning.

Technologies

Python

Pandas

Tkinter (GUI)

Snowflake (database)

Git and GitHub

Dataset

The project uses three CSV datasets:

File

Description

recipes.csv

Stores recipe details, cuisine, cooking time, servings, and instructions.

ingredients_master.csv

Stores the master list of ingredients and their categories.

recipe_ingredients.csv

Connects recipes to their required ingredients, quantities, and units.

Project Structure

Pantry_To_Plate/
│
├── data/
│   ├── recipes.csv
│   ├── ingredients_master.csv
│   └── recipe_ingredients.csv
│
├── main.py
├── check_data.py
├── requirements.txt
├── README.md
└── .gitignore

Installation

Clone the repository:

git clone https://github.com/charismalim12/Pantry_To_Plate.git

Navigate to the project folder:

cd Pantry_To_Plate

Install the required packages:

pip install -r requirements.txt

Running the Application

Run the main Python file:

python3 main.py

Project Status

Currently in development. Future development includes recipe-matching functionality, Snowflake database integration, and a graphical user interface.

Author

Charisma Lim