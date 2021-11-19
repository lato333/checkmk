#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

from cmk.gui.i18n import _
from cmk.gui.plugins.wato import (
    CheckParameterRulespecWithItem,
    rulespec_registry,
    RulespecGroupCheckParametersApplications,
)
from cmk.gui.valuespec import Dictionary, Integer, MonitoringState, TextInput, Tuple


def _parameter_valuespec_redis_info_memory():
    return Dictionary(
        elements=[
            (
                "used_memory",
                Tuple(
                    title=_("Total number of bytes allocated by Redis using its allocator"),
                    elements=[
                        Filesize(title=_("Warning at")),
                        Filesize(title=_("Critical at")),
                    ],
                ),
            ),
            (
                "used_memory_rss",
                Tuple(
                    title=_("Number of bytes that Redis allocated as seen by the operating system (a.k.a resident set size)"),
                    elements=[
                        Filesize(title=_("Warning at")),
                        Filesize(title=_("Critical at")),
                    ],
                ),
            ),
            (
                "used_memory_peak",
                Tuple(
                    title=_("Peak memory consumed by Redis"),
                    elements=[
                        Filesize(title=_("Warning at")),
                        Filesize(title=_("Critical at")),
                    ],
                ),
            ),
            (
                "used_memory_overhead",
                Tuple(
                    title=_("The sum in bytes of all overheads that the server allocated for managing its internal data structures"),
                    elements=[
                        Filesize(title=_("Warning at")),
                        Filesize(title=_("Critical at")),
                    ],
                ),
            ),
            (
                "used_memory_dataset",
                Tuple(
                    title=_("The size in bytes of the dataset"),
                    elements=[
                        Filesize(title=_("Warning at")),
                        Filesize(title=_("Critical at")),
                    ],
                ),
            ),
            (
                "used_memory_startup",
                Tuple(
                    title=_("Initial amount of memory consumed by Redis at startup"),
                    elements=[
                        Filesize(title=_("Warning at")),
                        Filesize(title=_("Critical at")),
                    ],
                ),
            ),
            (
                "used_memory_lua",
                Tuple(
                    title=_("Number of bytes used by the Lua engine"),
                    elements=[
                        Filesize(title=_("Warning at")),
                        Filesize(title=_("Critical at")),
                    ],
                ),
            ),
            (
                "used_memory_startup",
                Tuple(
                    title=_("Number of bytes used by cached Lua scripts"),
                    elements=[
                        Filesize(title=_("Warning at")),
                        Filesize(title=_("Critical at")),
                    ],
                ),
            ),
        ],
    )


rulespec_registry.register(
    CheckParameterRulespecWithItem(
        check_group_name="redis_info_memory",
        group=RulespecGroupCheckParametersApplications,
        item_spec=lambda: TextInput(title=_("Redis server name")),
        match_type="dict",
        parameter_valuespec=_parameter_valuespec_redis_info_memory,
        title=lambda: _("Redis memory"),
    )
)
