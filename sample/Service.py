from Data import SLO

# TODO Dynamic SLA

class SLA:

    SLO = None

    def __init__(self, slo=None):
        if SLO:
            self.SLO = slo
        else:
            self.SLO = None

            # Magic function call them by repr(MC)
            # Print all the necessary Info to recreate the object

    def __repr__(self):
        pass

        # Magic function call them by str(MC)
        # Print Info related to the object

    def __str__(self):
        pass

class Service:

    SLA = None
    Description = None

    def __init__(self, sla=None, description=""):
        if SLA:
            self.SLA = sla
            self.Description = description
        else:
            self.Description = description


            # Magic function call them by repr(MC)
            # Print all the necessary Info to recreate the object

    def __repr__(self):
        pass

        # Magic function call them by str(MC)
        # Print Info related to the object

    def __str__(self):
        pass