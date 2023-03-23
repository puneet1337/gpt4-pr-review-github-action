# GPT-4 PR Review GitHub Action

This GitHub Action automatically reviews newly created pull requests using OpenAI's GPT-4 language model (using GPT-3 if GPT-4 is not available) and adds comments based on the model's output. By leveraging the power of GPT-4, this action helps maintainers to identify potential issues in the submitted code, suggest improvements, and streamline the code review process.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
  - [Step 1: Clone the Repository](#step-1-clone-the-repository)
  - [Step 2: Add the GPT-4 API Key](#step-2-add-the-gpt-4-api-key)
  - [Step 3: Add the Personal Access Token](#step-3-add-the-personal-access-token)
- [Usage](#usage)
- [License](#license)

## Features

- Automatically reviews new pull requests using the GPT-4 language model
- Adds comments based on the model's output
- Streamlines the code review process for maintainers

## Prerequisites

To use this GitHub Action, you need the following:

1. A GitHub account and a repository where you want to set up the action.
2. An OpenAI API key (you can sign up for an API key at [https://beta.openai.com/signup/](https://beta.openai.com/signup/)).
3. A GitHub personal access token with `repo` and `workflow` permissions (see [Creating a personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)).

## Setup

Follow these steps to set up the GPT-4 PR Review GitHub Action in your repository:

### Step 1: Clone the Repository

Clone the GPT-4 PR Review GitHub Action repository:

```bash
git clone https://github.com/yourusername/gpt4-pr-review-github-action.git
````
Copy the `.github` directory from the cloned repository to your own repository.

### Step 2: Add the GPT-4 API Key

Add the OpenAI API key as a secret in your GitHub repository:

1. Go to your repository's **Settings**.
2. Navigate to the **Secrets** tab.
3. Click **New repository secret**.
4. Name the secret `GPT_4_API_KEY` and add the corresponding API key.

### Step 3: Add the Personal Access Token

Add the GitHub personal access token as a secret in your GitHub repository:

1. Follow the same steps as in Step 2 to access the **Secrets** tab.
2. Click **New repository secret**.
3. Name the secret `PAT` and add the personal access token you created.

## Usage

Once you've set up the GPT-4 PR Review GitHub Action, it will automatically review newly created pull requests in your repository. The action will analyze the changes in the pull request, generate comments using the GPT-4 language model, and post these comments as a review on the pull request.

To test the functionality, create a new branch in your repository, make changes to a file or add a new file, and then create a pull request. The GPT-4 PR Review GitHub Action will run and provide a review with comments based on the submitted code.

## License

This project is licensed under the [MIT License](LICENSE). Please refer to the LICENSE file for more details.
