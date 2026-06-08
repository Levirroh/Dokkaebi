from enum import Enum
import os
from pathlib import Path
from pydantic import BaseModel, Field


class DatabaseEnum(str, Enum):
    SQLITE = "sqlite"
    MYSQL = "mysql"
    POSTGRES = "postgres"


class ConnectionTypeEnum(str, Enum):
    ONLINE = "online"
    OFFLINE = "offline"


class Font(str, Enum):
    BASIC = "basic"


class ScreenSettings(BaseModel):
    width: int = 80
    height: int = 24
    background_color: str = "black"
    text_color: str = "aqua"
    font: Font = Font.BASIC


class ConnectionSettings(BaseModel):
    database_selected: DatabaseEnum = DatabaseEnum.SQLITE
    database_url: str = ""
    network: str = "local"
    connection_type: ConnectionTypeEnum = ConnectionTypeEnum.OFFLINE
    connected_as: str = ""


class SettingsConfig(BaseModel):
    screen: ScreenSettings = Field(default_factory=ScreenSettings)
    connection: ConnectionSettings = Field(default_factory=ConnectionSettings)
    
    
settings_path = str(Path.cwd()) + "/settings.json"

      
def get_config() -> SettingsConfig:
    json_text = Path(settings_path).read_text(encoding="utf-8")
    return SettingsConfig.model_validate_json(json_text)


def set_config(settings: SettingsConfig) -> None:
    Path(settings_path).write_text(
        settings.model_dump_json(indent=2),
        encoding="utf-8"
    )