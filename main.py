"""
main loop outline:

- initialize "world" constants
    - initialize objects
- connect inputs (lets start with predefined from a function)
- boundary condition = world + objects
- for i in timestep:
    - solve object for i in objects (incl world interactions, input response)
    - update world and objects
    - log data/output frame

"""