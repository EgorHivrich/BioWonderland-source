import json, telebot.types
from json import loads, JSONDecoder, dumps

from .types import *

class JsonConfigDeserializer (JSONDecoder):

    def decode (self,
               s,  _w = json.decoder.WHITESPACE.match
    ) -> Config:

        obj = super().decode(s, _w)
        decodedConfig: Config = Config(obj["token"], {},)

        objects: dict = obj["objects"]

        for key in objects.keys():
            if isinstance(objects[key], list):
                decodedConfig.objects[key] = [ objects[key][0], telebot.types.InlineKeyboardMarkup.de_json(dumps(objects[key][1])) ]

            decodedConfig.__dict__[key] = objects[key]

        return decodedConfig # ready for inspection sir
    