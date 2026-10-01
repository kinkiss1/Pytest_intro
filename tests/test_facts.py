from unittest.mock import Mock

import pytest

from study_project.facts import get_cat_fact, FACTS_URL


def test_cat_fact_response():
    http_client = Mock()
    response = Mock()
    response.json.return_value = {"fact": "Cats sleep a lot."}
    http_client.get.return_value = response
    result = get_cat_fact(http_client)
    assert result == "Cats sleep a lot."
    http_client.get.assert_called_once_with(
        FACTS_URL,
        timeout=5
    )
    response.raise_for_status.assert_called_once()
    response.json.assert_called_once_with()


def test_cat_fact_network():
    http_client = Mock()
    http_client.get.side_effect = ConnectionError('Unlucky')
    with pytest.raises(ConnectionError):
        get_cat_fact(http_client)
    http_client.get.assert_called_once_with(
        FACTS_URL,
        timeout=5
    )


def test_cat_fact_exception():
    http_client = Mock()
    response = Mock()
    response.json.return_value = {"length": 20}
    http_client.get.return_value = response
    with pytest.raises(KeyError, match='fact'):
        get_cat_fact(http_client)
    response.raise_for_status.assert_called_once_with()
    response.json.assert_called_once_with()
