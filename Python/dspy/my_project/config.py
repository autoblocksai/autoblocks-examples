import pydantic
from autoblocks.configs.config import AutoblocksConfig
from autoblocks.configs.models import RemoteConfig


class ConfigValue(pydantic.BaseModel):
    model: str
    max_bootstrapped_demos: int
    max_labeled_demos: int
    max_rounds: int
    max_errors: int


class Config(AutoblocksConfig[ConfigValue]):
    pass


config = Config(
    value=ConfigValue(
        model="gpt-4-turbo",
        max_bootstrapped_demos=4,
        max_labeled_demos=4,
        max_rounds=10,
        max_errors=5,
    ),
)

config.activate_from_remote(
    config=RemoteConfig(
        id="dspy",
        major_version="1",
        minor_version="0",
    ),
    parser=ConfigValue.model_validate,
)
