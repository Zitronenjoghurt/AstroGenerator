from typing import Any
from pint import Quantity, Unit
from astro_generator.exceptions import InvalidUnitError

def validate_unit(quantity: Quantity, unit, value_name: str, hint_unit: str) -> None:
    if not isinstance(unit, Unit):
        raise InvalidUnitError(expected_dimensionality="None", received_dimensionality="None", value_name=value_name, hint_unit=hint_unit)
    if not isinstance(quantity, Quantity):
        raise InvalidUnitError(expected_dimensionality=str(unit.dimensionality), received_dimensionality="None", value_name=value_name, hint_unit=hint_unit)
    if not quantity.dimensionality == unit.dimensionality:
        raise InvalidUnitError(expected_dimensionality=str(unit.dimensionality), received_dimensionality=str(quantity.dimensionality), value_name=value_name, hint_unit=hint_unit)
    
def validate_of_type(value: Any, required_type: type, value_name: str = "value"):
    if not isinstance(value, required_type):
        raise ValueError(f"{value_name} must be of type {required_type.__name__}")
    
def validate_of_types(value: Any, required_type: list[type], value_name: str = "value"):
    if not isinstance(value, tuple(required_type)):
        type_names = [type.__name__ for type in required_type]
        raise ValueError(f"{value_name} must be one of these types: {', '.join(type_names)}")
    
def validate_list_type(data_list: list, required_type: type, list_name: str, value_name: str):
    validate_of_type(value=data_list, required_type=list, value_name=list_name)
    for value in data_list:
        if not isinstance(value, required_type):
            raise ValueError(f"All {value_name} in {list_name} must be of type {required_type.__name__}")