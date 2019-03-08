# coding: utf-8
from __future__ import unicode_literals

import re

from .common import InfoExtractor
from ..utils import (
    ExtractorError,
    int_or_none,
    try_get,
    url_or_none,
    urlencode_postdata,
)

class NetologyBaseIE(InfoExtractor):
    _NETRC_MACHINE = 'netology'

    def _login(self):
        username, password = self._get_login_info()
        if username is None:
            return

        login_data = self._download_json(
            'https://netology.ru/rest/1/user/login', None,
            note = 'Logging in',
            data = urlencode_postdata({
                'login': username,
                'password': password,
                'remember': 'true'
            }),
            headers = {
                'Origin': 'https://netology.ru',
                'Referer': 'https://netology.ru/?modal=sign_in'
            })
        print login_data

    def _real_initialize(self):
        self._login()

class NetologyIE(NetologyBaseIE):
    _VALID_URL = r'(?:https?://)?(?:www\.)?netology\.ru/.+'

    def _real_extract(self, url):
        return []
