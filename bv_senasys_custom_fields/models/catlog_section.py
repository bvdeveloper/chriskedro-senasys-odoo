from odoo import api, fields, models, _

class CatlogSection(models.Model):
    _name ='catalog.section'
    _description = "Catalog  Section"
    name = fields.Char(string="Catalog Section",required=True)

class SalePersonList2(models.Model):
    _name ='sales.person.two'
    _description = "Sales Person List2"
    name = fields.Char(string="Name",required=True)

class SalePersonList3(models.Model):
    _name ='sales.person.three'
    _description = "Sales Person List3"
    name = fields.Char(string="Name",required=True)

