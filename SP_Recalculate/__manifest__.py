# Copyright 2022 M.Kamal Habbaba <habbaba@mkhabbaba.com>
# License LGPL-3 - See http://www.gnu.org/licenses/Lgpl-3.0.html

{
    'name': 'Sale and purchase Price Recalculate',
    'version': '1.0',
    'summary': 'This module updates order lines prices by action button on sales and purchases',
    'description': 'Allows to recompute purchase and sales order lines prices from action menu',
    'author': 'M.Kamal Habbaba',
    'maintainer': 'M.Kamal Habbaba',
    'support': 'habbaba@mkhabbaba.com',
    'sequence': '10',
    'license': 'LGPL-3',
    'images': ['static/description/icon.png'],
    'depends': ['sale', 'sale_management', 'purchase'],
	'data': [
        'view/actions_server.xml'
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
