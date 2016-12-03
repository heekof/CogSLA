from Data import SLO


class SLA:

    SLO = None

    def __init__(self, slo=None):
        if SLO:
            self.SLO = slo
        else:
            self.SLO = None


class Service:

    SLA = None
    Description = None

    def __init__(self, sla=None, description=""):
        if SLA:
            self.SLA = sla
            self.Description = description
        else:
            self.Description = description
