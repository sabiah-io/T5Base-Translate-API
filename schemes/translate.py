from enum import Enum


class SourceEnum(str, Enum):
    English = "English"
    French = "French"
    Romanian = "Romanian"
    German = "German"


class DestinationEnum(Enum):
    English = "English"
    French = "French"
    Romanian = "Romanian"
    German = "German"
