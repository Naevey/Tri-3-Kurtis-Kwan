![image](https://user-images.githubusercontent.com/28553165/162357629-de2ff564-a2b1-45c1-83dd-388a4a4fc490.png)
![image](https://user-images.githubusercontent.com/28553165/162357678-2165673f-0a23-4e7c-83c9-5a5f654d0e86.png)


# [Video](https://www.loom.com/share/e5e04a182e5d431e993df2578e155e70)
|Number|Part|Answer|
|--|---|---|
|3a.|i.|The overall purpose of this program is a fun hangman game, where the user can guess various authors and books. |
|   |ii.|As shown in the video, each button matches the corresponding letter of the alphabet and clicking the wrong ones will start to draw a hangman. With 7 mistakes, the game will end.|
|   |iii|The video shows the input buttons, to start to guess the word created. The output is either the dashes changing to the letter or the hangman, slowly appearing.| 
|**3b.**|i.|![image](https://user-images.githubusercontent.com/28553165/155860146-a815ef95-af66-46de-99d9-aaf3f22f3390.png)<br/>The list has been stored in a variable|
|    |ii. |![image](https://user-images.githubusercontent.com/28553165/155860178-af2e0b95-3579-4558-a77c-977afb1f17e9.png)|
|    |iii.|The authors list is being used to choose a random word and set that word as the variable, answer. |
|    |iv.|The list represents the list of words that the game will take a random word from, to use as the answer.|
|    |v.|The list makes sure that the word to be guessed is different every time, so it is not predictable. If the list was not used, it would be the same word guessed every time. We tried to include an API to have the list, but it would have formatting issues, such as spaces, and the introduction of capital letters. We had to use - as a placeholder for space because it would cause issues with the formatting. |
|**3c.**|i.|![image](https://user-images.githubusercontent.com/28553165/155860230-f0284466-b881-49ba-adfc-5fb43c77f3ec.png)|
|    |ii.|![image](https://user-images.githubusercontent.com/28553165/155860241-97402957-47a4-4f5c-a6e7-d737b5df6619.png)|
|    |iii.|The function Handleguess makes sure that the guessed letter, is either right or wrong. This would then update the cartoon, the number of wrong guesses, and the blanks. This is the overall function of the hangman game.|
|    |iv.|The function has the parameter chosenletter, which will be updated in accordance with the button chosen. Once the button is chosen, it will disable the button from being pressed further. It then matches the letter with the word chosen, and if it matches, it will update the word, and check if the game has won. If else, it will increase the mistakes counter by 1, update the cartoon, and check if the game has ended. 
|**3d.**|i.|In the program, we can choose the answer to be cat-in-the-hat. In which, the two calls can be -, and z.|
|    |ii.|First we can check the -. The program checks if - is used in the word, which it is. It would then update every instance of - in the guessed word to appear.<br/>Z is then checked in the word and since it does not show up, it will update the mistakes counter and the cartoon.|
|    |iii.|The result of - being checked, is that it will update the word to include - and check if the game has won. The result of z being checked is that it will update the mistakes counter, the cartoon drawing, then check if the maximum mistakes have been approached, which will then end the game.|




