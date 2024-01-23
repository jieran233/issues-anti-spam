# issues-anti-spam

> 🚧 The project is currently in development stage. Now it might be able to run preliminarily

This project aims to help open-source project developers better focus on the development and maintenance of the project itself, stay away from annoying rookie issues.

The core of this project is a GitHub Workflow file and a prompt for ChatGPT. The GitHub Workflow will be triggered when a new issue is opened. It will send the prompt and the title, content of the issue (obtained through GitHub API) to ChatGPT in Actions, and handle the issue through GitHub API based on ChatGPT's response, spam content will be hidden.

Demo: (may not reflect the effects of the latest version)

- Spam: [Issue](https://github.com/jieran233/issues-anti-spam/issues/4), [Workflow run](https://github.com/jieran233/issues-anti-spam/actions/runs/7613432937)
- Suspicious: [Issue](https://github.com/jieran233/issues-anti-spam/issues/7), [Workflow run](https://github.com/jieran233/issues-anti-spam/actions/runs/7613573885)
- Harmless: [Issue](https://github.com/jieran233/issues-anti-spam/issues/3), [Workflow run](https://github.com/jieran233/issues-anti-spam/actions/runs/7613376008)

## Use it for your repository

- Fork this repo, and modify the workflow file and prompt file in your fork to better suit your project needs
  - You can add introduction to project or rules for the issues in the prompt file to make ChatGPT better serve your project
  - Make sure the environment variable `PROMPT_FILE_URL` in the workflow file is referred to your fork
 
- Copy the workflow file in the fork to your repository which you want to use issues-anti-spam

- Goto `https://github.com/settings/tokens/new` (Your GitHub --> Settings --> Developer settings --> Personal access tokens (classic) --> Generate new token (classic)) to create a token for reading/writing issues of your repository:
  - Set name and expiration
  - Select scopes: check `repo`

- Register a new ChatGPT account and make sure the account is only used for ChatGPT Web API because it will leave all messages in the conversations history. Then obtain the session token of ChatGPT for the account (See [here](https://github.com/Sxvxgee/UnlimitedGPT/blob/main/docs/README.md#obtaining-the-session-token))

- Goto `https://github.com/USER_NAME/REPO_NAME/settings/secrets/actions/new` (Your Repo --> Settings --> Secrets and variables --> Action --> New repository secrets) to create secrets for your repository:
  1. Name: `GH_TOKEN_REPO`, value: fill in the GitHub token you just generated
  2. Name: `CHATGPT_SESSION_TOKEN`, value: fill in the ChatGPT session token you just obtained

- Add labels of issues for your repository (Your Repo --> Issues --> Labels --> New label):
  1. Name: `spam`
  2. Name: `suspicious-spam`

- Then you can open an issue in your repository for testing if it works properly

## Used Libraries

- [jieran233/chatgpt-api-server](https://github.com/jieran233/chatgpt-api-server)

## Acknowledgments

In building this project, we would like to acknowledge the contributions of the following projects:

- [Sxvxgee/UnlimitedGPT](https://github.com/Sxvxgee/UnlimitedGPT)
- [nick-fields/retry](https://github.com/nick-fields/retry)
