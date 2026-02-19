import logging
from typing import Dict, Any
import pandas as pd

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DataProcessor:
    def __init__(self):
        pass

    async def process(self, raw_data: Dict[str, Any]) -> Dict[str, Any]:
        """Processes and structures raw data for analysis."""
        try:
            # Convert raw data into structured format
            df = self._structure_data(raw_data)
            processed_data = {
                'structured': df.to_dict('records'),
                'summary': self._generate_summary(df)
            }
            logger.info("Data processing completed.")
            return processed_data
        except Exception as e:
            logger.error(f"Data processing failed: {str(e)}")
            raise

    def _structure_data(self, raw_data: Dict[str, Any]) -> pd.DataFrame:
        """Structures raw data into a DataFrame."""
        try:
            # Flatten nested structures
            flattened = {}
            for key, value in raw_data.items():
                if isinstance(value, dict):
                    flattened.update({f"{key}__{k}": v for k, v in value.items()})
                else:
                    flattened[key] = value
            df = pd.DataFrame([flattened])
            logger.info("Data structured into DataFrame.")
            return df
        except Exception as e:
            logger.error(f"Failed to structure data: {str(e)}")
            raise

    def _generate_summary(self, df: pd.DataFrame) -> Dict[str, Any]:
        """Generates a summary of the processed data."""
        try:
            summary = {
                'count': len(df),
                'mean_response_time': df['response_time'].mean(),
                'max_error_rate': df['error_rate'].max()
            }
            logger.info("Summary generated.")
            return summary
        except Exception as e:
            logger.error(f"Failed to generate summary: {str(e)}")
            raise