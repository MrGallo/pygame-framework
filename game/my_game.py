from game.base_game import BaseGame


class MyGame(BaseGame):
    def create(self):
        from game.title_view import TitleView
        MyGame.set_current_view(TitleView())
