from qdrant_client import QdrantClient

print("conecting to qdrant...")
qdrant_client = QdrantClient(
    url="https://80432624-41ed-4f74-8ac3-a588187afe33.eu-central-1-0.aws.cloud.qdrant.io:6333", 
    api_key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJtIn0.WqTUHM5JmLkWl8Hs-B5Bpq3vOC6M_us8BPfZAItJAx4",
)

print(qdrant_client.get_collections())
print("qdrant connection successful")

