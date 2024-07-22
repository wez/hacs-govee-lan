"""Test component setup."""
import pytest

from homeassistant.setup import async_setup_component

from custom_components.govee_lan.const import DOMAIN


@pytest.mark.asyncio
async def test_async_setup(hass):
    """Test the component gets setup."""
    assert await async_setup_component(hass, DOMAIN, {}) is True
