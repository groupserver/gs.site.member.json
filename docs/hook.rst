========
Web hook
========

Synopsis
========

``/gs-site-member.json```? :option:`token` =<t> & (:option:`users` | :option:`user_groups`)

Description
===========

The web hook ``gs-site-member.json`` in the *site* context takes
a :option:`token` and returns a JSON_ formatted list of all
users. What is returned depends on the *action*, which is either
:option:`users` or :option:`user_groups`.

Required arguments
==================

.. option:: token=<token>

  The authentication token [#token]_.

The *action* can be one of two values (no value needs to be set,
but the argument must be present):

.. option:: users

  Retrieve a simple list of all the site-members.

.. option:: user_groups

   A complex list of all the site members is returned, along with
   the groups on the site that each person belongs to.

Returns
=======

A list of people that belong to at least one group on the site.

* If the *action* was :option:`users` then a simple list of
  user-identifiers is returned.

* If the :option:`user_groups` then a list of standard
  user-objects will be returned (see `the core web-hook
  documentation`_).

Example
=======

Retrieving a list of user-identifiers.

.. code-block:: console

   $ wget --post-data='token=Fake&users' \
     http://groups.example.com/gs-site-member-list.json

Retrieving a list of profiles for the people that belong to at
least one group on the site:

.. code-block:: console

   $ wget --post-data='token=Falke&user_groups' \
     http://groups.example.com/gs-site-member-list.json

.. _JSON: http://json.org/

.. _the core web-hook documentation:
   http://groupserver.readthedocs.org/en/latest/webhook.html#profile-data

.. [#token] See ``gs.auth.token`` for more information
   <https://github.com/groupserver/gs.auth.token>
