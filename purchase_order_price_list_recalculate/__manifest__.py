# Copyright 2021 M.Kamal Habbaba <habbaba@mkhabbaba.com>
# License LGPL-3 - See http://www.gnu.org/licenses/Lgpl-3.0.html

{
    'name': 'Purchase Price Recalculate',
    'version': '13.0',
    'summary': 'This module manage to product price list re-calculation',
    'description': 'This module added a new feature related to the re-calculate order line cost according to the price list onchanage.',
    'category': 'purchases',
    'author': 'M.Kamal Habbaba',
    'website': 'www.mkhabbaba.com',
    'maintainer': 'M.Kamal Habbaba',
    'support': 'habbaba@mkhabbaba.com',
    'sequence': '10',
    'license': 'LGPL-3',
    'images': ['static/description/pricelist.gif'],
    'depends': ['purchase', 'purchase_requisition'],
    'installable': True,
    'auto_install': False,
    'application': True,
}
