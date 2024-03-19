from pint import UnitRegistry, Unit

UNIT_REGISTRY = UnitRegistry()

# Initialize custom units
UNIT_REGISTRY.define("solar_luminosity = 3.828e+26 * watt = L☉")
UNIT_REGISTRY.define("solar_mass = 1.989e+30 * kilogram = M☉")
UNIT_REGISTRY.define("solar_radius = 6.957e+8 * meter = R☉")
UNIT_REGISTRY.define("metallicity = [] = [Fe/H]")

# Expose custom units so they can be imported and used easily
SOLAR_LUMINOSITY: Unit = UNIT_REGISTRY.solar_luminosity #type: ignore
SOLAR_MASS:       Unit = UNIT_REGISTRY.solar_mass       #type: ignore
SOLAR_RADIUS:     Unit = UNIT_REGISTRY.solar_radius     #type: ignore
METALLICITY:      Unit = UNIT_REGISTRY.metallicity      #type: ignore
KM_PER_SEC:       Unit = UNIT_REGISTRY.kilometer / UNIT_REGISTRY.second