
TYPELIST = {}
DRIVERLIST = {}
RESERVEDATTRS = {}

class ClustoDriver(type):
    """
    Metaclass for all clusto drivers
    """
    def __init__(cls, name, bases, dct):

        if not hasattr(cls, '_driverName'):
            raise DriverException("Driver %s missing _driverName attribute"
                                  % cls.__name__)

        if cls._driverName in DRIVERLIST:
            raise KeyError("class '%s' is trying to add the driverName '%s' "
                           "to the driver list but that name is already "
                           "claimed by the '%s' class."
                           % (cls.__name__,
                              cls._driverName,
                              DRIVERLIST[cls._driverName].__name__))
        

        DRIVERLIST[cls._driverName] = cls
        TYPELIST[cls._clustoType] = cls

        # setup properties
        if not isinstance(cls._properties, dict):
            raise TypeError('_properties of %s is not a dict type.',
                            cls.__name__)
        

        super(ClustoDriver, cls).__init__(name, bases, dct)

