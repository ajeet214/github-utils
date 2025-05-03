#!/usr/bin/env python3
"""
CLI entry-point for deleting old GitHub Actions workflow runs.
"""
import sys
from pathlib import Path

project_root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(project_root))

import os
import click
from dotenv import load_dotenv
from src.config import logger
from src.utils.github_client import GitHubAPIClient
from src.actions.workflow_cleaner import WorkflowCleaner

load_dotenv(dotenv_path=project_root / ".env")


@click.command()
@click.option("--owner", required=True, help="GitHub repository owner.")
@click.option("--repo", required=True, help="GitHub repository name.")
@click.option("--workflow-file", default=None, help="Workflow filename.")
@click.option("--max-runs", type=int, default=80, show_default=True, help="Max runs to delete.")
@click.option("--status", type=click.Choice(["completed","in_progress","queued"], case_sensitive=False),
              default="completed", show_default=True, help="Status filter.")
@click.option("--debug/--no-debug", default=False, help="Enable debug logging.")
def main(owner, repo, workflow_file, max_runs, status, debug):
    if debug:
        logger.setLevel("DEBUG")
        logger.debug("Debug enabled")
    token = os.getenv('GITHUB_TOKEN')
    if not token:
        logger.error("Missing GITHUB_TOKEN")
        sys.exit(1)
    client = GitHubAPIClient(token, owner, repo)
    cleaner = WorkflowCleaner(client, workflow_file, max_runs, status)
    try:
        cleaner.clean()
    except Exception as e:
        logger.error(f"Error: {e}", exc_info=True)
        sys.exit(2)


if __name__ == '__main__':
    main()