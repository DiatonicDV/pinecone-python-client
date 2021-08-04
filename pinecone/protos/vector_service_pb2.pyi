# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
    RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int


DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class DenseVector(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    id: typing___Text = ...
    values: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___float] = ...
    metadata: typing___Text = ...

    def __init__(self,
        *,
        id : typing___Optional[typing___Text] = None,
        values : typing___Optional[typing___Iterable[builtin___float]] = None,
        metadata : typing___Optional[typing___Text] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"id",b"id",u"metadata",b"metadata",u"values",b"values"]) -> None: ...
type___DenseVector = DenseVector

class AnonymousVector(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    values: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___float] = ...

    def __init__(self,
        *,
        values : typing___Optional[typing___Iterable[builtin___float]] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"values",b"values"]) -> None: ...
type___AnonymousVector = AnonymousVector

class ScoredVector(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    id: typing___Text = ...
    score: builtin___float = ...
    values: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___float] = ...
    metadata: typing___Text = ...

    def __init__(self,
        *,
        id : typing___Optional[typing___Text] = None,
        score : typing___Optional[builtin___float] = None,
        values : typing___Optional[typing___Iterable[builtin___float]] = None,
        metadata : typing___Optional[typing___Text] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"id",b"id",u"metadata",b"metadata",u"score",b"score",u"values",b"values"]) -> None: ...
type___ScoredVector = ScoredVector

class UpsertRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    request_id: builtin___int = ...
    namespace: typing___Text = ...

    @property
    def vectors(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___DenseVector]: ...

    def __init__(self,
        *,
        request_id : typing___Optional[builtin___int] = None,
        vectors : typing___Optional[typing___Iterable[type___DenseVector]] = None,
        namespace : typing___Optional[typing___Text] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"namespace",b"namespace",u"request_id",b"request_id",u"vectors",b"vectors"]) -> None: ...
type___UpsertRequest = UpsertRequest

class UpsertResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    request_id: builtin___int = ...

    def __init__(self,
        *,
        request_id : typing___Optional[builtin___int] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"request_id",b"request_id"]) -> None: ...
type___UpsertResponse = UpsertResponse

class DeleteRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    request_id: builtin___int = ...
    ids: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text] = ...
    delete_all: builtin___bool = ...
    namespace: typing___Text = ...

    def __init__(self,
        *,
        request_id : typing___Optional[builtin___int] = None,
        ids : typing___Optional[typing___Iterable[typing___Text]] = None,
        delete_all : typing___Optional[builtin___bool] = None,
        namespace : typing___Optional[typing___Text] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"delete_all",b"delete_all",u"ids",b"ids",u"namespace",b"namespace",u"request_id",b"request_id"]) -> None: ...
type___DeleteRequest = DeleteRequest

class DeleteResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    request_id: builtin___int = ...

    def __init__(self,
        *,
        request_id : typing___Optional[builtin___int] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"request_id",b"request_id"]) -> None: ...
type___DeleteResponse = DeleteResponse

class FetchRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    request_id: builtin___int = ...
    ids: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text] = ...
    namespace: typing___Text = ...

    def __init__(self,
        *,
        request_id : typing___Optional[builtin___int] = None,
        ids : typing___Optional[typing___Iterable[typing___Text]] = None,
        namespace : typing___Optional[typing___Text] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"ids",b"ids",u"namespace",b"namespace",u"request_id",b"request_id"]) -> None: ...
type___FetchRequest = FetchRequest

class FetchResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    request_id: builtin___int = ...
    namespace: typing___Text = ...

    @property
    def vectors(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___DenseVector]: ...

    def __init__(self,
        *,
        request_id : typing___Optional[builtin___int] = None,
        vectors : typing___Optional[typing___Iterable[type___DenseVector]] = None,
        namespace : typing___Optional[typing___Text] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"namespace",b"namespace",u"request_id",b"request_id",u"vectors",b"vectors"]) -> None: ...
type___FetchResponse = FetchResponse

class QueryRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class QueryVector(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        top_k: builtin___int = ...
        namespace: typing___Text = ...
        filter: typing___Text = ...

        @property
        def vector(self) -> type___AnonymousVector: ...

        def __init__(self,
            *,
            vector : typing___Optional[type___AnonymousVector] = None,
            top_k : typing___Optional[builtin___int] = None,
            namespace : typing___Optional[typing___Text] = None,
            filter : typing___Optional[typing___Text] = None,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"vector",b"vector"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"filter",b"filter",u"namespace",b"namespace",u"top_k",b"top_k",u"vector",b"vector"]) -> None: ...
    type___QueryVector = QueryVector

    request_id: builtin___int = ...
    request_default_namespace: typing___Text = ...
    request_default_top_k: builtin___int = ...
    request_default_filter: typing___Text = ...
    include_data: builtin___bool = ...
    include_metadata: builtin___bool = ...

    @property
    def queries(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___QueryRequest.QueryVector]: ...

    def __init__(self,
        *,
        request_id : typing___Optional[builtin___int] = None,
        request_default_namespace : typing___Optional[typing___Text] = None,
        request_default_top_k : typing___Optional[builtin___int] = None,
        request_default_filter : typing___Optional[typing___Text] = None,
        include_data : typing___Optional[builtin___bool] = None,
        include_metadata : typing___Optional[builtin___bool] = None,
        queries : typing___Optional[typing___Iterable[type___QueryRequest.QueryVector]] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"include_data",b"include_data",u"include_metadata",b"include_metadata",u"queries",b"queries",u"request_default_filter",b"request_default_filter",u"request_default_namespace",b"request_default_namespace",u"request_default_top_k",b"request_default_top_k",u"request_id",b"request_id"]) -> None: ...
type___QueryRequest = QueryRequest

class QueryResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class SingleQueryResults(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        namespace: typing___Text = ...

        @property
        def matches(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___ScoredVector]: ...

        def __init__(self,
            *,
            matches : typing___Optional[typing___Iterable[type___ScoredVector]] = None,
            namespace : typing___Optional[typing___Text] = None,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"matches",b"matches",u"namespace",b"namespace"]) -> None: ...
    type___SingleQueryResults = SingleQueryResults

    request_id: builtin___int = ...

    @property
    def results(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___QueryResponse.SingleQueryResults]: ...

    def __init__(self,
        *,
        request_id : typing___Optional[builtin___int] = None,
        results : typing___Optional[typing___Iterable[type___QueryResponse.SingleQueryResults]] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"request_id",b"request_id",u"results",b"results"]) -> None: ...
type___QueryResponse = QueryResponse

class ListRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    request_id: builtin___int = ...
    namespace: typing___Text = ...

    def __init__(self,
        *,
        request_id : typing___Optional[builtin___int] = None,
        namespace : typing___Optional[typing___Text] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"namespace",b"namespace",u"request_id",b"request_id"]) -> None: ...
type___ListRequest = ListRequest

class ListResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    request_id: builtin___int = ...
    ids: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text] = ...
    namespace: typing___Text = ...

    def __init__(self,
        *,
        request_id : typing___Optional[builtin___int] = None,
        ids : typing___Optional[typing___Iterable[typing___Text]] = None,
        namespace : typing___Optional[typing___Text] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"ids",b"ids",u"namespace",b"namespace",u"request_id",b"request_id"]) -> None: ...
type___ListResponse = ListResponse

class ListNamespacesRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    request_id: builtin___int = ...

    def __init__(self,
        *,
        request_id : typing___Optional[builtin___int] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"request_id",b"request_id"]) -> None: ...
type___ListNamespacesRequest = ListNamespacesRequest

class ListNamespacesResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    request_id: builtin___int = ...
    namespaces: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text] = ...

    def __init__(self,
        *,
        request_id : typing___Optional[builtin___int] = None,
        namespaces : typing___Optional[typing___Iterable[typing___Text]] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"namespaces",b"namespaces",u"request_id",b"request_id"]) -> None: ...
type___ListNamespacesResponse = ListNamespacesResponse

class SummarizeRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    request_id: builtin___int = ...

    def __init__(self,
        *,
        request_id : typing___Optional[builtin___int] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"request_id",b"request_id"]) -> None: ...
type___SummarizeRequest = SummarizeRequest

class SummarizeResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    request_id: builtin___int = ...
    index_size: builtin___int = ...
    dimension: builtin___int = ...

    def __init__(self,
        *,
        request_id : typing___Optional[builtin___int] = None,
        index_size : typing___Optional[builtin___int] = None,
        dimension : typing___Optional[builtin___int] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"dimension",b"dimension",u"index_size",b"index_size",u"request_id",b"request_id"]) -> None: ...
type___SummarizeResponse = SummarizeResponse
