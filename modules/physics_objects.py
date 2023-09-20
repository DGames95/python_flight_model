"""
objects need mass, moment of intertia(x,y,z), velocity (x,y,z) and rotational velocity (x,y,z)

there is a pyhsics engine here basically required

aircrafts have:
    lift coefficient (determined by aero model)
    input parameters (throttle setting, yoke, rudder vlaue), 
    input responses (function of input parameters, may be determined by aero model)
    reaction with ground
    structure model (influences aero model?, defines load limits)

deal with: coordinate reference frames aircraft centered, earth centered etc.

"""

class Body():
    """
    has attributes: mass, 3 axis moment of intertia
    """
    def __init__(self, mass: float,
                 position: tuple,
                 velocity: tuple,
                 rotational_velocity: tuple,
                 rotational_inertia: tuple) -> None:
        
        self.mass = mass
        self.position = position
        self.velocity = velocity
        self.rotational_velocity = rotational_velocity
        self.rotational_intertia = rotational_inertia


class FixedWingAircraft():
    """_summary_
    
    Provides class for aircraft, inherits from Body Class
    
    attributes: lift coefficient, 
    
    methods: __solve__:  defines interaction with the solver
    
    """
    pass