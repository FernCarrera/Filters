import copy
import inspect
import numpy as np  
from collections import defaultdict
#based on Roger Labbe's class MIT license


class Saver(object):

    ''' Class to save the states of filter object
        appends all states, covariances to lists

        Parameters
    ----------
    kf : object
        any object with a __dict__ attribute, but intended to be one of the
        filtering classes
    save_current : bool, default=False
        save the current state of `kf` when the object is created;
    skip_private: bool, default=False
        Control skipping any private attribute (anything starting with '_')
        Turning this on saves memory, but slows down execution a bit.
    skip_callable: bool, default=False
        Control skipping any attribute which is a method. Turning this on
        saves memory, but slows down execution a bit.
    ignore: (str,) tuple of strings
        list of keys to ignore.
     '''



    def __init__(self,kf,save_current=False,
                skip_private=False,
                skip_callable=False,
                ignore=()):


        self._kf = kf
        self._DL = defaultdict(list)
        self._skip_private = skip_private
        self._skip_callalbe = skip_callable
        self._ignore = ignore
        self._len = 0


        self.properties = inspect.getmembers(
            type(kf),lambda o: isinstance(o,property)
        )

        if save_current:
            self.save()


    def save(self):
        '''save current state of the filter'''

        kf = self._kf

        # force attributes to be computed
        # necessary if the class uses properties
        # that are only calcualted when accessed

        for prop in self.properties:
            self._DL[prop[0]].append(getattr(kf,prop[0]))