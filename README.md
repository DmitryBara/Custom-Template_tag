# Django custom templatetag


___About___

Main purpose of this project - create application module 'menu' which could be connected in django project by template tag.
Admin of site have opportunity to CRUD menu items and customize it from standard django admin.

__Technologies__
Django, AJAX, Javascript, JQuery


___Run___
This repository include application 'menu' and all standard django project.
So you could easy run it on you localhost by command `python3 manage.py runserver`.
Django is required to be install.


___Settings___

Adding of new menu tables have not userfriendly interface now, so if you wanna add new table you should enter in django admin and create new instances of Menu and MenuElement(foreign key to menu). MenuElement should contain:

`title` - name of this element ('books').

`number` - identificator of current element within one level ('2').

`path` - path from root Menu instance to current element ('3.1.3.2') where 3 is id of Menu.

`url` - adres for requests from client ('/entertaiment/books/shekspir/romeo_and_julietta/').

`is_parent` - bool flag. If have children elements set in true.

In future it's possible to realize creating of new Menu Instances through config loading or make frontend UI interface.
Now you could use ready database (sqlite3) from this repository. There are 2 ready Menu.

Be careful and don't use 2 equal Menu on one template. It will not be work correctly.
