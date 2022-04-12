class Application:
    def parent(self, money: int = None):
        print('call parent')
        res = self.child(money)
        if not isinstance(res, int):
            raise Exception('child return not int')
        return f'So parent has {res} $'

    def child(self, money: int = None):
        print('call child')
        print(f'child has {money} $ lucky money')
        return money
