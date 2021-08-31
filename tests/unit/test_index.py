vector_dim = 8
vals1 = [0.1] * vector_dim
vals2 = [0.2] * vector_dim
md1 = {'genre': 'action', 'year': 2021}
md2 = {'genre': 'documentary', 'year': 2020}
filter1 = {'genre': {'$in': ['action']}}
filter2 = {'year': {'$eq': 2020}}


def test_upsert_request_tuples_id_data(mocker):
    import pinecone
    index = pinecone.Index('example-name')
    mocker.patch.object(index._vector_api, 'vector_service_upsert', autospec=True)
    index.upsert([('vec1', vals1), ('vec2', vals2)])
    index._vector_api.vector_service_upsert.assert_called_once_with(
        pinecone.UpsertRequest(vectors=[
            pinecone.Vector(id='vec1', values=vals1, metadata={}),
            pinecone.Vector(id='vec2', values=vals2, metadata={})
        ])
    )


def test_upsert_request_tuples_id_data_metadata(mocker):
    import pinecone
    index = pinecone.Index('example-name')
    mocker.patch.object(index._vector_api, 'vector_service_upsert', autospec=True)
    index.upsert([('vec1', vals1, md1),
                  ('vec2', vals2, md2)])
    index._vector_api.vector_service_upsert.assert_called_once_with(
        pinecone.UpsertRequest(vectors=[
            pinecone.Vector(id='vec1', values=vals1, metadata=md1),
            pinecone.Vector(id='vec2', values=vals2, metadata=md2)
        ])
    )


def test_query_request_tuples_query_only(mocker):
    import pinecone
    index = pinecone.Index('example-name')
    mocker.patch.object(index._vector_api, 'vector_service_query', autospec=True)
    index.query(queries=[vals1, vals2])
    index._vector_api.vector_service_query.assert_called_once_with(
        pinecone.QueryRequest(queries=[
            pinecone.QueryVector(values=vals1),
            pinecone.QueryVector(values=vals2)
        ])
    )


def test_query_request_tuples_query_filter(mocker):
    import pinecone
    index = pinecone.Index('example-name')
    mocker.patch.object(index._vector_api, 'vector_service_query', autospec=True)
    index.query(queries=[
        (vals1, filter1),
        (vals2, filter2)
    ])
    index._vector_api.vector_service_query.assert_called_once_with(
        pinecone.QueryRequest(queries=[
            pinecone.QueryVector(values=vals1, filter=filter1),
            pinecone.QueryVector(values=vals2, filter=filter2)
        ])
    )