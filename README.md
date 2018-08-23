# StackOverflow-Lite            [![Build Status](https://travis-ci.org/dnuwa/StackOverflow-lite.svg?branch=develop)](https://travis-ci.org/dnuwa/StackOverflow-lite)            [![Coverage Status](https://coveralls.io/repos/github/dnuwa/StackOverflow-lite/badge.svg?branch=develop)](https://coveralls.io/github/dnuwa/StackOverflow-lite?branch=develop)          [![Maintainability](https://api.codeclimate.com/v1/badges/f0ee4bc946330957a26e/maintainability)](https://codeclimate.com/github/dnuwa/StackOverflow-lite/maintainability) 

StackOverflow-lite is a platform where people can ask questions and provide answers. 

## Platform Features

- Users can create an account and log in.
- Users can post questions.
- Users can delete the questions they post.
- Users can post answers.
- Users can view the answers to questions.
- Users can accept an answer out of all the answers to his/her question as the preferred answer. 

## For project contributions

- clone https://github.com/dnuwa/StackOverflow-lite.git to your computer

## Installing and runing the app locally
   - Download project
   Clone the project to your local computer
   
   - Prepare the environment to run the application
   pip install virtualenv or virtualenv enviroment_name
   cd enviroment_name/scripts/activate | this activates the virtual environment
   
   - Install packages in the requirements.txt
   pip install -r requirements.txt

   - run tha app by typing the command python run.py
   - to checkout test coverage, run the code nosetests --with-coverage 

## This Platform is served by  
 - git-pages [GitHub Pages](https://dnuwa.github.io/StackOverflow-lite/UI/).

 - Heroku [Heroku](https://stackoverflow-.herokuapp.com/apidocs/#/.
   - API end points
      - retrieve all users [Users](https://stackoverflow-.herokuapp.com/apidocs/#/Users/get_api_v1_subscribers)
      - retrieve all Questions [Questions](https://stackoverflow-.herokuapp.com/api/v1/questions)
      - retrieve all answers [Answers](https://stackoverflow-.herokuapp.com/apidocs/#/Answers/get_api_v1_answers)
      - retieve a question by id [Questions/<int:qn_id>](https://stackoverflow-.herokuapp.com/apidocs/#/Question/get_api_v1_questions__qn_id_)
      - post an answers to a particular qn [<int:qn_id>/answers](https://stackoverflow-.herokuapp.com/apidocs/#/Answer/post_api_v1__qn_id__answers)

