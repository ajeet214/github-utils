# 🛠️ GitHub Utils
A collection of Python scripts for automating and managing various aspects of GitHub repositories using the GitHub REST API.

GitHub Utils is a lightweight toolkit of command-line utilities designed to automate and simplify common GitHub repository maintenance tasks. Whether you’re cleaning up old workflow runs, pruning stale branches, reviewing pull requests, or closing inactive issues, this repo has you covered.

---

## 📦 Features

🌟 Features

🛠️ Delete Old Workflow RunsClean up completed, queued, or in-progress GitHub Actions runs—either for a specific workflow file or across the entire repo.

🌿 Prune Stale BranchesIdentify and remove branches that haven’t seen commits in a configurable number of days.

🔍 List Pull RequestsFetch and display pull requests by state (open, closed, or all) along with their numbers and titles.

📭 Auto-Close Stale IssuesAutomatically close issues that haven’t been updated for a configurable period.

---
## 📁 Project Structure
```
github-utils/
├── bin/                           # CLI scripts (entry points)
│   ├── delete_old_workflow_runs   # Delete workflow runs
│   ├── delete_stale_branches      # Prune stale branches
│   ├── list_pull_requests         # List pull requests
│   └── auto_close_stale_issues    # Auto-close issues
│
├── src/                           # Library code
│   ├── config.py                  # Logging & configuration
│   ├── utils/                     # Low-level API helpers
│   │   └── github_client.py       # GitHubAPIClient
│   └── actions/                   # Task-specific classes
│       ├── base_action.py         # Abstract GitHubAction
│       ├── workflow_cleaner.py    # WorkflowCleaner
│       ├── branch_cleaner.py      # BranchCleaner
│       ├── pr_lister.py           # PullRequestLister
│       └── issue_closer.py        # StaleIssueAutoCloser
│
├── tests/                         # pytest test suites
├── .env                           # Environment variables (e.g., GITHUB_TOKEN)
├── requirements.txt               # Dependencies
└── README.md                      # Project overview and usage
```
---

## 🚀 Quick Start

### 1. Clone the Repo

```bash
git clone https://github.com/ajeet214/github-utils.git
cd github-utils
```
### 2. Create a virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate   # On Windows: .\.venv\Scripts\activate
```
### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
### 4. Set Up Your GitHub Token

Create a Personal Access Token (PAT) with appropriate scopes, such as:

 - repo — for repo access
 - workflow — for managing GitHub Actions
 - delete_repo (optional) — for cleanup scripts

Store it securely using an environment variable:
```bash
export GITHUB_TOKEN=your_token_here
```
or 
```bash
echo "GITHUB_TOKEN=<your_token>" > .env
```
### 5. Run a Tool
```python
# Delete up to 50 completed runs of notifier.yml
python bin/delete_old_workflow_runs.py \
  --owner your-username \
  --repo your-repo-name \
  --workflow-file your-workflow.yml \
  --max-runs 50 \
  --status completed
```

---
## 📖 Usage Examples
### Delete Old Workflow Runs
```commandline
python bin/delete_old_workflow_runs.py \
  --owner <owner> \
  --repo <repo> \
  --workflow-file notifier.yml \
  --max-runs 80 \
  --status completed \
  [--debug]
```
### Prune Stale Branches
```commandline
python bin/delete_stale_branches.py \
  --owner <owner> \
  --repo <repo> \
  --days-stale 30 \
  [--debug]
```
### List Pull Requests
```commandline
python bin/list_pull_requests.py \
  --owner <owner> \
  --repo <repo> \
  --state open \
  [--debug]
```
### Auto-Close Stale Issues
```commandline
python bin/auto_close_stale_issues.py \
  --owner <owner> \
  --repo <repo> \
  --days-stale 60 \
  [--debug]
```

---
## 🧪 Testing
Run the full test suite with pytest:
```commandline
pytest -q
```
All tests live under tests/ and use mocking to avoid real GitHub API calls.

---
## 🛠️ Development
- Add a new action: create a subclass of GitHubAction in src/actions/ and corresponding CLI in bin/.
- Extend client: add methods to src/utils/github_client.py.
- Adjust logging: modify src/config.py for new handlers or formats.

---
## 🤝 Contributions Welcome
We welcome contributions! Please fork, branch, and submit a PR with clear descriptions of changes.

---
## 📄 License
This project is licensed under the MIT License.