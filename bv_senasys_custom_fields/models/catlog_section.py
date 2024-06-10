from odoo import api, fields, models, _

class CatlogSection(models.Model):
    _name ='catalog.section'
    _description = "Catalog  Section"
    name = fields.Char(string="Catalog Section",required=True)

    _sql_constraints = [
        ('name_uniq', 'unique(name)', "A Catalog section Already Exist!"),
    ]

    @api.model
    def create(self, vals):
        if 'name' in vals:
            web_category = self.env['product.public.category'].sudo().create({'name': vals['name']})
        return super(CatlogSection, self).create(vals)

    def write(self, vals):
        web_category = self.env['product.public.category'].search([('name', '=', self.name)], limit=1)
        if web_category:
            web_category.sudo().write({'name': vals['name']})
        return super(CatlogSection, self).write(vals)

    def unlink(self):
        for record in self:
            web_category = self.env['product.public.category'].search([('name', '=', record.name)], limit=1)
            if web_category:
                web_category.sudo().unlink()
        return super(CatlogSection, self).unlink()

class SalePersonList2(models.Model):
    _name ='sales.person.two'
    _description = "Sales Person List2"
    name = fields.Char(string="Name",required=True)

class SalePersonList3(models.Model):
    _name ='sales.person.three'
    _description = "Sales Person List3"
    name = fields.Char(string="Name",required=True)
