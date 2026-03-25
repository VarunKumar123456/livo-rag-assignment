print("🚀 STARTING LIVO RAG APPLICATION...\n")

from utils import get_transcript
import re

# Step 1: Load transcripts
print("📥 Fetching transcripts...")

videos = [
    "aircAruvnKk",
    "wjZofJX0v4M",
    "fHF22Wxuyw4",
    "C6YtPJxNULA"
]

documents = []

for vid in videos:
    text = get_transcript(vid)
    if text.strip():
        documents.append(text)

print("✅ Transcripts loaded successfully!")

# Step 2: Clean + split text
print("\n🧠 Preparing knowledge base...")

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return text

chunks = []
for doc in documents:
    parts = doc.split(".")
    chunks.extend([clean_text(p.strip()) for p in parts if p.strip()])

print(f"✅ {len(chunks)} knowledge chunks ready!")

# Normalize words
def normalize(word):
    return word[:-1] if word.endswith("s") else word

# Step 3: Retrieval
def ask(query):
    stopwords = ["what", "is", "the", "a", "an", "of", "to", "do"]

    query_clean = clean_text(query)
    query_words = [normalize(w) for w in query_clean.split() if w not in stopwords]

    results = []

    for chunk in chunks:
        chunk_words = [normalize(w) for w in chunk.split()]
        score = sum(word in chunk_words for word in query_words)

        if score > 0:
            results.append((score, chunk))

    results.sort(reverse=True)

    print("\n===================================")
    print("🔎 QUERY:", query_clean)
    print("===================================\n")

    if len(results) == 0:
        print("❌ No relevant results found.\n")
        return

    print("📌 TOP MATCHES:\n")
    for i, (score, text) in enumerate(results[:2], 1):
        confidence = round(score / max(len(query_words), 1), 2)
        print(f"{i}. {text}")
        print(f"   🔹 Confidence: {confidence}\n")

# Step 4: Loop
print("\n🎯 System Ready! Ask your questions below.\n")

while True:
    q = input("👉 Ask (type 'exit' to quit): ")

    if q.lower() == "exit":
        print("\n👋 Exiting... Thank you!")
        break

    ask(q)
