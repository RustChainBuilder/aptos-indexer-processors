from aptos.util.timestamp import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RawDatastreamRequest(_message.Message):
    __slots__ = ["starting_version", "transactions_count"]
    STARTING_VERSION_FIELD_NUMBER: _ClassVar[int]
    TRANSACTIONS_COUNT_FIELD_NUMBER: _ClassVar[int]
    starting_version: int
    transactions_count: int
    def __init__(self, starting_version: _Optional[int] = ..., transactions_count: _Optional[int] = ...) -> None: ...

class RawDatastreamResponse(_message.Message):
    __slots__ = ["chain_id", "data", "status"]
    CHAIN_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    chain_id: int
    data: TransactionsOutput
    status: StreamStatus
    def __init__(self, status: _Optional[_Union[StreamStatus, _Mapping]] = ..., data: _Optional[_Union[TransactionsOutput, _Mapping]] = ..., chain_id: _Optional[int] = ...) -> None: ...

class StreamStatus(_message.Message):
    __slots__ = ["end_version", "start_version", "type"]
    class StatusType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    END_VERSION_FIELD_NUMBER: _ClassVar[int]
    START_VERSION_FIELD_NUMBER: _ClassVar[int]
    STATUS_TYPE_BATCH_END: StreamStatus.StatusType
    STATUS_TYPE_INIT: StreamStatus.StatusType
    STATUS_TYPE_UNSPECIFIED: StreamStatus.StatusType
    TYPE_FIELD_NUMBER: _ClassVar[int]
    end_version: int
    start_version: int
    type: StreamStatus.StatusType
    def __init__(self, type: _Optional[_Union[StreamStatus.StatusType, str]] = ..., start_version: _Optional[int] = ..., end_version: _Optional[int] = ...) -> None: ...

class TransactionOutput(_message.Message):
    __slots__ = ["encoded_proto_data", "timestamp", "version"]
    ENCODED_PROTO_DATA_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    encoded_proto_data: bytes
    timestamp: _timestamp_pb2.Timestamp
    version: int
    def __init__(self, encoded_proto_data: _Optional[bytes] = ..., version: _Optional[int] = ..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class TransactionsOutput(_message.Message):
    __slots__ = ["transactions"]
    TRANSACTIONS_FIELD_NUMBER: _ClassVar[int]
    transactions: _containers.RepeatedCompositeFieldContainer[TransactionOutput]
    def __init__(self, transactions: _Optional[_Iterable[_Union[TransactionOutput, _Mapping]]] = ...) -> None: ...