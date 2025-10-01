"""Configuration file for model settings"""
import os

from camel.models import ModelFactory, BaseModelBackend
from camel.types import ModelType, ModelPlatformType

# Model Configuration 
# for more information on the models, see https://github.com/camel-ai/camel/blob/master/camel/types/enums.py

PLATFORM_TYPE = "azure"

#openrouter url
#URL = "https://openrouter.ai/api/v1"

Azure_key = os.getenv("AZURE_KEY")

MODEL_TYPE = "gpt-4.1-mini-2025-04-14"
# MODEL_TYPE_THINK = "O3_MINI"
# MODEL_TYPE_MANAGE = "O3_MINI"
# MODEL_TYPE_VIDEO = "O3_MINI"

# MODEL_TYPE_PLANNING = "GPT_4O_MINI"
MODEL_TYPE_WORKER = "gpt-4.1-mini-2025-04-14"
MODEL_TYPE_WEB = "gpt-4.1-mini-2025-04-14"
MODEL_TYPE_WEB_PLANNING = "o4-mini"
MODEL_TYPE_IMAGE = "gpt-4.1-mini-2025-04-14"
MODEL_TYPE_AUDIO = "o4-mini"

# Model Settings
MODEL_CONFIG = {
    "temperature": 0,
    "frequency_penalty": 0,
    "top_p": 0.99,
    #"max_tokens": 128000,
}

# PLANNING_MODEL_CONFIG = {
#     "temperature": 0,
#     "frequency_penalty": 0,
#     "top_p": 0.99,
#     #"max_tokens": 128000,
# }

WORKER_MODEL_CONFIG = {
    "temperature": 0,
    "frequency_penalty": 0,
    "top_p": 0.99,
    # "max_tokens": 1600,
}

WEB_MODEL_CONFIG = {
    "temperature": 0,
    "frequency_penalty": 0,
    "top_p": 0.99,
    #"max_tokens": 127000,
}

WEB_PLANNING_MODEL_CONFIG = {
    #"max_tokens": 200000,
}

IMAGE_MODEL_CONFIG = {
    "temperature": 0,
    "frequency_penalty": 0,
    "top_p": 0.99,
    #"max_tokens": 60000,
}

AUDIO_MODEL_CONFIG = {
    #"max_tokens": 60000,
}

# Agent Settings
MESSAGE_WINDOW_SIZE = None
TOKEN_LIMIT = None

# PLANNING_MESSAGE_WINDOW_SIZE = 4096 * 50
# PLANNING_TOKEN_LIMIT = 60000

# IMAGE_MESSAGE_WINDOW_SIZE = 4096 * 50
# IMAGE_TOKEN_LIMIT = 128000

# AUDIO_MESSAGE_WINDOW_SIZE = 4096 * 50
# AUDIO_TOKEN_LIMIT = 200000


def get_model() -> BaseModelBackend:
    """Get the model for general tasks."""
    return ModelFactory.create(
        model_platform=PLATFORM_TYPE,
        model_type=MODEL_TYPE,
        url = "https://newmodels.openai.azure.com/openai/deployments/gpt-4.1-mini/chat/completions?api-version=2025-01-01-preview",
        api_key=Azure_key,  # Set your API key if needed
        api_version="2025-01-01-preview",
        azure_deployment_name="gpt-4.1-mini",
        model_config_dict=MODEL_CONFIG
    )

# def get_planning_model() -> BaseModelBackend:
#     """Get the model for planning assistant."""
#     return ModelFactory.create(
#         model_platform=ModelPlatformType[PLATFORM_TYPE],
#         model_type=ModelType[MODEL_TYPE_PLANNING],
#         url = "https://openrouter.ai/api/v1",
#         api_key=os.getenv("OPENROUTER_API_KEY"),  # Set your API key if needed
#         model_config_dict=PLANNING_MODEL_CONFIG
#     )

def get_worker_model() -> BaseModelBackend:
    """Get the model for worker agent."""
    return ModelFactory.create(
        model_platform=PLATFORM_TYPE,
        model_type=MODEL_TYPE_WORKER,
        url = "https://newmodels.openai.azure.com/openai/deployments/gpt-4.1-mini/chat/completions?api-version=2025-01-01-preview",
        api_key=Azure_key,  # Set your API key if needed
        api_version="2025-01-01-preview",
        azure_deployment_name="gpt-4.1-mini",
        model_config_dict=WORKER_MODEL_CONFIG
    )

def get_reasoning_worker_model() -> BaseModelBackend:
    """Get the model for worker agent."""
    return ModelFactory.create(
        model_platform=PLATFORM_TYPE,
        model_type=MODEL_TYPE_WEB_PLANNING,
        url = "https://newmodels.openai.azure.com/openai/deployments/o4-mini/chat/completions?api-version=2025-01-01-preview",
        api_key=Azure_key,  # Set your API key if needed
        api_version="2025-01-01-preview",
        azure_deployment_name="o4-mini",
        model_config_dict=WEB_PLANNING_MODEL_CONFIG
    )

def get_web_model() -> BaseModelBackend:
    """Get the model for worker agent."""
    return ModelFactory.create(
        model_platform=PLATFORM_TYPE,
        model_type=MODEL_TYPE_WEB,
        url = "https://newmodels.openai.azure.com/openai/deployments/gpt-4.1-mini/chat/completions?api-version=2025-01-01-preview",
        api_key=Azure_key,  # Set your API key if needed
        api_version="2025-01-01-preview",
        azure_deployment_name="gpt-4.1-mini",
        model_config_dict=WEB_MODEL_CONFIG
    )

def get_web_planning_model() -> BaseModelBackend:
    """Get the model for worker agent."""
    return ModelFactory.create(
        model_platform=PLATFORM_TYPE,
        model_type=MODEL_TYPE_WEB_PLANNING,
        url = "https://newmodels.openai.azure.com/openai/deployments/o4-mini/chat/completions?api-version=2025-01-01-preview",
        api_key=Azure_key,  # Set your API key if needed
        api_version="2025-01-01-preview",
        azure_deployment_name="o4-mini",
        model_config_dict=WEB_PLANNING_MODEL_CONFIG
    )

def get_image_model() -> BaseModelBackend:
    """Get the model for worker agent."""
    return ModelFactory.create(
        model_platform=PLATFORM_TYPE,
        model_type=MODEL_TYPE_IMAGE,
        url = "https://newmodels.openai.azure.com/openai/deployments/gpt-4.1-mini/chat/completions?api-version=2025-01-01-preview",
        api_key=Azure_key,  # Set your API key if needed
        api_version="2025-01-01-preview",
        azure_deployment_name="gpt-4.1-mini",
        model_config_dict=IMAGE_MODEL_CONFIG
    )

def get_audio_model() -> BaseModelBackend:
    """Get the model for worker agent."""
    return ModelFactory.create(
        model_platform=PLATFORM_TYPE,
        model_type=MODEL_TYPE_AUDIO,
        url = "https://newmodels.openai.azure.com/openai/deployments/o4-mini/chat/completions?api-version=2025-01-01-preview",
        api_key=Azure_key,  # Set your API key if needed
        api_version="2025-01-01-preview",
        azure_deployment_name="o4-mini",
        model_config_dict=AUDIO_MODEL_CONFIG
    )







