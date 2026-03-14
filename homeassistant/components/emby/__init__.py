"""The Emby integration."""

from __future__ import annotations

from pyemby import EmbyServer

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import (
    CONF_API_KEY,
    CONF_HOST,
    CONF_PORT,
    CONF_SSL,
    EVENT_HOMEASSISTANT_START,
)
from homeassistant.core import Event, HomeAssistant, callback

from .const import PLATFORMS

type EmbyConfigEntry = ConfigEntry[EmbyServer]


async def async_setup_entry(hass: HomeAssistant, entry: EmbyConfigEntry) -> bool:
    """Set up Emby from a config entry."""
    host = entry.data[CONF_HOST]
    key = entry.data[CONF_API_KEY]
    port = entry.data[CONF_PORT]
    ssl = entry.data[CONF_SSL]

    emby = EmbyServer(host, key, port, ssl, hass.loop)
    entry.runtime_data = emby

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    @callback
    def start_emby(event: Event | None = None) -> None:
        """Start Emby connection."""
        emby.start()

    if hass.is_running:
        start_emby()
    else:
        entry.async_on_unload(
            hass.bus.async_listen_once(EVENT_HOMEASSISTANT_START, start_emby)
        )

    entry.async_on_unload(emby.stop)

    return True


async def async_unload_entry(hass: HomeAssistant, entry: EmbyConfigEntry) -> bool:
    """Unload a config entry."""
    return await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
