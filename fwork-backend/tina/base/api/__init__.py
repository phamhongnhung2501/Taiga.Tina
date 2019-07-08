# -*- coding: utf-8 -*-


VERSION = "2.3.13-tina" # Based on django-resframework 2.3.13

# Header encoding (see RFC5987)
HTTP_HEADER_ENCODING = 'iso-8859-1'

# Default datetime input and output formats
ISO_8601 = 'iso-8601'


from .viewsets import ModelListViewSet
from .viewsets import ModelCrudViewSet
from .viewsets import ModelUpdateRetrieveViewSet
from .viewsets import GenericViewSet
from .viewsets import ReadOnlyListViewSet
from .viewsets import ModelRetrieveViewSet

__all__ = ["ModelCrudViewSet",
           "ModelListViewSet",
           "ModelUpdateRetrieveViewSet",
           "GenericViewSet",
           "ReadOnlyListViewSet",
           "ModelRetrieveViewSet"]
