/*
Almost all of this code was taken from
https://github.com/pythongosssss/ComfyUI-Custom-Scripts/blob/main/web/js/showText.js

See credit/credit.md for the full license.
*/

import { app } from "../../../scripts/app.js";
import { ComfyWidgets } from "../../../scripts/widgets.js";

app.registerExtension({
	name: "HowToSD.ShowText",
	async beforeRegisterNodeDef(nodeType, nodeData, app) {

		// Each node needs to match NODE_CLASS_MAPPINGS in Python
		const targetNodes = [
			"PandasShowText",
			"PandasShowIndex",
			"PandasShowDataFrame",
			"CDAShowInt",
			"CDAShowFloat",
			"NumpyShow",
			"PandasShowSeries",
		]

		const noConvertedFieldNodes = [
			"CDAShowInt",
			"CDAShowFloat",
		]

		if (targetNodes.includes(nodeData.name)) {

			function populate(text) {
				// 'this' is not bound automatically — it's explicitly set via .call() in onExecuted.
				if (this.widgets) {
					// On older frontend versions there is a hidden converted-widget
					// Legacy version: const isConvertedWidget = +!!this.inputs?.[0].widget;
					const hasInputWidget = !!(this.inputs?.[0]?.widget); // Coerce to boolean: true if widget exists
					let isConvertedWidget = hasInputWidget ? 1 : 0;    // Convert boolean to integer (1 or 0)

					if (noConvertedFieldNodes.includes(nodeData.name)){ // Remove all widgets
						isConvertedWidget = 0;
					}

					// Remove all dynamically added widgets, preserving the auto-converted input widget if present
					for (let i = isConvertedWidget; i < this.widgets.length; i++) {
						this.widgets[i].onRemove?.();
					}
					this.widgets.length = isConvertedWidget;
				}

				const v = [...text]; // Shallow copy of text array into v
				// If the first element is empty or undefined, remove it from the array
				if (!v[0]) { 
					v.shift();
				}
				for (let row of v) { // Iterate over v. v can be 1d or 2d.
					if (!(row instanceof Array)) row = [row];
					for (const elem of row) {
						// Create a new STRING widget
						// Use field name like "text_0", "text_1", accounting for existing widgets
						const fieldName = "text_" + (this.widgets?.length ?? 0);
						const w = ComfyWidgets["STRING"](
							this,
							fieldName,
							["STRING", { multiline: true }],
							app).widget;
						w.inputEl.readOnly = true;
						w.inputEl.style.opacity = 0.6;
						w.value = elem;
					}
				}

				/*
					Defer until the next animation frame so all widgets are rendered and layout is stable.
					Then compute the node size needed to fit new content.
					If computeSize underestimates it, use the current node size as the floor to preserve layout.
				*/
				requestAnimationFrame(() => {
					const sz = this.computeSize(); // Compute size based on current widgets

					// Adjust to ensure the node fits its current visual width/height
					if (sz[0] < this.size[0]) sz[0] = this.size[0]; // Fit existing node width
					if (sz[1] < this.size[1]) sz[1] = this.size[1]; // Fit existing node height

					this.onResize?.(sz); // Apply the size adjustment
					app.graph.setDirtyCanvas(true, false); // Trigger a redraw of the canvas
				});
			}

			// **onExecute** setup
			// When the node is executed we will be sent the input text, display this in the widget
			const onExecuted = nodeType.prototype.onExecuted;
			nodeType.prototype.onExecuted = function (message) {
				// Call the original onExecuted handler (if one exists), forwarding all arguments
				onExecuted?.apply(this, arguments);

				// Call our populate function, binding 'this' to the current node
				populate.call(this, message.text);
			};

			// **configure** setup
			const VALUES = Symbol(); // Unique internal key to store widget values
			const configure = nodeType.prototype.configure;

			nodeType.prototype.configure = function () {
				// Store unmodified widget values as they get removed on configure by new frontend
				// This value is applied in onConfigure
				this[VALUES] = arguments[0]?.widgets_values;

				// Call the original configure handler, if it exists
				return configure?.apply(this, arguments);
			};

			// **onConfigure** setup
			// Populate node's widgets using the saved values in Configure
			const onConfigure = nodeType.prototype.onConfigure;
			nodeType.prototype.onConfigure = function () {
				onConfigure?.apply(this, arguments);

				// Read saved widget values
				const widgets_values = this[VALUES];
				if (widgets_values?.length) {
					// In newer frontend there seems to be a delay in creating the initial widget
					requestAnimationFrame(() => {
						// Legacy code
						// populate.call(this,
						//	widgets_values.slice(+(widgets_values.length > 1 && this.inputs?.[0].widget)));

						const hasAutoWidget = widgets_values.length > 1 && this.inputs?.[0]?.widget;
						let startIndex = hasAutoWidget ? 1 : 0;
						if (noConvertedFieldNodes.includes(nodeData.name)){ // Remove all widgets
								startIndex = 0;
						}
						populate.call(this, widgets_values.slice(startIndex));
					});
				}
			};
		}
	},
});
