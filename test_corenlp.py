from unittest.mock import patch
import pytest
import textblob

from nlplogic.corenlp import (
    search_wikipedia,
    summarize_wikipedia,
    get_text_blob,
    get_phrases,
)


def test_search_wikipedia():
    # define what the mock should return
    mock_return_value = ["Python (programming language)", "Pythonidae", "Monty Python"]

    # mock wikipedia.search
    with patch("wikipedia.search", return_value=mock_return_value) as mock_search:
        # call the fucntion being tested
        result = search_wikipedia("Python")

        # Assertion
        mock_search.assert_called_once_with(
            "Python"
        )  # Ensure it was called with the expected argument
        assert result == mock_return_value  # Ensure the return value is as expected


def test_summarize_wikipedia():
    mock_return_value = "A face book or facebook is a paper or online directory of individuals' photographs and names published by some American universities. In particular, the term denotes publications of this type distributed by university administrations at the start of the academic year, with the intention of helping students to get to know each other."

    with patch("wikipedia.summary", return_value=mock_return_value) as mock_summary:
        result = summarize_wikipedia("Facebook", 2)

        mock_summary.assert_called_once_with(
            "Facebook", sentences=2
        )  # need to be called with the same arguments as the mocking fuction
        assert result == mock_return_value


def test_summarize_wikipedia_string_lenght():
    with pytest.raises(KeyError):
        summarize_wikipedia("Facebook", "abc")


def test_get_text_blob():
    input_text = "This is a sample text"
    result = get_text_blob(input_text)

    assert type(result) == textblob.blob.TextBlob


def test_get_phrases():
    with pytest.raises(KeyError):
        get_phrases("Facebook", "abc")


def test_get_phrases_1():
    mock_return_value = "Donald"

    with patch("wikipedia.summary", return_value=mock_return_value) as mock_summary:
        result = get_phrases("Facebook", 2)

        mock_summary.assert_called_once_with("Facebook", sentences=2)
        assert result == ["donald"]  # the noun phrase of "Donald"
