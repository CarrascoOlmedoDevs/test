class ResultFragmentSimulation:
    """
    Simulates a Kotlin ResultFragment for displaying nutrition data.
    Data can be set via a method, mimicking arguments or ViewModel data.
    """

    def __init__(self):
        """Initializes the fragment simulation with no data."""
        self._nutrition_data = None

    def set_nutrition_data(self, data):
        """
        Sets the nutrition data for the fragment.
        This simulates receiving data via arguments or from a ViewModel.

        Args:
            data (dict): A dictionary containing nutrition information
                         (e.g., {"calories": 300, "protein_g": 20, ...}).
        """
        if isinstance(data, dict):
            self._nutrition_data = data
            print("Nutrition data received and set.")
        else:
            print("Error: Data must be a dictionary.")
            self._nutrition_data = None # Ensure data is cleared if invalid

    def display_data(self):
        """
        Simulates displaying the nutrition data in the fragment's UI.
        """
        print("\n--- Result Fragment Display ---")
        if self._nutrition_data:
            print("Displaying Nutrition Information:")
            for key, value in self._nutrition_data.items():
                print(f"- {key.replace('_', ' ').capitalize()}: {value}")
        else:
            print("No nutrition data available to display.")
        print("-------------------------------")

# --- Example Usage ---
if __name__ == "__main__":
    # Create an instance of the simulated fragment
    result_fragment = ResultFragmentSimulation()

    # Simulate receiving data
    sample_nutrition = {
        "calories": 450,
        "protein_g": 30,
        "carbs_g": 55,
        "fat_g": 15,
        "fiber_g": 5,
        "sugar_g": 10
    }

    print("Setting nutrition data...")
    result_fragment.set_nutrition_data(sample_nutrition)

    # Simulate displaying the data
    print("\nAttempting to display data...")
    result_fragment.display_data()

    # Simulate the case where no data is set
    print("\nCreating another fragment instance without setting data...")
    another_fragment = ResultFragmentSimulation()
    another_fragment.display_data()

    # Simulate setting invalid data
    print("\nAttempting to set invalid data...")
    result_fragment.set_nutrition_data("This is not a dict")
    result_fragment.display_data()