"""Unit tests for math module."""

import pytest

from our_package import math


class TestAddIntegers:
    """Tests for `add_integers()` function."""

    def test_no_args_TypeError(self):
        "No arguments passed."
        with pytest.raises(TypeError):
            math.add_integers()

    def test_str_arg_TypeError(self):
        "String argument passed."
        with pytest.raises(TypeError):
            math.add_integers(3, '4')  # type: ignore

    def test_float_arg_TypeError(self):
        "Float argument passed."
        with pytest.raises(TypeError):
            math.add_integers(3, 3.4)  # type: ignore

    def test_list_arg(self):
        "List argument passed."
        with pytest.raises(TypeError):
            math.add_integers(list(range(3)))  # type: ignore

    def test_valid_arg(self):
        "Valid argument passed."
        assert math.add_integers(3) == 3

    def test_valid_args(self):
        "Multiple valid arguments passed."
        assert math.add_integers(3, 4, 5) == 3 + 4 + 5

    def test_unpacked_list_args(self):
        "Unpacked list passed."
        assert math.add_integers(*list(range(3))) == 0 + 1 + 2
