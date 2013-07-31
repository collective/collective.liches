Introduction
============

Make link checking easy with liches_, the Link CHEcker Server.


Usage
======

Configure the access to your liches Linkchecker serser and which content
types will be displayed on your link checker start page in the plone
control panel:

.. image:: https://raw.github.com/collective/collective.liches/master/docs/liches-settings.png


Linkcheckers normally go through your site recursivly which
will result in many pages to be checked several times. The
linkchecker start pages tries to avoid this by giving the
linkchecker_ a page from which every relevant content item can be reached.
Append `@@linkchecker-startpage.html` to your siteroot to view this page.

.. image:: https://raw.github.com/collective/collective.liches/master/docs/linkchecker-startpage.png

append `@@linkchecker-brokenpages.html` to your site root or to any
folder(ish object) in your site. This will show you a view whith links
to all pages with broken links in this path.

.. image:: https://raw.github.com/collective/collective.liches/master/docs/broken-pages-in-site.png

All pages will show you (as long as you are able to edit it) which links
are broken. At the top you see a summary of the links and the result
of the linkcheck. Broken Links are highlighted and underlined in red.

.. image:: https://raw.github.com/collective/collective.liches/master/docs/broken-links-in-page.png


.. _linkchecker: http://wummel.github.io/linkchecker/

.. _liches: https://github.com/cleder/liches
