# Copyright 2021 M.Kamal Habbaba <habbaba@mkhabbaba.com>
# License LGPL-3 - See http://www.gnu.org/licenses/Lgpl-3.0.html

from odoo import api, fields, models

class PurchaseOrderRecalculation(models.Model):
    _inherit = 'purchase.order'

    @api.onchange('requisition_id', 'partner_id')
    def _onchange_price_recalculation(self):
        """this method use to show the product price according to the sales order price list"""
        if self.partner_id and self.requisition_id:
            for line in self.order_line:
                product = line.product_id.with_context(
                    lang=line.order_id.partner_id.lang,
                    partner=line.order_id.partner_id,
                    quantity=line.product_uom_qty,
                    date=line.order_id.date_order,
                    pricelist=line.order_id.pricelist_id.id,
                    uom=line.product_uom.id,
                )
                line.price_unit = self.env['account.tax']._fix_tax_included_price_company(
                    line._get_display_price(product), product.taxes_id, line.tax_id, line.company_id)
