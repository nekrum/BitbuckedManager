from bbmanager.config import Config
from httpx import AsyncClient as Client
from loguru import logger
import dotenv


class BitBucketClient:
    def __init__(self, timeout: int = 10):
        self.config = Config()
        self.base_url = self.config.BB_BASE_URL
        self.workspace_name = self.config.BB_WORKSPACE_NAME
        self.access_token = self.config.BB_ACCES_TOKEN
        self.timeout = timeout
        self.client = self.create_client()

    def create_client(self):
        if self.base_url is not None:
            return Client(
                base_url=self.base_url,
                headers={
                    "Authorization": f"Bearer {self.access_token}",
                    "Accept": "application/json;charset=UTF-8",
                },
                timeout=self.timeout,
            )

    async def ensure_valid_token(self):
        test_url = "https://api.bitbucket.org/2.0/user"
        if self.client is not None:
            response = await self.client.get(test_url)

            if response.status_code == 401:
                logger.info("Token expired, refreshing...")
                self.access_token = await self.refresh_token()
                dot_file = dotenv.find_dotenv()
                dotenv.set_key(dot_file, "BB_ACCESS_TOKEN", self.access_token)
                self.update_client()

    async def refresh_token(self):
        url = "https://bitbucket.org/site/oauth2/access_token"
        auth = (self.config.BB_API_KEY, self.config.BB_API_SECRET)
        data = {
            "grant_type": "refresh_token",
            "refresh_token": self.config.BB_REFRESH_TOKEN,
        }

        async with Client() as client:
            response = await client.post(url, auth=auth, data=data)

            if response.status_code == 200:
                new_token = response.json()["access_token"]
                logger.info("Token refreshed successfully")
                return new_token
            else:
                logger.error(f" Token refresh failed: {response.text}")
                raise Exception(f"Failed to refresh token: {response.text}")

    def update_client(self):
        self.close()
        self.client = self.create_client()

    async def close(self):
        await self.client.aclose()
