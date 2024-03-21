import numpy as np
import random
from typing import Any
from astro_generator.utils.validator import validate_list_type, validate_of_type, validate_of_types

class RandomSelector():
    def select(self) -> Any:
        return
    
    def get_values(self) -> list:
        return []
    
    def get_value_count(self) -> int:
        return 0
    
class WeightedSelector(RandomSelector):
    def __init__(self, weights: list, values: list, select_count: int) -> None:
        """
        Will select values according to given weights.
        The higher the weight of a value, the higher it's chance to be selected.
        Weights do not have to sum up to 1.

        Args:
            weights (list): All weights for the given values.
            values (list): Values the selector will choose from.
            select_count (int): The amount of values that are supposed to be generated per select().

        Raises:
            ValueError: On invalid input.
        """
        validate_of_type(weights, list, "weights")
        validate_of_type(values, list, "values")
        validate_of_type(select_count, int, "select_count")
        if len(weights) != len(values):
            raise ValueError("There have to be the same amount of weights as values.")
        try:
            total = sum(weights)
        except Exception:
            raise ValueError("The given weights are invalid, make sure they are numbers.")

        self.probabilities = [weight / total for weight in weights]
        self.values = values
        self.select_count = select_count

    @staticmethod
    def from_dict(data: dict) -> 'WeightedSelector':
        """Will create a WeightedSelector instance from a dictionary

        Args:
            data (dict): Dictionary the selector is to be created from. 
                         Example: {"weights": [10, 50], "values": [1, 2], "count": 1}

        Returns:
            WeightedSelector: A WeightedSelector instance
        """
        weights = data.get("weights", None)
        values = data.get("values", None)
        select_count = data.get("count", 1)

        return WeightedSelector(weights=weights, values=values, select_count=select_count)

    def select(self) -> Any:
        """Will select a random value according to the specified weights.

        Returns:
            Any: The random generated value
        """
        value = np.random.choice(self.values, size=self.select_count, replace=False, p=self.probabilities)
        if self.select_count == 1 and len(value) > 0:
            return value[0]
        return value
    
    def get_values(self) -> list:
        """Will return all values this selector can generate.

        Returns:
            list: A list of all possible values.
        """
        return self.values
    
    def get_value_count(self) -> int:
        """Will return the amount of values the selector generates.

        Returns:
            int: Amount of values the selector returns on select().
        """
        return self.select_count
    
class MinMaxSelector(RandomSelector):
    def __init__(self, minimum: float|int, maximum: float|int, select_count: int) -> None:
        """
        Will select float values between two given numbers.

        Args:
            minimum (float): The minimum generated value.
            maximum (float): The maximum generated value.
            select_count (int): The amount of values that are supposed to be generated per select().

        Raises:
            ValueError: On invalid input.
        """
        validate_of_types(minimum, [float, int], "minimum")
        validate_of_types(maximum, [float, int], "maximum")
        validate_of_type(select_count, int, "select_count")

        if minimum > maximum:
            raise ValueError("The maximum has to be greater than the minimum.")
        
        if isinstance(minimum, int) and isinstance(maximum, int):
            self.mode = "int"
        else:
            self.mode = "float"
        self.minimum = minimum
        self.maximum = maximum
        self.select_count = select_count

    @staticmethod
    def from_dict(data: dict) -> 'MinMaxSelector':
        """Will create a MinMaxSelector instance from a dictionary

        Args:
            data (dict): Dictionary the selector is to be created from. 
                         Example: {"min": 1, "max": 3, "count": 1}

        Returns:
            MinMaxSelector: A MinMaxSelector instance
        """
        minimum = data.get("min", None)
        maximum = data.get("max", None)
        select_count = data.get("count", 1)

        return MinMaxSelector(minimum=minimum, maximum=maximum, select_count=select_count)

    def select(self) -> float:
        """Will select a random value between the specified min and max.

        Returns:
            float: The random generated value
        """
        if self.mode == "float":
            value = random.uniform(self.minimum, self.maximum)
        else:
            value = random.randint(self.minimum, self.maximum) # type: ignore
        return value
    
    def get_values(self) -> list:
        """Will return all values this selector can generate.

        Returns:
            list: A list of all possible values.
        """
        return [self.minimum, self.maximum]
    
    def get_value_count(self) -> int:
        """Will return the amount of values the selector generates.

        Returns:
            int: Amount of values the selector returns on select().
        """
        return self.select_count

