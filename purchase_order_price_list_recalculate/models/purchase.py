# Copyright 2021 M.Kamal Habbaba <habbaba@mkhabbaba.com>
# License LGPL-3 - See http://www.gnu.org/licenses/Lgpl-3.0.html

from odoo import api, fields, models

class PurchaseOrderRecalculation(models.Model):
    _inherit = 'purchase.order'

    @api.onchange('product_qty', 'product_uom')
    def _onchange_quantity(self):
        res = super(PurchaseOrderLine, self)._onchange_quantity()
        if self.order_id.requisition_id:
            for line in self.order_id.requisition_id.line_ids.filtered(lambda l: l.product_id == self.product_id):
                if line.product_uom_id != self.product_uom:
                    self.price_unit = line.product_uom_id._compute_price(
                        line.price_unit, self.product_uom)
                else:
                    self.price_unit = line.price_unit * 2
                break
        return res
