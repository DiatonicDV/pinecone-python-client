# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import pinecone.protos.vector_service_pb2 as vector__service__pb2

class VectorServiceStub(object):
    """The VectorService interface is exposed by Pinecone vector database services
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Upsert = channel.unary_unary(
                '/pinecone.VectorService/Upsert',
                request_serializer=vector__service__pb2.UpsertRequest.SerializeToString,
                response_deserializer=vector__service__pb2.UpsertResponse.FromString,
                )
        self.Delete = channel.unary_unary(
                '/pinecone.VectorService/Delete',
                request_serializer=vector__service__pb2.DeleteRequest.SerializeToString,
                response_deserializer=vector__service__pb2.DeleteResponse.FromString,
                )
        self.Fetch = channel.unary_unary(
                '/pinecone.VectorService/Fetch',
                request_serializer=vector__service__pb2.FetchRequest.SerializeToString,
                response_deserializer=vector__service__pb2.FetchResponse.FromString,
                )
        self.Query = channel.unary_unary(
                '/pinecone.VectorService/Query',
                request_serializer=vector__service__pb2.QueryRequest.SerializeToString,
                response_deserializer=vector__service__pb2.QueryResponse.FromString,
                )
        self.List = channel.unary_unary(
                '/pinecone.VectorService/List',
                request_serializer=vector__service__pb2.ListRequest.SerializeToString,
                response_deserializer=vector__service__pb2.ListResponse.FromString,
                )
        self.ListNamespaces = channel.unary_unary(
                '/pinecone.VectorService/ListNamespaces',
                request_serializer=vector__service__pb2.ListNamespacesRequest.SerializeToString,
                response_deserializer=vector__service__pb2.ListNamespacesResponse.FromString,
                )
        self.Summarize = channel.unary_unary(
                '/pinecone.VectorService/Summarize',
                request_serializer=vector__service__pb2.SummarizeRequest.SerializeToString,
                response_deserializer=vector__service__pb2.SummarizeResponse.FromString,
                )


class VectorServiceServicer(object):
    """The VectorService interface is exposed by Pinecone vector database services
    """

    def Upsert(self, request, context):
        """The Upsert operation is for uploading data (vector ids and values) to be indexed.
        Note: Most users are recommended to submit upserts via the StreamWrites operation instead.
        If a new value is upserted for an existing vector id, it overwrites the previous value.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """The Delete operation deletes a vector by id.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Fetch(self, request, context):
        """The FetchVectors operation returns a vector value by id.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Query(self, request, context):
        """The Query operation queries the database for the nearest stored vectors to one
        or more query vectors and returns their ids and/or values.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """The List operation returns the vector IDs in this database.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListNamespaces(self, request, context):
        """The ListNamespaces operation returns the namespaces for which data exists in this
        database.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Summarize(self, request, context):
        """The Summarize operation returns summary statistics about the database contents.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_VectorServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Upsert': grpc.unary_unary_rpc_method_handler(
                    servicer.Upsert,
                    request_deserializer=vector__service__pb2.UpsertRequest.FromString,
                    response_serializer=vector__service__pb2.UpsertResponse.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=vector__service__pb2.DeleteRequest.FromString,
                    response_serializer=vector__service__pb2.DeleteResponse.SerializeToString,
            ),
            'Fetch': grpc.unary_unary_rpc_method_handler(
                    servicer.Fetch,
                    request_deserializer=vector__service__pb2.FetchRequest.FromString,
                    response_serializer=vector__service__pb2.FetchResponse.SerializeToString,
            ),
            'Query': grpc.unary_unary_rpc_method_handler(
                    servicer.Query,
                    request_deserializer=vector__service__pb2.QueryRequest.FromString,
                    response_serializer=vector__service__pb2.QueryResponse.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=vector__service__pb2.ListRequest.FromString,
                    response_serializer=vector__service__pb2.ListResponse.SerializeToString,
            ),
            'ListNamespaces': grpc.unary_unary_rpc_method_handler(
                    servicer.ListNamespaces,
                    request_deserializer=vector__service__pb2.ListNamespacesRequest.FromString,
                    response_serializer=vector__service__pb2.ListNamespacesResponse.SerializeToString,
            ),
            'Summarize': grpc.unary_unary_rpc_method_handler(
                    servicer.Summarize,
                    request_deserializer=vector__service__pb2.SummarizeRequest.FromString,
                    response_serializer=vector__service__pb2.SummarizeResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'pinecone.VectorService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class VectorService(object):
    """The VectorService interface is exposed by Pinecone vector database services
    """

    @staticmethod
    def Upsert(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pinecone.VectorService/Upsert',
            vector__service__pb2.UpsertRequest.SerializeToString,
            vector__service__pb2.UpsertResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pinecone.VectorService/Delete',
            vector__service__pb2.DeleteRequest.SerializeToString,
            vector__service__pb2.DeleteResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Fetch(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pinecone.VectorService/Fetch',
            vector__service__pb2.FetchRequest.SerializeToString,
            vector__service__pb2.FetchResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Query(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pinecone.VectorService/Query',
            vector__service__pb2.QueryRequest.SerializeToString,
            vector__service__pb2.QueryResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def List(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pinecone.VectorService/List',
            vector__service__pb2.ListRequest.SerializeToString,
            vector__service__pb2.ListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListNamespaces(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pinecone.VectorService/ListNamespaces',
            vector__service__pb2.ListNamespacesRequest.SerializeToString,
            vector__service__pb2.ListNamespacesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Summarize(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pinecone.VectorService/Summarize',
            vector__service__pb2.SummarizeRequest.SerializeToString,
            vector__service__pb2.SummarizeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
