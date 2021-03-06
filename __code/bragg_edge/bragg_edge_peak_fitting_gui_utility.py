import numpy as np


class GuiUtility:

	cell_str_format = "{:.3f}"
	cell_str_format_2 = "{:f}"

	def __init__(self, parent=None):
		self.parent = parent

	def get_tab_selected(self, tab_ui=None):
		tab_index = tab_ui.currentIndex()
		return tab_ui.tabText(tab_index)

	def get_toolbox_selected(self, toolbox_ui=None):
		toolbox_index = toolbox_ui.currentIndex()
		return toolbox_ui.itemText(toolbox_index)

	def update_kropff_high_tof_table_ui(self, row=0, a0=None, b0=None, a0_error=None, b0_error=None):
		table_ui = self.parent.ui.high_tof_tableWidget
		table_ui.item(row, 1).setText(self.cell_str_format.format(a0))
		table_ui.item(row, 2).setText(self.cell_str_format.format(b0))
		table_ui.item(row, 3).setText(self.cell_str_format.format(a0_error))
		table_ui.item(row, 4).setText(self.cell_str_format.format(b0_error))

	def update_kropff_low_tof_table_ui(self, row=0, ahkl=None, bhkl=None, ahkl_error=None, bhkl_error=None):
		table_ui = self.parent.ui.low_tof_tableWidget
		table_ui.item(row, 1).setText(self.cell_str_format.format(ahkl))
		table_ui.item(row, 2).setText(self.cell_str_format.format(bhkl))
		table_ui.item(row, 3).setText(self.cell_str_format.format(ahkl_error))
		table_ui.item(row, 4).setText(self.cell_str_format.format(bhkl_error))

	def update_kropff_bragg_edge_table_ui(self, row=0, tofhkl=None, tofhkl_error=None,
	                                      tau=None, tau_error=None,
	                                      sigma=None, sigma_error=None):

		tofhkl_error = np.NaN if tofhkl_error is None else tofhkl_error
		tau_error = np.NaN if tau_error is None else tau_error
		sigma_error = np.NaN if sigma_error is None else sigma_error

		table_ui = self.parent.ui.bragg_edge_tableWidget
		table_ui.item(row, 1).setText(self.cell_str_format_2.format(tofhkl))
		table_ui.item(row, 2).setText(self.cell_str_format_2.format(tau))
		table_ui.item(row, 3).setText(self.cell_str_format_2.format(sigma))
		table_ui.item(row, 4).setText(self.cell_str_format_2.format(tofhkl_error))
		table_ui.item(row, 5).setText(self.cell_str_format_2.format(tau_error))
		table_ui.item(row, 6).setText(self.cell_str_format_2.format(sigma_error))

	def check_status_of_kropff_fitting_buttons(self):

		enabled_low_lambda_button = False
		enabled_bragg_peak_button = False

		# can we enabled the low lambda button
		if self.parent.fitting_input_dictionary['rois'][0]['fitting']['kropff']['high']['a0']:
			enabled_low_lambda_button = True

		if self.parent.fitting_input_dictionary['rois'][0]['fitting']['kropff']['low']['ahkl']:
			enabled_bragg_peak_button = True

		self.parent.ui.fit_low_tof_region.setEnabled(enabled_low_lambda_button)
		self.parent.ui.fit_bragg_peak_region.setEnabled(enabled_bragg_peak_button)
