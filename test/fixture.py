"""
fixture impor
"""

from unittest.mock import AsyncMock

import pytest

@pytest.fixture
def update_context_fixture():
    """
    fixture
    """
    update_mock = AsyncMock()
    context_mock = AsyncMock()
    return update_mock, context_mock
