from astro_generator.entities.star import Star
from astro_generator.utils.validator import validate_of_type, validate_list_type

class SolarSystem():
    def __init__(
        self,
        stars: list[Star],
        name: str = ""
    ) -> None:
        """A class representing properties of a solar system

        Args:
            stars (list[Star]): List of stars that belong to the solar system.
            name (str, optional): The name of the solar system. Defaults to "".

        Raises:
            ValueError: On invalid initialization values.
        """
        try:
            validate_list_type(stars, Star, "stars", "star")
            validate_of_type(name, str, "name")
        except Exception as e:
            raise ValueError(f"An error occured while initializing SolarSystem: {e}")

        self.stars = stars
        self.name = name