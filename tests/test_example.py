import pytest

from game.base_view import BaseView


def test_throws_type_error_without_overriding_base_view_methods():
    class MyView(BaseView):
        pass

    with pytest.raises(TypeError):
        MyView()


def test_ok_when_overriding_base_view_methods():
    class MyView(BaseView):
        def event_loop(self, events):
            pass

        def update(self):
            pass

        def draw(self, surface):
            pass
    
    MyView()
