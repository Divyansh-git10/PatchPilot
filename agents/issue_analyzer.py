import requests
from bs4 import BeautifulSoup

class IssueAnalyzer:


    def __init__(self, client):
        self.client = client

    def fetch_issue(self, issue_url):

        response = requests.get(issue_url)

        if response.status_code != 200:
            raise Exception("Failed to fetch issue")

        soup = BeautifulSoup(response.text, "html.parser")

        text = soup.get_text(separator="\n")

        return text[:15000]

    def analyze_issue(self, issue_text):

        prompt = f"""
    You are a senior Go developer.

    Analyze this GitHub issue carefully.

    Return:

    1. Issue Summary
    2. Problem Type
    3. Possible Affected Modules
    4. Suggested Fix Direction
    5. Testing Considerations

    Issue:
    {issue_text}
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

