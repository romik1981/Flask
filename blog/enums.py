# from enum import Enum, auto


# class EnvType(Enum):
#     development = auto()
#     production = auto()


from enum import Enum


class EnvType(Enum):
    DEVELOPMENT = 'development'
    PRODUCTION = 'production'