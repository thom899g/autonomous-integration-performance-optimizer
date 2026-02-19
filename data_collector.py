import logging
from typing import Dict, Any
import aiohttp

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DataCollector:
    def __init__(self):
        self.session = aiohttp.ClientSession()

    async def fetch_metrics(self) -> Dict[str, Any]:
        """Fetches metrics from New Relic and logs from Datadog."""
        try:
            new_relic_data = await self._fetch_new_relic()
            datadog_data = await self._fetch_datadog()
            
            return {
                'new_relic': new_relic_data,
                'datadog': datadog_data
            }
        except Exception as e:
            logger.error(f"Failed to fetch data: {str(e)}")
            raise

    async def _fetch_new_relic(self) -> Dict[str, Any]:
        """Fetches metrics from New Relic."""
        try:
            # Simulated API call
            async with self.session.get('https://api.newrelic.com/metrics') as response:
                data = await response.json()
                logger.info("Fetched New Relic data.")
                return data
        except Exception as e:
            logger.error(f"Failed to fetch New Relic data: {str(e)}")
            raise

    async def _fetch_datadog(self) -> Dict[str, Any]:
        """Fetches logs from Datadog."""
        try:
            # Simulated API call
            async with self.session.get('https://api.datadog.com/logs') as response:
                data = await response.json()
                logger.info("Fetched Datadog data.")
                return data
        except Exception as e:
            logger.error(f"Failed to fetch Datadog data: {str(e)}")
            raise

    def __del__(self):
        """Closes the aiohttp session."""
        self.session.close()