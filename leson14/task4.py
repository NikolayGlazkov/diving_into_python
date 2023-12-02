from task2 import clear_text
import pytest



def test_non_change():
    assert "this is a sample" == clear_text("this is a sample"), "FAIL"


def test_register():
    assert "this is a sample" == clear_text("This is a sample"), "FAIL"


def test_punctuation():
    assert "this is a sample" == clear_text("this is a sample,"), "FAIL"


def test_another_alph():
    assert "this is a sample " == clear_text("this is a sample вапвап"), "FAIL"


def test_all():
    assert "this is a sample  " == clear_text("This is a Sample, - вапвап"), "FAIL"


if __name__ == '__main__':
    pytest.main(['-sv'])