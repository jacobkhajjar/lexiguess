class Phone:
    def __init__(self, fx: str):
        self.fx = fx

    def __str__(self):
        return self.fx
    
    def __repr__(self):
        return self.fx