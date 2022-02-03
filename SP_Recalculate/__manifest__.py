# Copyright 2022 M.Kamal Habbaba <habbaba@mkhabbaba.com>
# License LGPL-3 - See http://www.gnu.org/licenses/Lgpl-3.0.html

{
    'name': 'Sale and purchase Price Recalculate',
    'version': '13.0',
    'summary': 'This module updates order lines prices in Sales and Purchases when pricelist / vendor / agreement changed in the form',
    'description': 'Allows to recompute purchase lines from action menu and sales order line price according to the price list onchanage.',
    'category': 'Sales','Purchase Management',
    'author': 'M.Kamal Habbaba',
    'website': 'www.linkedin.com/in/manishkumarbohra',
    'maintainer': 'M.Kamal Habbaba',
    'support': 'habbaba@mkhabbaba.com',
    'sequence': '10',
    'license': 'LGPL-3',
    'images': ['static/description/pricelist.gif'],
    'depends': ['sale', 'sale_management', 'purchase'],
	'data': [
        'view/actions_server.xml'
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
