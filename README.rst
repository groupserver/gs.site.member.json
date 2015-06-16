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
a ``token`` as its only argument [#token]_ and returns a JSON
formatted list of all users. What is returned depends on the
*action*, which is either `users`_ or `user_groups`_

``users``
---------

If the action is ``users`` then a simple list of all the
site-members is returned. Each member is represented as a
user-identifier (string).

.. code-block:: console

   $ wget --post-data='token=aFakeToken&users=' \
     http://groups.example.com/gs-site-member-list.json

user_groups
-----------

If the action is ``user_groups`` then a complex list of all the
site members is returned, along with the groups on the site that
each person belongs to.

.. code-block:: console

   $ wget --post-data='token=aFakeToken&user_groups=' \
     http://groups.example.com/gs-site-member-list.json

Return value
~~~~~~~~~~~~

A JSON formatted list is returned. Each member of the list
contains the following values.

``id``:
    The identifier for the site member.

``name``:
    The name of the site member.

``url``:
    The URL of the profile of the site member.

``email``:
  The member's email addresses:

  * ``all``: All the addresses.
  * ``preferred``: The preferred address or addresses.
  * ``unverified``: The unverified addresses.
  * ``other``: The verified addresses that are not preferred.

``groups``:
    A list of groups the member belongs to. Each group is
    represented by its group-identifier.

Example
~~~~~~~

.. code-block:: json

  [
    {
      "id": "qK7SgjsTHcLNrJ2ClevcJ0",
      "name": "A Person"
      "url": "https://groups.example.com/p/aperson",
      "email": {
        "all": [
          "a.person@home.example.com",
          "a.person@work.example.com"
        ],
        "other": [
          "a.person@work.example.com"
        ],
        "preferred": [
          "a.person@home.example.com"
        ],
        "unverified": []
      },
      "groups": [
        "example",
        "test"
      ],
    },
    {
      "id": "HgTvjLrc7ecJNK0JCs2lSq",
      "name": "Another Person"
      "url": "https://groups.example.com/p/HgTvjLrc7ecJNK0JCs2lSq",
      "email": {
        "all": [
          "another_person@home.example.com"
        ],
        "other": [],
        "preferred": [
          "another_person@home.example.com"
        ],
        "unverified": []
      },
      "groups": [
        "example"
      ],
    }
  ]

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

.. [#token] See the ``gs.auth.token`` product
            <https://github.com/groupserver/gs.auth.token>
