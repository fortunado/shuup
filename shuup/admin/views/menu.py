# -*- coding: utf-8 -*-
# This file is part of Shuup.
#
# Copyright (c) 2012-2016, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the AGPLv3 license found in the
# LICENSE file in the root directory of this source tree.
from django.views.generic import TemplateView


class MenuView(TemplateView):
    template_name = "shuup/admin/base/_main_menu.jinja"
