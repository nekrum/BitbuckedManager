from bbmanager.api_client.base_class import BitBucketClient
from loguru import logger


class Projects(BitBucketClient):
    def __init__(self, timeout: int = 10):
        super().__init__(timeout=timeout)

    async def get_all_projects(self):
        url = f"{self.base_url}/workspaces/{self.workspace_name}/projects"
        await self.ensure_valid_token()
        logger.debug(f"Getting projects from {url}")
        response = await self.client.get(url)
        if response.status_code == 200:
            projects = [
                (item["name"], item["description"])
                for item in response.json()["values"]
            ]
            return projects

        else:
            logger.error(f"Error in request: {response.text}")

    async def create_project(
        self, proj_name: str, proj_key: str, proj_desc: str | None = None
    ):
        url = f"{self.base_url}workspaces/{self.workspace_name}/projects"

        project_data = {
            "key": proj_key,
            "name": proj_name,
            "description": proj_desc,
            # "links": {"avatar": {"href": "http://i.imgur.com/72tRx4w.gif"}},
            # "is_private": "true",
        }
        logger.debug(f"Getting projects from {url}")
        response = await self.client.post(url=url, data=project_data)
        await self.close()

        if response.status_code in [200, 201]:
            return response.json()
        else:
            logger.error(f"Error in request: {response.text}")
