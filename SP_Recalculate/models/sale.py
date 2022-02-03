# Copyright 2022 M.Kamal Habbaba <habbaba@mkhabbaba.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models

class SalesOrderRecalculation(models.Model):
    _inherit = 'sale.order'

    def _price_recalculation(self):
        """this method use to show the product price according to the sales order price list"""
        if self.partner_id and self.pricelist_id:
            for line in self.order_line:
                product = line.product_id.with_context(
                    lang=line.order_id.partner_id.lang,
                    partner=line.order_id.partner_id,
                    quantity=line.product_uom_qty,
                    date=line.order_id.date_order,
                    pricelist=line.order_id.pricelist_id.id,
                    uom=line.product_uom.id,
                    fiscal_position=line.env.context.get('fiscal_position')
                )
                line.price_unit = self.env['account.tax']._fix_tax_included_price_company(
                    line._get_display_price(product), product.taxes_id, line.tax_id, line.company_id)

    def _discount_recalculation(self):
        """method for the discount price calculation according to the price list"""
        if self.partner_id and self.pricelist_id:
            for line in self.order_line:
                if not (line.product_id and line.product_uom and
                        line.order_id.partner_id and line.order_id.pricelist_id and
                        line.order_id.pricelist_id.discount_policy == 'without_discount' and
                        self.env.user.has_group('product.group_discount_per_so_line')):
                    return
