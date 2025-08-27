# -*- coding: utf-8 -*-
{
    "name": "Form Required Star",
    "version": "18.0.0",
    "summary": "Display a red star (*) before required fields in Odoo forms",
    "description": """
Smart Form Required Star

This module improves Odoo form usability by clearly marking required fields with a red asterisk (*) before the field label.

Features:
- Adds a red star before required form fields
- Maintains spacing for non-required fields to keep alignment consistent
- Works with Odoo native form labels and layouts
- Lightweight front-end patch, no server restart required
- Fully compatible with Odoo 17.0 (and adaptable for 16.0 / 15.0)

Usage:
Once installed, required fields in forms will automatically display a red star. No configuration needed.
    """,
    "category": "User Interface",
    "author": "Chen Han Bin",
    "website": "",
    "support": "jeffreyfirstten@163.com",
    "currency": "EUR",
    "price": 0.0,
    "license": "LGPL-3",
    "depends": [
        "web",
    ],
    "data": [
    ],
    "assets": {
        "web.assets_backend": [
            "chb_form_display_required/static/src/**/*",
        ],
    },
    "images": [
        "static/description/icon.png",
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
}
