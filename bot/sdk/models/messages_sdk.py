# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from abc import ABCMeta
from future.utils import with_metaclass
from .base import Base

class Message_sdk(with_metaclass(ABCMeta, Base)):

    def __init__(self, id=None, **kwargs):
        """__init__ method.

        :param string id: Message ID
        :param kwargs: argument
        """

        super(Message_sdk, self).__init__(**kwargs)

        self.type = None
        self.id = id


class TextMessage(Message_sdk):

    def __init__(self, id=None, text=None, **kwargs):
        """__init__ method.

        :param str id: Message ID
        :param str text: Message text
        :param kwargs: argument
        """

        super(textMessage, self).__init__(id=id, **kwargs)

        self.type = 'text'
        self.text = text

class ImageMessage(Message_sdk):

    def __init__(self, id=None, **kwargs):
        """__init__ method.

        :param str id: Message ID
        :param kwargs:
        """
        super(ImageMessage, self).__init__(id=id, **kwargs)

        self.type = 'image'


class VideoMessage(Message_sdk):

    def __init__(self, id=None, **kwargs):
        """__init__ method.

        :param str id: Message ID
        :param kwargs:
        """
        super(VideoMessage, self).__init__(id=id, **kwargs)

        self.type = 'video'


class AudioMessage(Message_sdk):

    def __init__(self, id=None, **kwargs):
        """__init__ method.

        :param str id: Message ID
        :param kwargs:
        """
        super(AudioMessage, self).__init__(id=id, **kwargs)

        self.type = 'audio'


class LocationMessage(Message_sdk):

    def __init__(self, id=None,
                 title=None,
                 address=None,
                 latitude=None,
                 longitude=None,
                 **kwargs
                 ):
        
        """__init__ method.

        :param str id: Message ID
        :param str title: Title
        :param str address: Address
        :param float latitude: Latitude
        :param float longitude: Longitude
        :param kwargs:
        """
        super(LocationMessage, self).__init__(id=id, **kwargs)

        self.type = 'location'
        self.title = title
        self.address = address
        self.latitude = latitude
        self.longitude = longitude


class StickerMessage(Message_sdk):

    def __init__(self,
                 id=None,
                 package_id=None,
                 sticker_id=None,
                 **kwargs
                 ):
        
        """__init__ method.

        :param str id: Message ID
        :param str package_id: Package ID
        :param str sticker_id: Sticker ID
        :param kwargs:
        """
        super(StickerMessage, self).__init__(id=id, **kwargs)

        self.type = 'sticker'
        self.package_id = package_id
        self.sticker_id = sticker_id
