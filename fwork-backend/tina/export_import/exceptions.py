# -*- coding: utf-8 -*-


class TinaImportError(Exception):
    def __init__(self, message, project, errors=[]):
        self.message = message
        self.project = project
        self.errors = errors
