"""
fixture impor
"""

import os
from unittest.mock import AsyncMock, ANY, patch
from io import BytesIO
import pytest
from PIL import Image
from src.lib.lib import *

@pytest.fixture
def update_context_fixture():
    """
    fixture
    """
    update_mock = AsyncMock()
    context_mock = AsyncMock()
    return update_mock, context_mock
