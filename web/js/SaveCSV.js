/*
This code is based on
https://github.com/pythongosssss/ComfyUI-Custom-Scripts/blob/main/web/js/showText.js

See credit/credit.md for the full license.
*/

import { app } from "../../../scripts/app.js";
import { ComfyWidgets } from "../../../scripts/widgets.js";

// Displays input text on a node
app.registerExtension({
	name: "HowToSD.SaveCSV",
	async beforeRegisterNodeDef(nodeType, nodeData, app) {
		if (nodeData.name === "PandasSaveCSV") {  // This needs to match NODE_CLASS_MAPPINGS in Python
			function populate(text) {
				// No op as we are not updating the node's UI for now.
			}

			// When the node is executed we will be sent the input text, display this in the widget
			const onExecuted = nodeType.prototype.onExecuted;
			nodeType.prototype.onExecuted = function (message) {
				onExecuted?.apply(this, arguments);
				populate.call(this, message.text);
			};

			const onConfigure = nodeType.prototype.onConfigure;
			nodeType.prototype.onConfigure = function () {
				onConfigure?.apply(this, arguments);
				if (this.widgets_values?.length) {
					populate.call(this, this.widgets_values.slice(+this.widgets_values.length > 1));
				}
			};
		}
	},
});