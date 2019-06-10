
import abc

class mediator(abc.ABC):

    def __init__(self, kwargs):

        # get the kwargs dict
        self._kwargs = kwargs

    @abc.abstractmethod
    def execute(self, m, n, func, maps, max_itr):
        pass


