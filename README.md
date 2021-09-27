# Question Analyser

Question Analyser is a survey made with Python, which runs in the Code Institute mock terminal on Heroku.

The user will answer a couple of questions and then have their answered compared to answers people had for the same questions but from a google form.

[Link to live version of the program](https://question-analyser.herokuapp.com/)

## How to use

Using question analyser is extremely simple, all you have to do is answer with either Yes or No when the questions pop up in the terminal.

## Features

### Current Features

* Welcome and walkthrough
  - Shows the user how to use the program
  
![welcome walkthrough](https://user-images.githubusercontent.com/83542146/134925776-3334b3da-4b0d-4b8d-bc5f-5fefd6330497.png)

* Questioning
  - Takes questions from google gspread which is taken from a google form and shows it to the user
  - The user must answer a question to get to the next one
  - Depending on the answer, the user can get more or less questions

* Input validation and error-handling
  - The user must enter either Yes or No
  - Question is repeated if the user doesn't answer with the correct input

![Questions](https://user-images.githubusercontent.com/83542146/134925800-ed436c28-c13f-41aa-8a7d-1093803efe26.png)

* Answers
  - Shows all the questions with how much percentage people answered on yes and no

![Answers](https://user-images.githubusercontent.com/83542146/134925672-e31f3600-71a8-4cd5-b91b-3dfb81fb46a2.png)

### Future Features

* Choose your own google form with your own questions

## Testing

I have tested this project by doing the following:

* Passed the code through a PEP8 linter and confirmed there are no problems
* Given invalid inputs: wrong strings when Yes or No is expected
* Tested in my local terminal and the Code Institute Heroku terminal

### Bugs

#### Solved Bugs
* The answers in the end was in the wrong order so the percentage for yes was replaced by no. This was a simple fix as I just had to replace Yes and No in the code

#### Remaining Bugs
* No bugs remaining


### Validator Testing
* PEP8
 - The error "Blank line at end of file" was returned from PEP8online.com. This was fixed by removing the blank line at the end of the code

## Deployment
This project was deployed using Code Institute's mock terminal for Heroku.

* Steps for deployment:
 - Fork or clone this repository
 - Create a new Heroku app
 - Set the buildpacks to Python and NodeJS in that order
 - Link the Heroku app to the repository
 - Click on Deploy

## Credits

* Code Institute for the deployment terminal
* 
