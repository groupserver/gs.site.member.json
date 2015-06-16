=======================
``gs.site.member.json``
=======================
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
A JSON list of the members of a GroupServer site
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Author: `Michael JasonSmith`_
:Contact: Michael JasonSmith <mpj17@onlinegroups.net>
:Date: 2015-16-17
:Organization: `GroupServer.org`_
:Copyright: This document is licensed under a
  `Creative Commons Attribution-Share Alike 4.0 International License`_
  by `OnlineGroups.net`_.

.. _Creative Commons Attribution-Share Alike 4.0 International License:
   http://creativecommons.org/licenses/by-sa/4.0/

Introduction
============

In GroupServer, each group belongs to a site. Likewise, each
group-member belongs to a related site-member user-group. This
product provides a `web hook`_ that provides a list of the site
members, in JSON format.

Web hook
========

The web hook ``gs-site-member.json`` in the *site* context takes
a ``token`` as its only argument and returns a JSON formatted
list of all the user-identifiers.

Resources
=========

- Code repository:
  https://github.com/groupserver/gs.site.member.json
- Questions and comments to
  http://groupserver.org/groups/development
- Report bugs at https://redmine.iopen.net/projects/groupserver

.. _GroupServer: http://groupserver.org/
.. _GroupServer.org: http://groupserver.org/
.. _OnlineGroups.Net: https://onlinegroups.net
.. _Michael JasonSmith: http://groupserver.org/p/mpj17
