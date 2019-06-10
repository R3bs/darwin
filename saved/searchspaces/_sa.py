
from .searchspace import searchspace
from darwin.engine.opt import agtfactory as agtfct

class sa(searchspace):

    def __init__(self, m, n, initial_temperature=None, final_temperature=None, cooling_schedule=None):

        # call super from searchspace base class
        super().__init__(m, n)

        for i in range(m):
            self._a.append(agtfct.create_agent('sa', n))

        if initial_temperature == None:
            print('error: SA searchspace requires a "initial_temperature" be set')
            sys.exit(1)

        if final_temperature == None:
            print('error: SA searchspace requires a "final_temperature" be set')
            sys.exit(1)

        if cooling_schedule == None:
            print('error: SA searchspace requires a "cooling_schedule" be set')
            sys.exit(1)

        self._cooling_schedule_id = cooling_schedule # identification number of the cooling schedule used on SA
        self._init_temperature = initial_temperature # Initial temp. If  0 (zero) or any below, determine it automatically from the number of iterations.
        self._end_temperature = final_temperature # temperature that means the convergence of the algorithm (Generally = 1)
        self._func_param = 0.0 # extra parameter for the cooling schedule functions

    def show(self):

        # call super to show basic data
        super.show()

        for i in range(self._m):

            print('Agent {} -> '.format(i), end='')
            for j in range(self._n):
                fit = self._a[i].x[j]
                print('x[{}]: {}   '.format(j, fit), end='')

            print('Boundaries')
            for j in range(self._n):
                fit = self._a[i].x[j]
                UB = 0
                LB = 0
                print('UB[{}]: {}, LB[{}]: {} '.format(j, UB, j, LB), end='')

            print('fitness value: {}'.format(self._a[i].fit))

    def evaluate(self, func, args):

        for i in range(self.m):

            self.a[i].evaluate(args)

    def check(self):

        if not isinstance(self._end_temperature, float):
            print(' -> end temperature undefined')
            return 1
        else:
            return 0