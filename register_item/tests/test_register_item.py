from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError

class TestRegisterItem(TransactionCase):
    def setUp(self):
        super().setUp()
        self.supplier = self.env['res.partner'].create({'name': 'Supplier 1', 'supplier': True})

    def test_create_valid_item(self):
        item = self.env['register.item'].create({
            'material_code': 'MAT001',
            'material_name': 'Cotton Fabric',
            'material_type': 'cotton',
            'buy_price': 150,
            'supplier_id': self.supplier.id
        })
        self.assertTrue(item.id)

    def test_create_invalid_price(self):
        with self.assertRaises(ValidationError):
            self.env['register.item'].create({
                'material_code': 'MAT002',
                'material_name': 'Jeans Fabric',
                'material_type': 'jeans',
                'buy_price': 50,  # Invalid price
                'supplier_id': self.supplier.id
            })

    def test_update_item(self):
        item = self.env['register.item'].create({
            'material_code': 'MAT003',
            'material_name': 'Fabric Material',
            'material_type': 'fabric',
            'buy_price': 200,
            'supplier_id': self.supplier.id
        })
        item.write({'material_name': 'Updated Fabric'})
        self.assertEqual(item.material_name, 'Updated Fabric')

    def test_delete_item(self):
        item = self.env['register.item'].create({
            'material_code': 'MAT004',
            'material_name': 'Test Material',
            'material_type': 'cotton',
            'buy_price': 150,
            'supplier_id': self.supplier.id
        })
        item.unlink()
        self.assertFalse(self.env['register.item'].search([('id', '=', item.id)]))
