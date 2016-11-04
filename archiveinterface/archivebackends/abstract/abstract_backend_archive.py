"""Module that has the Abstract class for Archive Backends
Any new backends need to inherit from this class and implement
its methods. If the methods are not implemented in the child,
the child object will not be able to be instantiated
"""

import abc

class AbstractBackendArchive(object):
    """Abstract Base Class for Archive Backends"""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def __init__(self, prefix, user, auth):
        pass

    @abc.abstractmethod
    def open(self, filepath, mode):
        """Method that opens a file for the backend archive that implements
        this class Should return a file like object, most likely self
        """
        pass

    @abc.abstractmethod
    def close(self):
        """Method that closes an open file for the backend archive that
        implements this class"""
        pass

    @abc.abstractmethod
    def read(self, blocksize):
        """Method that reads an open file for the backend archive that
        implements this class and returns the contents"""
        pass

    @abc.abstractmethod
    def write(self, buf):
        """Method that writes an open file for the backend archive that
        implements this class"""
        pass

    @abc.abstractmethod
    def stage(self):
        """Method that stages a file for the the backend that implements
        this class Stage moves a file to an appropriate location to be
        downloaded"""
        pass

    @abc.abstractmethod
    def status(self):
        """Method that gets the status of a file in the archive
        Needs to return an implemented object of the abstract_status_class
        The abstract_status_class should be implemented for each backend type"""
        pass

    @abc.abstractmethod
    def set_mod_time(self, mod_time):
        """Method that sets a files mod time for the backend archive that
        implements this class"""
        pass