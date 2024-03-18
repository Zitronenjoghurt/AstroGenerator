class AstroGeneratorError(Exception):
    """Base exception class for astro generator errors."""
    pass

class InvalidUnitError(AstroGeneratorError):
    """This exception is thrown when a wrong pint unit is provided somewhere."""
    def __init__(self, expected_dimensionality: str, received_dimensionality: str, value_name: str, hint_unit: str) -> None:
        """Create an exception for an invalid provided unit.

        Args:
            expected_unit (str): The unit that was expected.
            received_unit (str): The unit that was provided.
            context (str): Explaining the context the error was thrown in.
        """
        full_message = f"Invalid unit for {value_name}: expected a unit of dimensionality {expected_dimensionality}, but got {received_dimensionality}.\nTry to define the value for {value_name} like: 1.5 * {hint_unit}, dont forget to import {hint_unit} from astro_generator.\nYou can also use units which are compatible from the UNIT_REGISTRY, example for mass: 1 * UNIT_REGISTRY.kilogram (import UNIT_REGISTRY from astro_generator)."
        super().__init__(full_message)