class Borg(object):
    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state


class YourBorg(Borg):
    def __init__(self, state=None):
        super().__init__()
        if state:
            self.state = state
        else:
            # initiate the first instance with default state
            if not hasattr(self, "state"):
                self.state = "Init"

    def __str__(self):
        return self.state


if __name__ == "__main__":
    rm1 = YourBorg()
    rm2 = YourBorg()
    rm1.state = "Idle"
    rm2.state = "Running"
    print("rm1: {0}".format(rm1))
    print("rm1: {0}".format(rm2))
    rm2.state = "Zombie"
    print("rm1: {0}".format(rm1))
    print("rm2: {0}".format(rm2))
    print(rm1 is rm2)
