from typing import Any
from pint import Quantity, Unit
from astro_generator.exceptions import InvalidUnitError

def validate_unit(quantity: Quantity, unit: Unit, value_name: str, hint_unit: str) -> None:
    if not isinstance(unit, Unit):
        raise InvalidUnitError(expected_dimensionality="None", received_dimensionality="None", value_name=value_name, hint_unit=hint_unit)
    if not isinstance(quantity, Quantity):
        raise InvalidUnitError(expected_dimensionality=str(unit.dimensionality), received_dimensionality="None", value_name=value_name, hint_unit=hint_unit)
    if not quantity.dimensionality == unit.dimensionality:
        raise InvalidUnitError(expected_dimensionality=str(unit.dimensionality), received_dimensionality=str(quantity.dimensionality), value_name=value_name, hint_unit=hint_unit)
    
def validate_of_type(value: Any, required_type: type, value_name: str = "value"):
    if not isinstance(value, required_type):
        raise ValueError(f"{value_name} must be of type {required_type.__name__}")