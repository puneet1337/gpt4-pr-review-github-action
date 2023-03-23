import os

import openai
from github import Github

GITHUB_TOKEN = os.environ['GITHUB_TOKEN']
GPT_4_API_KEY = os.environ['OPENAI_API_KEY']
GITHUB_REPOSITORY = os.environ['GITHUB_REPOSITORY']
GITHUB_PULL_REQUEST_NUMBER = os.environ['GITHUB_PULL_REQUEST_NUMBER']

openai.api_key = os.getenv(GPT_4_API_KEY)

g = Github(GITHUB_TOKEN)
repo = g.get_repo(GITHUB_REPOSITORY)
pr = repo.get_pull(int(GITHUB_PULL_REQUEST_NUMBER))
files = pr.get_files()

code_snippets = []
for file in files:
    if file.patch:
        code_snippets.append(file.patch)

gpt_4_request_data = {
    "api_key": GPT_4_API_KEY,
    "input": "\n\n".join(code_snippets)
}

response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are an expert software engineer & Github PR Review Bot. You are given Code "
                                      "as input, you generate a clear & concise PR Review with actionables creator "
                                      "can take."},
        {"role": "user", "content": gpt_4_request_data["input"]}
    ],
    temperature=.5,
)

response.raise_for_status()
gpt_output = response.json()["choices"][0]["message"]["content"].strip()

with open("gpt4_output.txt", "w") as f:
    f.write(gpt_output)
