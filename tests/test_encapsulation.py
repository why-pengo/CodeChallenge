from challenge.ProcessText import ProcessText
import pytest


def test_encapsulated_getter():
    pt = ProcessText("Now is the time for all good people")
    assert len(pt.get_words()) == 8


def test_encapsulated_private():
    pt = ProcessText("Now is the time for all good people")
    with pytest.raises(AttributeError):
        pt.__words
