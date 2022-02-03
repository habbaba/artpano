---------------------------------
sale_order_price_list_recalcualte
---------------------------------


This module add onchange method on sale order:

* Order line recalculation according to the customer and price list using onchange method.

Allows to recompute purchase lines clicking on `Purchase recalculation` entry in purchase action button

Some use cases where this module can be useful:

- product tax have been updated
- price definition have been updated (vendor prices)

And you may want your order reflect these modifications

All recomputed data have traceability in chatter

**Table of contents**

Installation:
-------------

There are thre depended modules sale,sale_management and purchases.

Usage:
------

In the sale order, you can onchange customer and price list to recalculation 
of your order line and losing the previous custom prices in the order line.

Authors:
--------
* M.Kamal Habbaba

Developer:
----------
* M.Kamal Habbaba <habbaba@mkhabbaba.com>

