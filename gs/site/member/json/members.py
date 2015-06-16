# -*- coding: utf-8 -*-
############################################################################
#
# Copyright © 2015 OnlineGroups.net and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
############################################################################
from __future__ import absolute_import, print_function, unicode_literals
from json import dumps as to_json
from logging import getLogger
log = getLogger('gs.site.member.json.members')
from zope.cachedescriptors.property import Lazy
from zope.formlib import form
from gs.auth.token import log_auth_error
from gs.content.form.api.json import SiteEndpoint
from gs.site.member.base import SiteMembers
from .interfaces import IMembersList


class MembersListHook(SiteEndpoint):
    '''The page removes someone from a group'''
    label = 'List the site members'
    form_fields = form.Fields(IMembersList, render_context=False)

    @Lazy
    def siteMembers(self):
        retval = SiteMembers(self.context)
        return retval

    @form.action(label='List', name='list', prefix='',
                 failure='handle_list_failure')
    def handle_get_list(self, action, data):
        '''The form action for the *simple* list

:param action: The button that was clicked.
:param dict data: The form data.'''
        retval = to_json(self.sitemembers.memberIds)
        return retval

    @form.action(label='Groups', name='groups', prefix='',
                 failure='handle_list_failure')
    def handle_get_groups(self, action, data):
        '''The form action for the list of members and their groups

:param action: The button that was clicked.
:param dict data: The form data.'''
        r = []
        retval = to_json(r)
        return retval

    def handle_list_failure(self, action, data, errors):
        log_auth_error(self.context, self.request, errors)
        retval = self.build_error_response(action, data, errors)
        return retval
