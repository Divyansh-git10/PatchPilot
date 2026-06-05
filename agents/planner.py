class PlannerAgent:

    def __init__(self, client):
        self.client = client

    def create_plan(
        self,
        issue_analysis,
        relevant_files,
        semantic_results
    ):

        relevant_context = "\n".join(relevant_files)

        semantic_context = "\n".join(semantic_results)

        prompt = f"""


    You are a senior Go engineer working on an open-source repository.

    Issue Analysis:
    {issue_analysis}

    Relevant Files:
    {relevant_context}

    Semantic Search Results:
    {semantic_context}

    Create a focused engineering plan.

    Return:

    1. Root Cause
    2. Files To Modify
    3. Functions Likely To Change
    4. Proposed Code Changes
    5. Testing Strategy
    6. Possible Risks

    Keep the solution minimal, safe, and production-oriented.
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

