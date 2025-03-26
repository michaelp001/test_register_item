from odoo import http
from odoo.http import request

class RegisterItemController(http.Controller):
    @http.route('/api/register_item', type='json', auth='user', methods=['GET'])
    def get_items(self, material_type=None):
        domain = []
        if material_type:
            domain.append(('material_type', '=', material_type))
        materials = request.env['register.item'].search(domain)
        return materials.read(['material_code', 'material_name', 'material_type', 'buy_price', 'supplier_id'])

    @http.route('/api/register_item/create', type='json', auth='user', methods=['POST'])
    def create_item(self, **kwargs):
        if kwargs.get('buy_price', 0) < 100:
            return {"error": "Material Buy Price tidak boleh kurang dari 100."}
        material = request.env['register.item'].create(kwargs)
        return {"id": material.id, "message": "Material berhasil dibuat"}

    @http.route('/api/register_item/update/<int:item_id>', type='json', auth='user', methods=['PUT'])
    def update_item(self, item_id, **kwargs):
        material = request.env['register.item'].browse(item_id)
        if material.exists():
            material.write(kwargs)
            return {"message": "Material berhasil diperbarui"}
        return {"error": "Material tidak ditemukan"}

    @http.route('/api/register_item/delete/<int:item_id>', type='json', auth='user', methods=['DELETE'])
    def delete_item(self, item_id):
        material = request.env['register.item'].browse(item_id)
        if material.exists():
            material.unlink()
            return {"message": "Material berhasil dihapus"}
        return {"error": "Material tidak ditemukan"}
