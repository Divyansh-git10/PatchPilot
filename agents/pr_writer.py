class PRWriterAgent:


    def __init__(self, client):
        self.client = client

    def generate_pr(
        self,
        issue_analysis,
        engineering_plan,
        patch
    ):

        prompt = f"""


    You are an experienced open-source contributor.

    Generate a professional GitHub pull request summary.

    Issue Analysis:
    {issue_analysis}

    Engineering Plan:
    {engineering_plan}

    Generated Patch:
    {patch}

    Return:

    1. PR Title
    2. PR Description
    3. Key Changes
    4. Testing Performed
    5. Limitations / Notes

    Keep the PR concise, technical, and professional.
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

