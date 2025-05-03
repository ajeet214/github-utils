from src.config import logger as root_logger
from src.actions.base_action import GitHubAction

logger = root_logger.getChild("workflow_cleaner")


class WorkflowCleaner(GitHubAction):
    def __init__(self, client, workflow_filename=None, max_runs=80, status="completed"):
        super().__init__(client)
        self.workflow_filename = workflow_filename
        self.max_runs = max_runs
        self.status = status

    def _find_workflow_id(self):
        if not self.workflow_filename:
            return None
        workflows = self.client.list_workflows()
        for wf in workflows:
            if wf['path'].endswith(self.workflow_filename):
                return wf['id']
        raise ValueError(f"Workflow file '{self.workflow_filename}' not found.")

    def clean(self):
        wf_id = self._find_workflow_id()
        runs = self.client.list_workflow_runs(workflow_id=wf_id, status=self.status, per_page=self.max_runs)
        logger.info(f"Found {len(runs)} runs to delete.")
        for run in runs:
            run_id = run['id']
            try:
                self.client.delete_workflow_run(run_id)
                logger.info(f"Deleted run {run_id}")
            except Exception:
                logger.warning(f"Failed to delete run {run_id}", exc_info=True)
