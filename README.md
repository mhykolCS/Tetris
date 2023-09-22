# tetris

Contents of Program: 
main.py [5 lines] <- The runtime of the program, an easy way to begin and run the program.
startup_surface.py [69 lines] <- This is the first function call of the program and contains the initial bootup screen with options to go between different menus.
configure_surface.py [55 lines] <- This file contains the configuration surface/screen for the program, all user options are selected here.
topscore_surface.py [44 lines] <- This file contains a list of all top scorers of the video game. Consider this screen a display of saved data.
setting.py [38 lines] <- Global constant variables that change the way the program is run on the backend, such as screen size, fps, window title, etc.
pgfunctions.py [9 lines] <- This file contains a list of regularly used functions throughout the program, such as createRect and drawText()
game_surface.py [193 lines] <- This is the main game screen, all gameplay happens in this file.
class_objects [25 lines] <- Thile file holds objects that are present in all of the files seen above. This ranges from buttons, audio, text, etc.

All variables, methods, classes and objects should use lowercase snake_case
All function calls should use lowercase snake_case
All constant variables should be CAPITILIZED

