from odoo import models, fields


class WizardLotsSerial(models.TransientModel):
    _name = "wizard.lots.serial"
    _description = "wizard.lots.serial"

    lots_ids = fields.Html(readonly=True, string=" ")

    def default_get(self, fields):
        """Defaultly gets/fills data(product with its Lots/Serial number)
            based on active stock picking lines"""
        res = super(WizardLotsSerial, self).default_get(fields)
        picking_id = self.env['stock.picking'].browse(self.env.context.get('stock_id'))
        add_string = """<table class='table table-bordered'>  
                            <thead class="thead-dark">
                                <tr>
                                    <th scope="col">Products</th>
                                    <th scope="col">Lot/Serial number</th>
                                </tr>
                            </thead>"""
        product_list = []
        for move_lines in picking_id.move_line_ids_without_package:
            # if move_lines.lot_id:
            if move_lines.lot_id and move_lines.product_id not in product_list:
                product_list.append(move_lines.product_id)
                add_string += """<tr>
                                    <td>""" + move_lines.product_id.name + """</td>""" + """
                                    <td>""" + move_lines.lot_id.name
            else:
                add_string += ",  " + move_lines.lot_id.name
        res.update({
            'lots_ids': add_string,
        })
        return res

    def action_button_validate(self):
        return self.env['stock.picking'].browse(self.env.context.get('stock_id')).button_validate()
