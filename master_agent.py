from typing import Dict, Any
import logging
from fastapi import FastAPI
from modules.data_collector import DataCollector
from modules.processor import DataProcessor
from modules.analyzer import PerformanceAnalyzer
from modules.optimizer import Optimizer
from modules.monitor import SystemMonitor

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class MasterAgent:
    def __init__(self):
        self.app = FastAPI()
        self.data_collector = DataCollector()
        self.processor = DataProcessor()
        self.analyzer = PerformanceAnalyzer()
        self.optimizer = Optimizer()
        self.monitor = SystemMonitor()

    async def collect_data(self) -> Dict[str, Any]:
        """Collects metrics and logs from monitoring tools."""
        try:
            data = await self.data_collector.fetch_metrics()
            logger.info("Collected data successfully.")
            return data
        except Exception as e:
            logger.error(f"Failed to collect data: {str(e)}")
            raise

    async def process_data(self, raw_data: Dict[str, Any]) -> Dict[str, Any]:
        """Processes and structures raw data for analysis."""
        try:
            processed_data = await self.processor.process(raw_data)
            logger.info("Data processing completed.")
            return processed_data
        except Exception as e:
            logger.error(f"Data processing failed: {str(e)}")
            raise

    async def analyze(self, processed_data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyzes data to identify performance issues."""
        try:
            analysis = await self.analyzer.analyze(processed_data)
            logger.info("Analysis completed.")
            return analysis
        except Exception as e:
            logger.error(f"Analysis failed: {str(e)}")
            raise

    async def optimize(self, analysis_results: Dict[str, Any]) -> Dict[str, Any]:
        """Generates optimization recommendations."""
        try:
            optimizations = await self.optimizer.optimize(analysis_results)
            logger.info("Optimization suggestions generated.")
            return optimizations
        except Exception as e:
            logger.error(f"Optimization failed: {str(e)}")
            raise

    async def monitor_system(self) -> None:
        """Monitors the system's health and performance."""
        try:
            await self.monitor.check_health()
            logger.info("System monitoring completed.")
        except Exception as e:
            logger.error(f"Monitoring failed: {str(e)}")
            raise

if __name__ == "__main__":
    master_agent = MasterAgent()