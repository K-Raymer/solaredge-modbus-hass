"""Constants For Modbus Server/Client.

This is the single location for storing default
values for the servers and clients.
"""
import enum


INTERNAL_ERROR = "Pymodbus internal error"


class Endian(str, enum.Enum):
    """An enumeration representing the various byte endianness.

    .. attribute:: AUTO

       This indicates that the byte order is chosen by the
       current native environment.

    .. attribute:: BIG

       This indicates that the bytes are in big endian format

    .. attribute:: LITTLE

       This indicates that the bytes are in little endian format

    .. note:: I am simply borrowing the format strings from the
       python struct module for my convenience.
    """

    AUTO = "@"
    BIG = ">"
    LITTLE = "<"
