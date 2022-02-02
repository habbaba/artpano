# Copyright 2021 M.Kamal Habbaba <habbaba@mkhabbaba.com>
# License LGPL-3 - See http://www.gnu.org/licenses/Lgpl-3.0.html

from odoo import api, fields, models

@api.onchange('requisition_id')
def _onchange_price_recalculation(self):
        res = super(PurchaseOrderLine, self)._onchange_requisition_id()
        if self.order_id.requisition_id != order_id.requisition_id:
            for line in self.order_id.requisition_id.line_ids.filtered(lambda l: l.product_id == self.product_id):
                self.price_unit = line.product_uom_id._compute_price(
                        line.price_unit, self.product_uom)
        return res
