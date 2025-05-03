# 🛠️ GitHub Utils
A collection of Python scripts for automating and managing various aspects of GitHub repositories using the GitHub REST API.

This toolkit is designed for developers, maintainers, DevOps engineers, and open-source contributors who want to streamline daily GitHub tasks — from cleaning up old workflow runs to managing stale branches, listing pull request stats, and more.
---

## 📦 Features

- 🔁 **Delete Old Workflow Runs**: Bulk delete completed GitHub Actions workflow runs.
- 🌿 **Delete Stale Branches** *(coming soon)*: Identify and remove local or remote branches with no recent activity.
- 🧹 **Clean Up Merged Pull Request Branches** *(coming soon)*: Automatically delete branches after merge.
- 📊 **List Pull Request Statistics** *(coming soon)*: Get an overview of open, merged, and closed PRs.
- 📄 **List Repository Files** *(coming soon)*: Use GitHub API to list files/folders in a repo path.
- 🚨 **Auto-Close Stale Issues** *(planned)*: Detect and close issues with no recent activity.

---

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/<your-username>/github-utils.git
cd github-utils
```
## Install Dependencies
```bash
pip install -r requirements.txt
```
## Set Up Your GitHub Token
Create a Personal Access Token (PAT) with appropriate scopes, such as:

 - repo — for repo access
 - workflow — for managing GitHub Actions
 - delete_repo (optional) — for cleanup scripts

Store it securely using an environment variable:
```bash
export GITHUB_TOKEN=your_token_here
```
## 🧰 Example Scripts
### Delete Completed Workflow Runs
```python
python delete_old_workflow_runs.py \
  --owner your-username \
  --repo your-repo-name \
  --workflow your-workflow.yml \
  --status completed \
  --limit 50
```
