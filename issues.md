# Encountered Problems

**NOTE:** Not all issuse were dealt with via issue tickets on GitHub, most were discussed via ```Discord```.
If there was a problem the Discord group would be messaged and we would resolve it through clear communication.  

* First problem encountered was figuring out the logic for hiding widget windows. At first two blank windows were used to test.
Eventually, after watching YouTube tutorials and reading Stackoverflow it was discovered that lambda functions can be used to set the state of a given widget.
A function was written to act as a boolean value for the window, hide or show. Upon click of a button that state can be turned on or off.


* Second problem encountered was getting the individual Rec Math windows to be combined into the main window.
It was decided that each Rec Math Generator would be written separately and then would be added into the main window after we knew the individual generator worked.
The second blank window was used a test for the Prime Number Generator (PNG). The second window code was replaced by the PNG
This worked pretty well, the PNG showed up on click of the PNG button on the main window.

  * An issues occurred while adding the PNG to the main window. Upon pressing 'reset' the app would crash.
  This was fixed by adding a positional argument ```'self'``` to ```reset_action()```. Also the definition of
  ``reset_action()`` was updated to include ``self.listWidget.clear()`` to empty the output box and 
  ```entry_box.clear()``` to clear the entry box.


* Third issue encountered was incorporating the Automorphic Number Generator (ANG). At first we thought it could be added just like the PNG, unfortunately that was not the case.
A class was written for the Generator and the Controls for the generator. The logic for the window hiding only looks at one class, so
it would show the window for the ANG but you could not use any of the widgets. It was decided that the Controls class would be added into the Generator class.
This fixed the problem instantly the ANG can now be used when its button is clicked on the main window.


### Minor issues encountered:
* text being cut off on screen, fixed by implementation of an update function which resized the text.
* testing with QtDesigner seemed more problematic than helpful.
* reset button PNG crashes the application, no fix has been made yet