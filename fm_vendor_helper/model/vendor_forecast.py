from odoo import models, fields, api

class VendorForecast(models.Model):
    _name = "vendor.forecast"
    
    #fields definition
    product_id = fields.Many2one('product.product', string='Product Name', required=True )
    expected_quantity = fields.Integer(string='Expected Quantity')
    forecast_date = fields.Date(string="Forecast Date")
