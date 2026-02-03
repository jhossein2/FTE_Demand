import unittest

class TestRegressionForecast(unittest.TestCase):

    def setUp(self):
        # Setup code to initialize any data required for the tests
        self.forecast_data = self.get_forecast_data()
        self.baseline_data = self.get_baseline_data()

    def get_forecast_data(self):
        # Code to get the forecast data from the forecast model
        # This will depend on how your forecasting function is implemented
        # Example: return forecast_model.calculate_forecast() 
        pass

    def get_baseline_data(self):
        # Code to get baseline data for comparison
        pass

    def test_row_count(self):
        expected_row_count = len(self.baseline_data)
        actual_row_count = len(self.forecast_data)
        self.assertEqual(expected_row_count, actual_row_count, "Row counts do not match!")

    def test_month_labels(self):
        expected_months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        actual_months = [item['month_label'] for item in self.forecast_data]
        self.assertEqual(actual_months, expected_months, "Month labels do not match!")

    def test_demand_values(self):
        baseline_demand_values = [item['demand'] for item in self.baseline_data]
        forecast_demand_values = [item['demand'] for item in self.forecast_data]
        self.assertEqual(forecast_demand_values, baseline_demand_values, "Demand values do not match!")

if __name__ == '__main__':
    unittest.main()