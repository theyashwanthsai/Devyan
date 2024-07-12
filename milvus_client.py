from pymilvus import connections, Collection, FieldSchema, CollectionSchema, DataType


class MilvusClient:
    def __init__(self, host="localhost", port="19530"):
        self.host = host
        self.port = port
        self.collection_name = "codebase"
        self.connect()

    def connect(self):
        try:
            connections.connect(host=self.host, port=self.port)
        except Exception as e:
            print(f"Failed to connect to Milvus: {e}")

    def create_collection(self):
        fields = [
            FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=True),
            FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=768),
        ]
        schema = CollectionSchema(fields, "Codebase collection")
        self.collection = Collection(self.collection_name, schema)

    def insert_embeddings(self, embeddings):
        self.collection.insert([embeddings])

    def search(self, query_embedding, top_k=5):
        search_params = {"metric_type": "L2", "params": {"nprobe": 10}}
        results = self.collection.search(
            [query_embedding], "embedding", search_params, limit=top_k
        )
        return results
