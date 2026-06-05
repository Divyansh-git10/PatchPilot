from dotenv import load_dotenv
from openai import OpenAI
from agents.issue_analyzer import IssueAnalyzer
from agents.repo_mapper import RepoMapper
from tools.embedding_tool import EmbeddingTool
from agents.planner import PlannerAgent
from agents.coder import CodeAgent
from agents.validator import ValidationAgent
from agents.pr_writer import PRWriterAgent



import os

load_dotenv()

client = OpenAI(
base_url="https://openrouter.ai/api/v1",
api_key=os.getenv("OPENAI_API_KEY")
)

issue_url = input("Enter GitHub Issue URL: ")

agent = IssueAnalyzer(client)

print("\nFetching issue...\n")

issue_text = agent.fetch_issue(issue_url)

print("Analyzing issue with AI...\n")

analysis = agent.analyze_issue(issue_text)

print("\n=== ISSUE ANALYSIS ===\n")

print(analysis)
repo_path = "repositories/cobra"

mapper = RepoMapper(repo_path)

keywords = [
"completion",
"args",
"shell",
"command"
]

relevant_files = mapper.find_relevant_files(keywords)

print("\n=== RELEVANT FILES ===\n")

for file in relevant_files:
    print(file)

print("\nBuilding semantic search index...\n")

embedder = EmbeddingTool()

embedder.load_go_files(repo_path)


semantic_results = embedder.search(
issue_text,
top_k=5
)

print("\n=== SEMANTIC SEARCH RESULTS ===\n")

for result in semantic_results:
    print(result)

planner = PlannerAgent(client)

print("\nGenerating engineering plan...\n")

plan = planner.create_plan(
analysis,
relevant_files,
semantic_results
)

print("\n=== ENGINEERING PLAN ===\n")

print(plan)

coder = CodeAgent(client)

target_file = semantic_results[0]

print("\nGenerating code patch...\n")

patch = coder.generate_patch(
analysis,
plan,
target_file
)

print("\n=== GENERATED PATCH ===\n")

print(patch)

validator = ValidationAgent(repo_path)

print("\nRunning repository tests...\n")

test_results = validator.run_tests()

print("\n=== TEST RESULTS ===\n")

print("Success:", test_results["success"])

print("\nSTDOUT:\n")
print(test_results["stdout"][:3000])

print("\nSTDERR:\n")
print(test_results["stderr"][:3000])
pr_agent = PRWriterAgent(client)

print("\nGenerating PR summary...\n")

pr_summary = pr_agent.generate_pr(
analysis,
plan,
patch
)

print("\n=== GENERATED PR ===\n")

print(pr_summary)
