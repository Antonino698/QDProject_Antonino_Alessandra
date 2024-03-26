"""
fixture impor
"""
# pylint: disable=R0914
# pylint: disable=W0104
# pylint: disable=W0401
# pylint: disable=W0401
# pylint: disable=W0611
# pylint: disable=W0612
# pylint: disable=W0613
# pylint: disable=W0614
# pylint: disable=W0621
# pylint: disable=W0718
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