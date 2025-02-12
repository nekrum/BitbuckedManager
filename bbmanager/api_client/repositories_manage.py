from bbmanager.api_client.base_class import BitBucketClient
from loguru import logger


class Repositories(BitBucketClient):
    def __init__(self, timeout: int = 10):
        super().__init__(timeout=timeout)

    async def get_all_repositories(self):
        url = f"{self.base_url}/workspaces/"
        await self.ensure_valid_token()
        logger.debug(f"Getting repositories from {url}")
        response = await self.client.get(url)
        if response.status_code == 200:
            repositories = [
                (i["name"], i["slug"]) for i in response.json().get("values", [])
            ]
            return repositories
        else:
            logger.error(f"Error in request: {response.text}")

    async def create_repository(
        self, workspace_name: str | None, repository_name: str, repository_key: str
    ):
        if workspace_name is None:
            workspace_name = self.workspace_name
        url = f"{self.base_url}repositories/{workspace_name}/{repository_name}"
        await self.ensure_valid_token()
        logger.debug(f"Gettin repositories from {url}")
        response = await self.client.post(url=url)
        await self.close()
        if response.status_code in [200, 201]:
            return response.json()
        else:
            logger.error(f"Error in request: {response.text}")
