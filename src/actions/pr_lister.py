from src.config import logger as root_logger
from src.actions.base_action import GitHubAction

logger = root_logger.getChild("pr_lister")


class PullRequestLister(GitHubAction):
    def __init__(self, client, state="open"):
        super().__init__(client)
        self.state = state

    def list(self):
        prs = self.client._request('GET', '/pulls', params={'state': self.state})
        logger.info(f"Found {len(prs)} pull requests (state={self.state}).")
        for pr in prs:
            logger.info(f"PR #{pr['number']}: {pr['title']}")