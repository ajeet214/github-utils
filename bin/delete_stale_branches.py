#!/usr/bin/env python3
"""
CLI entry-point for deleting stale branches.
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
from src.actions.branch_cleaner import BranchCleaner

load_dotenv(dotenv_path=project_root / ".env")

@click.command()
@click.option("--owner", required=True, help="GitHub repository owner.")
@click.option("--repo", required=True, help="GitHub repository name.")
@click.option("--days-stale", type=int, default=30, show_default=True,
              help="Branches without commits older than this many days.")
@click.option("--debug/--no-debug", default=False, help="Enable debug logging.")
def main(owner, repo, days_stale, debug):
    if debug:
        logger.setLevel("DEBUG")
        logger.debug("Debug enabled")
    token = os.getenv('GITHUB_TOKEN')
    if not token:
        logger.error("Missing GITHUB_TOKEN")
        sys.exit(1)
    client = GitHubAPIClient(token, owner, repo)
    cleaner = BranchCleaner(client, days_stale)
    try:
        cleaner.clean()
    except Exception as e:
        logger.error(f"Error: {e}", exc_info=True)
        sys.exit(2)


if __name__ == '__main__':
    main()