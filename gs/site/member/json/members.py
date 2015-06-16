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
from zope.component import createObject
from zope.formlib import form
from gs.auth.token import log_auth_error
from gs.content.form.api.json import SiteEndpoint
from gs.group.member.base import user_member_of_group
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

    @Lazy
    def groups(self):
        FOLDER_TYPES = ['Folder', 'Folder (ordered)']
        groups = getattr(self.context, 'groups')
        retval = [folder
                  for folder in groups.objectValues(FOLDER_TYPES)
                  if folder.getProperty('is_group', False)]
        return retval

    @form.action(label='List', name='list', prefix='',
                 failure='handle_list_failure')
    def handle_get_list(self, action, data):
        '''The form action for the *simple* list

:param action: The button that was clicked.
:param dict data: The form data.'''
        retval = to_json(self.siteMembers.memberIds)
        return retval

    @form.action(label='Groups', name='groups', prefix='',
                 failure='handle_list_failure')
    def handle_get_groups(self, action, data):
        '''The form action for the list of members and their groups

:param action: The button that was clicked.
:param dict data: The form data.'''
        usergroups = []
        for userId in self.siteMembers.memberIds:
            userInfo = createObject('groupserver.UserFromId',
                                    self.context, userId)
            groups = [group.getId()
                      for group in self.groups
                      if user_member_of_group(userInfo, group)]
            u = ''.join((self.siteInfo.url, userInfo.url))
            r = {'id': userInfo.id,
                 'name': userInfo.name,
                 'url': u,
                 'groups': groups}
            usergroups.append(r)

        retval = to_json(usergroups)
        return retval

    def handle_list_failure(self, action, data, errors):
        log_auth_error(self.context, self.request, errors)
        retval = self.build_error_response(action, data, errors)
        return retval
