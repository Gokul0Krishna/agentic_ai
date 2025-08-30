from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")  # downloads weights
emb = model.encode("This runs fine on CPU.")
print(len(emb), emb[:5])


        
                