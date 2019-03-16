from multiprocessing import Queue
from sorter import Sorter

#Dispatcher
# @purpose - an object manager that maintains a record of serveral Sorters. Using the dispatch() method
#  a zip archive will be sent to a Sorter for extraction, sorting, and re-zipping.
class Dispatcher:

    #max_sorters - maximum number of sorters allowed at a time
    #running_sorters - current number of running sorters
    #sorters - the list of sorters
    #result_queue - queue for the resulting zip archives which sorters creates
    #waiting_queue - queue for zip archives that are currently waiting to be sorted

    def __init__(self):
        self._max_sorters = 5
        self._running_sorters = 0
        self._sorters = []
        self._result_queue = Queue()
        self._waiting_queue = Queue()

    def dispatch(self, archive_name):

        if self._running_sorters == self._max_sorters:
            print('no more sorters available')
            self._waiting_queue.put(archive_name)
        else:
            self._sorters.append(Sorter(self._result_queue, archive_name))
            self._sorters[self._running_sorters].start()
            self._running_sorters = self._running_sorters + 1