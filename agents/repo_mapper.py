import os

class RepoMapper:


    def __init__(self, repo_path):
        self.repo_path = repo_path

    def scan_repository(self):

        go_files = []

        test_files = []

        for root, dirs, files in os.walk(self.repo_path):

            for file in files:

                if file.endswith(".go"):

                    full_path = os.path.join(root, file)

                    go_files.append(full_path)

                    if file.endswith("_test.go"):
                        test_files.append(full_path)

        return {
            "go_files": go_files,
            "test_files": test_files
        }

    def find_relevant_files(self, issue_keywords):

        relevant = []

        repo_data = self.scan_repository()

        for file_path in repo_data["go_files"]:

            file_name = os.path.basename(file_path).lower()

            for keyword in issue_keywords:

                if keyword.lower() in file_name:
                    relevant.append(file_path)

        return list(set(relevant))

