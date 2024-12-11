from carta import ReMarkable


class reMarkable(ReMarkable):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.view = None
        
    
    def update_view(self, view):
        self.view = view
        self.view.display()
    