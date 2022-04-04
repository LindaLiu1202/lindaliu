---
---
title: Create Task
---


## Create Task Ideas
Complex interactive quiz game called "Which BLACKPINK Member Are You?" that can be implemented into the Break Time portion of our website and contains multiple features which expresses creativity. There is a total of 4 questions that contains 4 different options. A numerical value (1, 2, 3 or 4) will be assigned to each of the options, and different ranges of ending point values will correspond to different BLACKPINK members.

Feature ideas: random BLACKPINK fact generator, display BLACKPINK's top YouTube mvs, changeable backgrounds using buttons <br> 

### [Link to Runtime](http://127.0.0.1:5000/quiz1/) <br>

## Requirements
| Requirements       |  Implementation |
| :----:     |     :----:     |
| Program Purpose and Function|  Input will come from user clicking his/her choice under the questions. Program output will return based on which member's number range did the total score of user fells within.     |
|  Data Abstraction  |  A list of facts in random BLACKPINK fact generator. A random math function will generate an index for this list to select a random fact and display it on the page.   |
| Managing Complexity   | The code will be strictly organized. Instead of the facts being stored in individual variables, they are stored in a single list. Without this list the code will be unorganized and the list allows the fact to be called easier. The list containing the word that the user guessed will be called in multiple places to see if any of the letters match any of the corresponding letters in the real word list.   |
|  Procedural Abstraction  |  Functions in js file will be called multiple times in different places. For example, a function to display facts and change background will be in a seperate js file and be called in the html file using functionName().   |
| Algorithm Implementation|  There will be an algorithm that tallies up the users’ answers to the quiz and determines which member their personality is the most like. A numerical value will be assigned to each of the options, and different ranges of ending point values will correspond to different BLACKPINK members.    |


## Code Commits
* [BLACKPINK Quiz html, js, css files(including features: random fact generator, mv display, different background buttons)](https://github.com/samayass/flask_portfolio/commit/8a6449dc3bf1ef47e4489c412af7e0ff20a4b2cd) <br>
* [Add BLACKPINK Quiz to main and navbar](https://github.com/samayass/flask_portfolio/commit/0ae3c1b1d01c6cd3a52a01338614db67488c07f6)


## Written Response Questions - BLACKPINK Quiz
| Number | Question| Answer|
| ----     |    ----   |    ----     |
|3ai |Describes the overall purpose of the program  | Our interactive quiz "Which BLACKPINK Member Are You?" is similar to Buzzfeed personality quiz that is for entertainment and will help users to gain knowledge about BLACKPINK, a 4-people K-pop girl group. The purpose of the program is to let the user answers the questions by choosing one of the four options under the question to see which BLACKPINK member the user's personality is the most like.  |
|3aii |Describes what functionality of the program is demonstrated in the video |The video demonstrates a user interacting with the quiz from top to bottom. In the video, the user is clicking and interacting with the multiple background buttons on the very top of the program. Every time the user clicks a new background button with the image on top of the button, the background image under the header above the buttons will change to the background image that the user clicked. Then, the program contains 4 questions with 4 options that the user can click on. A numerical value (1, 2, 3 or 4) is assigned to each of the options, and different ranges of ending point values will correspond to different BLACKPINK members. After the user has done answering all of the questions, the program contains a submit button which the user can click on and the program will calculate the total score that the user got and display the name and picture of the corresponding member. Below, there are three popular BLACKPINK music videos that the user can watch. On the very bottom, there is a random BLACKPINK fact generator that the user can click on and know more about BLACKPINK! |
|3aiii | Describes the input and output of the program demonstrated in the video  | In the video, the inputs are all the options that the user chose and clicked on when answering the questions. Then, the program will calculate the total score and different ranges of ending point values will correspond to different BLACKPINK members. So the output is the name and picture of the BLACKPINK member that the user's personality is the most like based on the user's choices. It will be display on screen after clicking the submit button. |
|3bi |The first program code segment must show how data have been stored in the list.  |![code1](https://user-images.githubusercontent.com/89208817/156059054-5a85afd3-b306-4e3b-8fc7-9d96f86fa17b.png)|
|3bii |The second program code segment must show the data in the same list being used, such as creating new data from the existing data or accessing multiple elements in the list, as part of fulfilling the program’s purpose.  | ![code2](https://user-images.githubusercontent.com/89208817/156059403-f3f14736-7554-4191-a2c0-e1238e42fa69.png)<br>![code3](https://user-images.githubusercontent.com/89208817/156059958-c8b60881-ea41-499f-87fc-a90702b9ed9b.png)|
|3biii| Identifies the name of the list being used in this response  |The list used in the code above is named "facts".  | 
|3biv | Describes what the data contained in the list represent in your program |The data contained in the list represents 10 facts about BLACKPINK, such as what the name BLACKPINK means.    |
|3bv | Explains how the selected list manages complexity in your program code by explaining why your program code could not be written, or how it would be written differently, if you did not use the list   |  The list allows for the program to store all the facts in one location. Without the list holding the facts the program will become redundant also the facts are all pretty long. One would have to resort to using different variables to hold many different facts in which the code would be unorganized.   |
|3ci |The first program code segment must be a student-developed procedure that:□ Defines the procedure’s name and return type (if necessary) □ Contains and uses one or more parameters that have an effect on the functionality of the procedure □ Implements an algorithm that includes sequencing, selection, and iteration   | ![image](https://user-images.githubusercontent.com/89225503/156255922-431969ef-34a4-4b3e-82ab-5098a8e3b27a.png) |
|3cii |The second program code segment must show where your student-developed procedure is being called in your program.  |![image](https://user-images.githubusercontent.com/89225503/156256035-b55a6b37-2c21-436f-8937-afc268f33599.png)|
|3ciii |Describes in general what the identified procedure does and how it contributes to the overall functionality of the program  |The procedure makes it so that if your answer choices (which have certain points depending on which answer option is chosen) are in a particular range, you will receive a certain character allocated to that point range. The if statements are used in order to state which point ranges will match its respective BlackPink member.|
|3civ |Explains in detailed steps how the algorithm implemented in the identified procedure works. Your explanation must be detailed enough for someone else to recreate it.  |First one should set the number of correctly identified letters to 0 so that it is able to be incremented for each correct letter. Next if statements are used so that each letter of the inputted word can be compared to that of the chosen word, so one should use each letter in the randomly chosen word and equate it to each letter in the inputted word. If the letter is present in the chosen word the correctly identified letters variable should be incremented by one and the color of the tile should be assigned to a data-variable id to change the color of it accordingly. This assigns the member of the band to the point value.| 
|3di |Describes two calls to the procedure identified in written response 3c. Each call must pass a different argument(s) that causes a different segment of code in the algorithm to execute.  |The first call is the return function and the second call function is the get element id that allows the procedure to run through the if statements and submit which member of the band you are.|
|3dii |Describes what condition(s) is being tested by each call to the procedure   |The program accumulates points for each answer option that is recorded. One the user clicks the "Submit" button, the program then calculates the total number of points acquired and follows through a set of if statements in order to associate the point to a member (defined by a point range).|
|3diii |Identifies the result of each call  |The result of the calls is the what member you would be after the user clicks on the "Submit Button."|


## Runtime Features Shown in 1 Minute Video
* [Link to Video](https://drive.google.com/file/d/1Xfp15B5-ZlGGc_erR21kA9IIkjmJ2DQT/view)

## Code in pdf file
* [Link to Code pdf file](https://drive.google.com/file/d/1-OgLqMcDDlNr4sDPg3zfuxY4UbWOWktK/view)

