/** @odoo-module **/

import { FormLabel } from "@web/views/form/form_label";
import { patch } from "@web/core/utils/patch";
import { evaluateBooleanExpr } from "@web/core/py_js/py";


patch(FormLabel.prototype, {
    setup() {
        super.setup();
    },

    get isRequired() {
        return evaluateBooleanExpr(this.props.fieldInfo.required, this.props.record.evalContextWithVirtualIds);
    },
})


