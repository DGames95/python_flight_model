"""
Takes an object and applies rk4 to the timestep

plan interaction with an __solve__ method per object 
that tells this function how to deal with it

imagined solver loop aircraft:

- get current data and data for previous steps needed
- setup equations and calculate
    - gravity (physics engine)
    - solve forces on aircraft
        - 1. determine lift distribution
        - calculate stress on wing
        - solve for force at base of wing
        - update control surface based on input
        - update force from control surfaces
        - 
    
- update new values

"""