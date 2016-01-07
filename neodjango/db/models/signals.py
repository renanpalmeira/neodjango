from __future__ import absolute_import

from django.dispatch import Signal

node_prepared = Signal()

"""
this signals get when __init__ started and finished
"""
pre_node_init = Signal(providing_args=['instance', ])
post_node_init = Signal(providing_args=['instance', ])

"""
this signals get when Node save started and finished
"""
pre_node_save = Signal(providing_args=['instance', ])
post_node_save = Signal(providing_args=['instance', ])