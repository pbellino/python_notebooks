from IPython.core.display import HTML
import os
import random
import numpy as np
from IPython.display import display
import pyqtgraph as pg
from qtpy.QtWidgets import QMainWindow
from qtpy import QtGui, QtCore

from neutronbraggedge.experiment_handler import *

from __code.bragg_edge.bragg_edge_normalization import BraggEdge as BraggEdgeParent
from __code.bragg_edge.peak_fitting_interface_initialization import Initialization
from __code.bragg_edge.bragg_edge_peak_fitting_gui_utility import GuiUtility
from __code import load_ui
from __code.utilities import find_nearest_index


DEBUGGING = True


class BraggEdge(BraggEdgeParent):
   pass


class Interface(QMainWindow):

    bragg_edge_range = [5, 20]
    roi_settings = {'color': [62, 13, 244],
                    'width': 0.01,
                    'position': [10, 10]}
    _color = QtGui.QColor(roi_settings['color'][0],
                          roi_settings['color'][1],
                          roi_settings['color'][2])
    image_size = {'width': None,
                  'height': None}
    roi_id = None

    def __init__(self, parent=None, o_norm=None, spectra_file=None):

        self.o_norm = o_norm
        self.spectra_file = spectra_file

        display(HTML('<span style="font-size: 20px; color:blue">Check UI that poped up \
            (maybe hidden behind this browser!)</span>'))

        super(Interface, self).__init__(parent)
        ui_full_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
                                    os.path.join('ui',
                                                 'ui_bragg_edge_peak_fitting.ui'))

        self.ui = load_ui(ui_full_path, baseinstance=self)
        self.setWindowTitle("Peak Fitting Tool")

        # initialization
        o_init = Initialization(parent=self)
        o_init.display(image=self.get_live_image())
        self.load_time_spectra()
        self.roi_moved()

    def load_time_spectra(self):
        self.tof_handler = TOF(filename=self.spectra_file)
        self.update_time_spectra()

    def update_time_spectra(self):
        _exp = Experiment(tof=self.tof_handler.tof_array,
                          distance_source_detector_m=np.float(self.ui.distance_detector_sample.text()),
                          detector_offset_micros=np.float(self.ui.detector_offset.text()))
        self.lambda_array = _exp.lambda_array * 1e10  # to be in Angstroms
        self.tof_array = self.tof_handler.tof_array

    def get_live_image(self):
        if DEBUGGING:
            final_array = self.o_norm.data['sample']['data']
        else:
            nbr_data_to_use = np.int(self.number_of_data_to_use_ui.value)

            _data = self.o_norm.data['sample']['data']

            nbr_images = len(_data)
            list_of_indexes_to_keep = random.sample(list(range(nbr_images)), nbr_data_to_use)

            final_array = []
            for _index in list_of_indexes_to_keep:
                final_array.append(_data[_index])

        final_image = np.mean(final_array, axis=0)
        self.final_image = final_image
        return final_image

    @staticmethod
    def check_size(x_axis=None, y_axis=None):
        size_x = len(x_axis)
        size_y = len(y_axis)
        min_len = np.min([size_x, size_y])
        return x_axis[:min_len], y_axis[:min_len]

    def roi_moved(self):
        self.update_selection_profile_plot()

    def get_x_axis(self):
        o_gui = GuiUtility(parent=self)
        tab_selected = o_gui.get_tab_selected().lower()

        x_axis_choice_ui = {'selection': {'index': self.ui.selection_index_radiobutton,
                                          'tof': self.ui.selection_tof_radiobutton,
                                          'lambda': self.ui.selection_lambda_radiobutton},
                            'fitting': {'index': self.ui.fitting_index_radiobutton,
                                        'tof': self.ui.fitting_tof_radiobutton,
                                        'lambda': self.ui.fitting_lambda_radiobutton},
                            }

        list_ui = x_axis_choice_ui[tab_selected]

        if list_ui['index'].isChecked():
            return self.get_specified_x_axis(xaxis='index')
        elif list_ui['tof'].isChecked():
            return self.get_specified_x_axis(xaxis='tof')
        else:
            return self.get_specified_x_axis(xaxis='lambda')

    def get_specified_x_axis(self, xaxis='index'):
        if xaxis == 'index':
            return np.arange(len(self.o_norm.data['sample']['file_name'])), "File index"
        elif xaxis == 'tof':
            return self.tof_array * 1e6, u"TOF (\u00B5s)"   # microS
        elif xaxis == 'lambda':
            return self.lambda_array, u"\u03BB (\u212B)"
        else:
            raise NotImplementedError

    def get_all_x_axis(self):
        all_x_axis = {'index': self.get_specified_x_axis(xaxis='index'),
                      'tof': self.get_specified_x_axis(xaxis='tof'),
                      'lambda': self.get_specified_x_axis(xaxis='lambda')}
        return all_x_axis

    def update_selection_profile_plot(self):
        profile = self.get_profile_of_roi()

        x_axis, x_axis_label = self.get_x_axis()
        
        x_axis, y_axis = Interface.check_size(x_axis=x_axis,
                                              y_axis=profile)

        self.ui.profile.clear()
        self.ui.profile.plot(x_axis, y_axis)
        self.ui.profile.setLabel("bottom", x_axis_label)
        self.ui.profile.setLabel("left", 'Mean counts')

        bragg_edge_range = [x_axis[self.bragg_edge_range[0]],
                            x_axis[self.bragg_edge_range[1]]]

        self.bragg_edge_range_ui = pg.LinearRegionItem(values=bragg_edge_range,
                                                       orientation=None,
                                                       brush=None,
                                                       movable=True,
                                                       bounds=None)
        self.bragg_edge_range_ui.sigRegionChanged.connect(self.bragg_edge_range_changed)
        self.bragg_edge_range_ui.setZValue(-10)
        self.ui.profile.addItem(self.bragg_edge_range_ui)

    def bragg_edge_range_changed(self):
        [left_range, right_range] = list(self.bragg_edge_range_ui.getRegion())
        x_axis, _ = self.get_x_axis()

        left_index = find_nearest_index(array=x_axis, value=left_range)
        right_index = find_nearest_index(array=x_axis, value=right_range)

        self.bragg_edge_range = [left_index, right_index]

    def get_profile_of_roi(self):
        roi_id = self.roi_id
        region = roi_id.getArraySlice(self.final_image,
                                      self.ui.image_view.imageItem)
        x0 = region[0][0].start
        x1 = region[0][0].stop
        y0 = region[0][1].start
        y1 = region[0][1].stop

        profile_value = []
        for _image in self.o_norm.data['sample']['data']:
            _value = np.mean(_image[y0:y1, x0:x1])
            profile_value.append(_value)

        return profile_value

    # event handler
    def selection_roi_size_changed(self, new_value):
        if self.roi_id is None:
            return
        self.ui.roi_size_value.setText(str(new_value))

        region = self.roi_id.getArraySlice(self.final_image, self.ui.image_view.imageItem)

        x0 = region[0][0].start
        y0 = region[0][1].start

        # remove old one
        self.ui.image_view.removeItem(self.roi_id)

        _color = QtGui.QColor(self.roi_settings['color'][0],
                              self.roi_settings['color'][1],
                              self.roi_settings['color'][2])

        _pen = QtGui.QPen()
        _pen.setColor(_color)
        _pen.setWidth(self.roi_settings['width'])
        self.roi_id = pg.ROI([x0, y0],
                             [new_value, new_value],
                             pen=_pen,
                             scaleSnap=True)
        self.ui.image_view.addItem(self.roi_id)
        self.roi_id.sigRegionChanged.connect(self.roi_moved)
        self.update_selection_profile_plot()

    def distance_detector_sample_changed(self):
        self.update_time_spectra()
        self.update_selection_profile_plot()

    def detector_offset_changed(self):
        self.update_time_spectra()
        self.update_selection_profile_plot()

    def selection_axis_changed(self):
        self.update_selection_profile_plot()

    def fitting_axis_changed(self):
        self.update_selection_profile_plot()

    def fit_that_selection_pushed(self):
        [left_range, right_range] = self.bragg_edge_range
        profile = self.get_profile_of_roi()

        yaxis = profile[left_range: right_range]

        all_x_axis = self.get_all_x_axis()
        index_array  = all_x_axis['index'][0]
        tof_array    = all_x_axis['tof'][0]
        lambda_array = all_x_axis['lambda'][0]

        index_selected = index_array[left_range: right_range]
        tof_selected = tof_array[left_range: right_range]
        lambda_selected = lambda_array[left_range: right_range]

        profile_to_fit = {'yaxis': yaxis,
                          'xaxis': {'index': index_selected,
                                    'tof': tof_selected,
                                    'lambda': lambda_selected},
                          }

        import pprint
        pprint.pprint(profile_to_fit)




    def cancel_clicked(self):
        self.close()

    def apply_clicked(self):
        # FIXME
        self.close()
