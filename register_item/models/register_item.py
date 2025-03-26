from odoo import models, fields, api
from odoo.exceptions import ValidationError

class RegisterItem(models.Model):
    _name = 'register.item'
    _description = 'Material Registration'
    _rec_name = 'material_code'

    material_code = fields.Char(string="Material Code", required=True)
    material_name = fields.Char(string="Material Name", required=True)
    material_type = fields.Selection([
        ('fabric', 'Fabric'),
        ('jeans', 'Jeans'),
        ('cotton', 'Cotton'),
    ], string="Material Type", required=True)
    buy_price = fields.Float(string="Material Buy Price", required=True)
    supplier_id = fields.Many2one('res.partner', string="Related Supplier", required=True, domain=[('supplier', '=', True)])

    @api.constrains('buy_price')
    def _check_buy_price(self):
        for record in self:
            if record.buy_price < 100:
                raise ValidationError("Material Buy Price tidak boleh kurang dari 100.")
