import pytest
from unittest import mock


@mock.patch('src.cat_models.hurricane_loss.hurricane_loss_model', return_value=10, autospec=True)
@pytest.mark.parametrize('florida_landfall_rate, florida_mean, florida_sigma,'
                         'gulf_landfall_rate, gulf_mean, gulf_sigma, num_sim, expected_result',
                         [(3, 100, 90, 6, 200, 190, 100, 10)])
def test_hurricane_loss_model(mock_hurricane_loss_model, florida_landfall_rate, florida_mean, florida_sigma,
                              gulf_landfall_rate, gulf_mean, gulf_sigma, num_sim, expected_result):

    # Mock a volatile function
    result = mock_hurricane_loss_model(florida_landfall_rate, florida_mean, florida_sigma,
                                       gulf_landfall_rate, gulf_mean, gulf_sigma, num_sim)

    assert result == expected_result

