import os

class EmbeddingTool:


    def __init__(self):

        self.documents = []

        self.file_paths = []

    def load_go_files(self, repo_path):

        for root, dirs, files in os.walk(repo_path):

            for file in files:

                if file.endswith(".go"):

                    path = os.path.join(root, file)

                    try:
                        with open(path, "r", encoding="utf-8") as f:

                            content = f.read().lower()

                            self.documents.append(content)

                            self.file_paths.append(path)

                    except:
                        pass

    def search(self, query, top_k=5):

        query_words = query.lower().split()

        scores = []

        for i, doc in enumerate(self.documents):

            score = 0

            for word in query_words:

                score += doc.count(word)

            scores.append((score, self.file_paths[i]))

        scores.sort(reverse=True)

        return [x[1] for x in scores[:top_k]]




