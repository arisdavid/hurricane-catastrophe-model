import pytest
from src.cat_models.hurricane_loss import hurricane_loss_model


@pytest.mark.parametrize('florida_landfall_rate, florida_mean, florida_sigma,'
                         'gulf_landfall_rate, gulf_mean, gulf_sigma, num_sim, expected_result',
                         [(0.4, 0.5, 0.28, 0.6, 0.8, 0.33, 1, 0.5)])
def test_hurricane_loss_model(florida_landfall_rate, florida_mean, florida_sigma,
                              gulf_landfall_rate, gulf_mean, gulf_sigma, num_sim, expected_result):

    result = hurricane_loss_model(florida_landfall_rate, florida_mean, florida_sigma,
                                  gulf_landfall_rate, gulf_mean, gulf_sigma, num_sim)

    assert result == expected_result
