# pygame-framework
Class-based pygame framework for simplified view-switching. 

The framework is a module, so you may run it by typing `$ python -m game` in the terminal (in this directory). The `game` folder is pre-loaded with some example code to highlight certain capabilities.

- View switching (`TitleView`, `PlayView`, `PauseView`)
- Pause screens retaining original game (`PlayView`) state and returning control back to the game.
- Passing info between views (`PauseView` quitting to `TitleView` sends the most recent score)
- Accessing world boundary within views (to make the ball bounce off the sides of the screen in the `PlayView`)

## Modification
You may remove the play, title, and pause screen files to make your own, or simply modify them in place.

You may also use the `template_view.py` file as a template for your new views.

## Testing
You may add tests following the example in `tests/test_example.py`. Make sure you import from the game module as is shown. All you need to do to run the tests is type `$ pytest` in the terminal from the project root directory.

