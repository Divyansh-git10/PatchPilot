class CodeAgent:


    def __init__(self, client):
        self.client = client

    def read_file(self, file_path):

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                return f.read()

        except Exception:
            return ""

    def generate_patch(
        self,
        issue_analysis,
        engineering_plan,
        target_file
    ):

        file_content = self.read_file(target_file)

        prompt = f"""


    You are a senior Go engineer.

    GitHub Issue Analysis:
    {issue_analysis}

    Engineering Plan:
    {engineering_plan}

    Target File:
    {target_file}

    Current File Content:
    {file_content[:12000]}

    Generate a focused production-quality code patch.

    Requirements:

    * Keep changes minimal
    * Preserve existing style
    * Avoid unrelated modifications
    * Explain the proposed changes clearly

    Return:

    1. Summary of changes
    2. Modified code snippet
    3. Why the fix works
    """

    
        response = self.client.chat.completions.create(
            model="deepseek/deepseek-chat-v3-0324",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content
    
