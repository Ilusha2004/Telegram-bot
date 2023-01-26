from typing import Optional
from dataclasses import dataclass

@dataclass
class TgBot:
    token: str
    admin_id: int
    num_threads: int
    log_file_path: Optional[str]

@dataclass
class Config:
    tg_bot: TgBot
