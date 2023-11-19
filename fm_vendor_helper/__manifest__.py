# -*- coding: utf-8 -*-

{
    'name'        : 'Vendor Helper',
    'version'     : '16.0.0.1',
    "license"     : "OPL-1",
    'author'      : 'AsifShah S',
    'category'    : 'Sales',
    'website'     : 'asifshah_s@hotmail.com',
    'summary'     : 'Vendor Self-Service Portal',
    'depends'     : ['base','sale','sale_management'],      
    'data'        : [       
                        'security/groups.xml',            
                        'security/ir.model.access.csv',
                        'data/email_template.xml',        
                        'view/vendor_forecast_view.xml',
                        'view/vendor_adjustment_request_view.xml'
                    ],
    "auto_install" : False,
    'installable'  : True,
    'application'  : True,
}
