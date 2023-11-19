from odoo import models, fields, api

class VendorForecast(models.Model):
    _name = "vendor.adjustment.request"
    
    #fields definition
    order_id = fields.Many2one('sale.order', string='Order Reference', required=True )
    adjustment_detail = fields.Text(string='Requested Adjustment', required=True)
    comment = fields.Text(string='Additional Comments')

    #function to send automated email notification
    @api.model
    def send_email_notification(self, procurement_order_id):
        order = self.browse(procurement_order_id)
        # Trigger the email sending
        template_id = self.env.ref('fm_vendor_helper.email_template_vendor_request')
        template_id.send_mail(order.id, force_send=True)

    #to sent email notification while creation of a record
    @api.model
    def create(self, vals):
        order = super(VendorForecast, self).create(vals)
        order.send_email_notification(order.id)
        return order
 
    #to sent email notification while a change occurs in the record
    def write(self, vals):
        res = super(VendorForecast, self).write(vals)
        for order in self:
            order.send_email_notification(order.id)
        return res
    
    #function to return the id of the record to the email template to specify which record the notification is about
    def get_record_ref(self):
        ref = self.env.ref('fm_vendor_helper.action_vendor_adjustment_request').id or False
        return ref   
