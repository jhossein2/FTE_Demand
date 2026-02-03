import unittest

class TestRegressionForecast(unittest.TestCase):
    def setUp(self):
        # Set up baseline values and forecast mode output
        self.baseline_values = [100, 200, 300]  # Example baseline values
        self.forecast_values = [95, 205, 310]    # Example forecast values

    def test_forecast_accuracy(self):
        for baseline, forecast in zip(self.baseline_values, self.forecast_values):
            self.assertAlmostEqual(baseline, forecast, delta=10, msg="Forecast output deviates from baseline.")

if __name__ == '__main__':
    unittest.main()