class Probability():
    def __init__(self, selector: RandomSelector) -> None:
        """
        An interface for different types of random generated values.
        Can be created from any given data via Probability.create().
        Data must abide by input scheme of any available RandomSelector.

        Args:
            selector (RandomSelector): The random selector this probability uses to generate values.
        """
        self.selector = selector

    @staticmethod
    def create(data: Any) -> 'Probability':
        """
        Will create a Probability instance from any given data.
        Data must abide by input scheme of any available RandomSelector.

        Args:
            data (Any): The data that the RandomSelector is created from.

        Raises:
            ValueError: On invalid input data.

        Returns:
            Probability: On successful creation, a proper Probability object is returned.
        """
        selector = None

        try:
            if isinstance(data, dict):
                if "weights" in data and "values" in data:
                    selector = WeightedSelector.from_dict(data=data)
                elif "min" in data and "max" in data:
                    selector = MinMaxSelector.from_dict(data=data)
        except Exception as e:
            raise ValueError(f"An error occured while creating Probability: {e}")
        if not isinstance(selector, RandomSelector):
            raise ValueError(f"Given data did not match any available selectors.")
        
        return Probability(selector=selector)

    def generate(self) -> Any:
        """Generates a random value according to the random selector the Probability was created for.

        Returns:
            Any: The randomly generated value.
        """
        return self.selector.select()
    
    def validate(self, required_type: type, count: int, name: str) -> None:
        """Will validate the Probability object for a certain desired output.

        Args:
            required_type (type): The output type all generated values must have.
            count (int): The amount of values the generator is supposed to output.
            name (str): The name of the Probability.

        Raises:
            ValueError: Should the Probability not abide by the specified parameters.
        """
        selector_count = self.selector.get_value_count()
        if selector_count != count:
            raise ValueError(f"Probability for '{name}' has to return {count} values, but it returns {selector_count}.")
        selector_values = self.selector.get_values()
        for value in selector_values:
            if not isinstance(value, required_type):
                raise ValueError(f"All values for Probability '{name}' have to be of type {required_type.__name__}")
            
class ProbabilityGroup():
    def __init__(self, probabilities: dict[str, Probability]) -> None:
        """A class for grouping different Probabilities with the same output scheme.

        Args:
            probabilities (dict[str, Probability]): A dictionary of available probabilities.

        Raises:
            ValueError: On invalid input.
        """
        self.probabilities = probabilities
        try:
            validate_of_type(probabilities, dict, "probabilities")
            validate_list_type(list(probabilities.keys()), str, "probabilities", "probability keys")
            validate_list_type(list(probabilities.values()), Probability, "probabilities", "probability values")
        except Exception as e:
            raise ValueError(f"An error occured while creating ProbabilityGroup: {e}")
        
    def generate(self, key: str, default: Any = None) -> Any:
        """Generates a random value according to the random selector the Probability of the given key was created for.

        Args:
            key (str): The key of the Probability object that is supposed to be used for generation.

        Returns:
            Any: A random generated value from the given key.
        """
        if key not in self.probabilities:
            return default
        probability: Probability = self.probabilities.get(key) # type: ignore
        return probability.generate()
    
    def validate(self, required_type: type, count: int, name: str) -> None:
        """Will validate the ProbabilityGroup object for a certain desired output.

        Args:
            required_type (type): The output type all generated values must have.
            count (int): The amount of values the generator is supposed to output.
            name (str): The name of the Probabilities.

        Raises:
            ValueError: Should one Probability in the ProbabilityGroup not abide by the specified parameters.
        """
        current_key = None
        try:
            for key, probability in self.probabilities.items():
                current_key = key
                probability.validate(required_type=required_type, count=count, name=name)
        except Exception as e:
            raise ValueError(f"An error occured in key '{current_key}' while creating ProbabilityGroup: {e}")