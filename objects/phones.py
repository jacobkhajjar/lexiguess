class Phone:
    def __init__(self, glyphs: str):
        self.glyphs = glyphs

    def __str__(self):
        return self.glyphs
    
    def __repr__(self):
        return self.glyphs