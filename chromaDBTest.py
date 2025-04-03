__import__('pysqlite3')
import chromadb
import sys

chroma_client = chromadb.Client()

collection = chroma_client.create_collection(name="my_collection")
collection.add(
    documents=[
        "Cats are small, carnivorous mammals that are often kept as pets.",
        "Dogs are loyal animals and are often referred to as man's best friend.",
        "The sun is the star at the center of the solar system.",
        "The moon orbits the Earth and affects ocean tides.",
        "Python is a popular programming language known for its simplicity.",
        "JavaScript is widely used for web development and interactive websites.",
        "Mount Everest is the highest mountain in the world.",
        "The Amazon rainforest is known for its biodiversity and dense vegetation."
    ],
    ids=["id1", "id2", "id3", "id4", "id5", "id6", "id7", "id8"]
)

results = collection.query(
    query_texts=[
        "Tell me about cats.",
        "What is the tallest mountain?",
        "Explain the importance of the moon.",
        "What is Python programming?"
    ],
    n_results=3  # Retrieve the top 3 most similar documents
)

print("Results:", results)
