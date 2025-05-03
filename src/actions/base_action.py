from abc import ABC, abstractmethod


class GitHubAction(ABC):
    def __init__(self, client):
        self.client = client

    @abstractmethod
    def clean(self):
        """Execute the action."""
        pass