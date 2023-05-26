class Carrot:
    states = {0: 'Empty', 1: 'Sapling', 2: 'Green', 3: 'Done'}

    def __init__(self, index):
        self.index = index
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    def is_ripe(self):
        if self.state == 3:
            return True
        return False

    def print_state(self):
        print('Carrot {} now is {}'.format(
            self.index, Carrot.states[self.state]
        ))


class CarrotFarm:

    def __init__(self, count):
        self.carrots = [Carrot(index) for index in range(1, count + 1)]

    def grow_all(self):
        print('Carrot is growing')
        for i_carrot in self.carrots:
            i_carrot.grow()

    def are_all_ripe(self):
        if not all([i_carrot.is_ripe() for i_carrot in self.carrots]):
            print('The Carrot is not ready yet\n')
        else:
            print('All the carrots are ready. You can harvest them.')


my_garden = CarrotFarm(5)
for _ in range(3):
    my_garden.grow_all()
    my_garden.are_all_ripe()