# -*- coding: utf-8 -*-

from tina.base import throttling


class ImportModeRateThrottle(throttling.UserRateThrottle):
    scope = "import-mode"


class ImportDumpModeRateThrottle(throttling.UserRateThrottle):
    scope = "import-dump-mode"
