import pydantic
from autoblocks.configs.config import AutoblocksConfig
from autoblocks.configs.models import RemoteConfig


class ConfigValue(pydantic.BaseModel):
    top_k: int
    similarity_metric: str


class Config(AutoblocksConfig[ConfigValue]):
    pass


config = Config(
    value=ConfigValue(top_k=1, similarity_metric="cosine"),
)


# Usage
config.activate_from_remote(
    config=RemoteConfig(
        id="health-copilot-retrieval", major_version="1", minor_version="latest"
    ),
    parser=ConfigValue.model_validate,
)
