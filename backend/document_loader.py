class Document:
    def __init__(self, doc_id, title, text):
        self.id = doc_id
        self.title = title
        self.text = text

def load_simple_wikipedia(path="data/simple_wikipedia/AllCombined.txt"):
    documents = []
    with open(path, "r", encoding="utf-8") as f:
        raw_text = f.read()

    # Articles are separated by blank lines
    articles = raw_text.split("\n\n")

    for idx, article in enumerate(articles):
        lines = article.strip().split("\n")
        if not lines:
            continue
        title = lines[0].strip()
        text = " ".join(lines[1:]).strip()
        if title and text:
            documents.append(Document(doc_id=idx, title=title, text=text))

    return documents

if __name__ == "__main__":
    docs = load_simple_wikipedia()
    print(f"Loaded {len(docs)} documents.")
    print("Example document:", docs[0].title, docs[0].text[:200])
    