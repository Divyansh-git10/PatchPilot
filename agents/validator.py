import subprocess

class ValidationAgent:


    def __init__(self, repo_path):
        self.repo_path = repo_path

    def run_tests(self):

        try:

            result = subprocess.run(
                ["go", "test", "./..."],
                cwd=self.repo_path,
                capture_output=True,
                text=True
            )

            return {
                "success": result.returncode == 0,
                "stdout": result.stdout,
                "stderr": result.stderr
            }

        except Exception as e:

            return {
                "success": False,
                "stdout": "",
                "stderr": str(e)
            }

