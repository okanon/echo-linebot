# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from abc import ABCMeta
from future.utils import with_metaclass
from .base import Base


class sendMessage_sdk(with_metaclass(ABCMeta, Base)):

    def __init__(self, **kwargs):
        """__init__ method.
        :param kwargs:
        """
        super(sendMessage_sdk, self).__init__(**kwargs)

        self.type = None


class TextSendMessage(sendMessage_sdk):

    def __init__(self, text=None, **kwargs):
        """__init__ method.
        :param str text: Message text
        :param kwargs:
        """
        super(TextSendMessage, self).__init__(**kwargs)

        self.type = 'text'
        self.text = text


class ImageSendMessage(sendMessage_sdk):

    def __init__(self, original_content_url=None, preview_image_url=None, **kwargs):
        """__init__ method.
        :param str original_content_url: Image URL.
            HTTPS
            JPEG
            Max: 1024 x 1024
            Max: 1 MB
        :param str preview_image_url: Preview image URL
            HTTPS
            JPEG
            Max: 240 x 240
            Max: 1 MB
        :param kwargs:
        """
        super(ImageSendMessage, self).__init__(**kwargs)

        self.type = 'image'
        self.original_content_url = original_content_url
        self.preview_image_url = preview_image_url


class VideoSendMessage(sendMessage_sdk):

    def __init__(self, original_content_url=None, preview_image_url=None, **kwargs):
        """__init__ method.
        :param str original_content_url: URL of video file.
            HTTPS
            mp4
            Less than 1 minute
            Max: 10 MB
        :param str preview_image_url: URL of preview image.
            HTTPS
            JPEG
            Max: 240 x 240
            Max: 1 MB
        :param kwargs:
        """
        super(VideoSendMessage, self).__init__(**kwargs)

        self.type = 'video'
        self.original_content_url = original_content_url
        self.preview_image_url = preview_image_url


class AudioSendMessage(sendMessage_sdk):

    def __init__(self, original_content_url=None, duration=None, **kwargs):
        """__init__ method.

        :param str original_content_url: URL of audio file.
            HTTPS
            m4a
            Less than 1 minute
            Max 10 MB
        :param long duration: Length of audio file (milliseconds).
        :param kwargs:
        """
        super(AudioSendMessage, self).__init__(**kwargs)

        self.type = 'audio'
        self.original_content_url = original_content_url
        self.duration = duration


class LocationSendMessage(sendMessage_sdk):

    def __init__(self, title=None, address=None, latitude=None, longitude=None, **kwargs):
        """__init__ method.

        :param str title: Title
        :param str address: Address
        :param float latitude: Latitude
        :param float longitude: Longitude
        :param kwargs:
        """
        super(LocationSendMessage, self).__init__(**kwargs)

        self.type = 'location'
        self.title = title
        self.address = address
        self.latitude = latitude
        self.longitude = longitude


class StickerSendMessage(sendMessage_sdk):

    def __init__(self, package_id=None, sticker_id=None, **kwargs):
        """__init__ method.

        :param str package_id: Package ID
        :param str sticker_id: Sticker ID
        :param kwargs:
        """
        super(StickerSendMessage, self).__init__(**kwargs)

        self.type = 'sticker'
        self.package_id = package_id
        self.sticker_id = sticker_id
