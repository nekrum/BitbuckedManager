from bbmanager.api_client.base_class import BitBucketClient
from loguru import logger


class Branch(BitBucketClient):
    def __init__(self, timeout: int = 10):
        super().__init__(timeout=timeout)

    async def get_branch_restrictions(self, repository_name: str):
        url = f"{self.base_url}repositories/{self.workspace_name}/{repository_name}/branch-restrictions"
        await self.ensure_valid_token()
        logger.debug(f"Getting restrinctions for {repository_name} branch's")
        response = await self.client.get(url)
        if response.status_code == 200:
            projects = [
                (
                    item["id"],
                    item["pattern"],
                    [u["nickname"] for u in item["users"]],
                    item["kind"],
                )
                for item in response.json()["values"]
            ]
            return projects

        else:
            logger.error(f"Error in request: {response.text}")

    async def remove_pr_restriction(
        self, repository_name, user_sel, branch: str = "master"
    ):
        url = f"{self.base_url}repositories/{self.workspace_name}/{repository_name}/branch-restrictions"
        restrictions = await self.get_branch_restrictions(repository_name)
        logger.debug(f"Remove restrictions for {user_sel} in branch: {branch}")
        restrictions = [i for i in restrictions if i[2]]
        restrictions = [i for i in restrictions if i[1] == branch]
        restrictions = [i for i in restrictions if i[3] == "restrict_merges"]
        logger.debug(f"Restrictions found {restrictions}")
        restrictions = restrictions[0]
        if restrictions is None:
            logger.error("No restrictions for pull reques")
        is_user = user_sel in restrictions[2]
        if is_user:
            logger.info(
                f"Remove pull request restriction for the user {user_sel} in repository {repository_name}"
            )
            url = f"{url}/{restrictions[0]}"
            response = await self.client.delete(url)
            if response.status_code in [200, 204]:
                logger.info(f"Restriction {restrictions[0]} removed")
                return response

        else:
            logger.info("No restriction found")
