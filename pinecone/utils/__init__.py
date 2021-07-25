#
# Copyright (c) 2020-2021 Pinecone Systems Inc. All right reserved.
#
from pathlib import Path

from pinecone.protos import core_pb2, vector_column_service_pb2
from . import constants
import numpy as np
import re
import lz4.frame
from typing import List

DNS_COMPATIBLE_REGEX = re.compile("^[a-z0-9]([a-z0-9]|[-])+[a-z0-9]$")


def load_numpy(proto_arr: 'core_pb2.NdArray') -> 'np.ndarray':
    """
    Load numpy array from protobuf
    :param proto_arr:
    :return:
    """
    if len(proto_arr.shape) == 0:
        return np.array([])
    if proto_arr.compressed:
        numpy_arr = np.frombuffer(lz4.frame.decompress(proto_arr.buffer), dtype=proto_arr.dtype)
    else:
        numpy_arr = np.frombuffer(proto_arr.buffer, dtype=proto_arr.dtype)
    return numpy_arr.reshape(proto_arr.shape)


def dump_numpy(np_array: 'np.ndarray', compressed: bool = False) -> 'core_pb2.NdArray':
    """
    Dump numpy array to core_pb2.NdArray
    """
    return _dump_numpy(np_array, core_pb2.NdArray(), compressed=compressed)


def dump_numpy_public(np_array: 'np.ndarray', compressed: bool = False) -> 'vector_column_service_pb2.NdArray':
    """
    Dump numpy array to vector_column_service_pb2.NdArray
    """
    return _dump_numpy(np_array, vector_column_service_pb2.NdArray(), compressed=compressed)


def _dump_numpy(np_array: 'np.ndarray', protobuf_arr, compressed: bool = False):
    protobuf_arr.dtype = str(np_array.dtype)
    protobuf_arr.shape.extend(np_array.shape)
    if compressed:
        protobuf_arr.buffer = lz4.frame.compress(np_array.tobytes())
        protobuf_arr.compressed = True
    else:
        protobuf_arr.buffer = np_array.tobytes()
    return protobuf_arr


def dump_strings_public(strs: List[str], compressed: bool = False) -> 'vector_column_service_pb2.NdArray':
    return dump_numpy_public(np.array(strs, dtype='S'), compressed=compressed)


def dump_strings(strs: List[str], compressed: bool = False) -> 'core_pb2.NdArray':
    return dump_numpy(np.array(strs, dtype='S'), compressed=compressed)


def load_strings(proto_arr: 'core_pb2.NdArray') -> List[str]:
    return [str(item, 'utf-8') for item in load_numpy(proto_arr)]


def get_version():
    return Path(__file__).parent.parent.joinpath('__version__').read_text().strip()


def get_environment():
    return Path(__file__).parent.parent.joinpath('__environment__').read_text().strip()


def validate_dns_name(name):
    if not DNS_COMPATIBLE_REGEX.match(name):
        raise ValueError("{} is invalid - service names and node names must consist of lower case "
                         "alphanumeric characters or '-', start with an alphabetic character, and end with an "
                         "alphanumeric character (e.g. 'my-name', or 'abc-123')".format(name))