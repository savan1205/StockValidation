{
    "name": "stock_validation",
    "version": "15.0.1.0.1",
    "summary": "Stock's Lot/Serial Confirmation",
    "sequence": 1,
    "description": """
        This module contains all the features of Stock's Lot/Serial Confirmation before validating in Stock Picking.
    """,
    "depends": ["sale_management","stock"],
    "data": [
        "security/ir.model.access.csv",
        "wizard/wizard_sp_lots_serial_views.xml",
        "views/stock_picking_views.xml",


    ],
    "demo": [],
    "installable": True,
    "application": True,
    "auto_install": False,
    "license": "LGPL-3",
}
