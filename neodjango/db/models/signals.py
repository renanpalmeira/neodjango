from __future__ import absolute_import

from django.dispatch import Signal

node_prepared = Signal()
pre_node_init = Signal(providing_args=['instance', ])