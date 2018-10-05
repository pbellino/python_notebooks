from ipywidgets import widgets
from IPython.core.display import display
import numpy as np
import ipywe.fileselector

from neutronbraggedge.experiment_handler import *
from neutronbraggedge.braggedge import BraggEdge as BraggEdgeLibrary
from neutronbraggedge.material_handler.retrieve_material_metadata import RetrieveMaterialMetadata
from __code.fileselector import FileSelection


class BraggEdge:

    list_of_elements = ['Fe']

    def __init__(self, working_dir='./'):
        self.working_dir = working_dir

    def exp_setup(self):

        label_width = '15%'
        box1 = widgets.HBox([widgets.Label("Default directory",
                                           layout=widgets.Layout(width=label_width)),
                             widgets.Text(self.working_dir,
                                          layout=widgets.Layout(width='85%'))])

        box2 = widgets.HBox([widgets.Label("dSD (m)",
                                           layout=widgets.Layout(width=label_width)),
                             widgets.Text(str(15.89),
                                          layout=widgets.Layout(width='20%'))])

        box3 = widgets.HBox([widgets.Label("detector offset (microns)",
                                           layout=widgets.Layout(width=label_width)),
                             widgets.Text(str(4200),
                                          layout=widgets.Layout(width='20%'))])

        retrieve_material = RetrieveMaterialMetadata(material='all')
        list_returned = retrieve_material.full_list_material()

        # import pprint
        # pprint.pprint(list_returned)

        box4 = widgets.HBox([widgets.Label("List of elements",
                                           layout=widgets.Layout(width=label_width)),
                             widgets.Text(','.join(self.list_of_elements),
                                          layout=widgets.Layout(width='20%'))])

        box5 = widgets.HBox([widgets.Label("Nbr Bragg Edges",
                                           layout=widgets.Layout(width=label_width)),
                             widgets.Text(str(8),
                                          layout=widgets.Layout(width='20%'))])

        vertical_box = widgets.VBox([box1, box2, box3, box4, box5])
        display(vertical_box)

        self.default_directory_ui = box1.children[1]
        self.dSD_ui = box2.children[1]
        self.detector_offset_ui = box3.children[1]
        self.list_elements_ui = box4.children[1]
        self.nbr_bragg_edges_ui = box5.children[1]

    def list_powder_bragg_edges(self):

        list_of_elements_selected = self.list_elements_ui.value
        list_of_elements = list_of_elements_selected.split(',')

        number_of_bragg_edges = np.int(self.nbr_bragg_edges_ui.value)

        _handler = BraggEdgeLibrary(material=list_of_elements,
                                    number_of_bragg_edges=number_of_bragg_edges)
        bragg_edges = _handler.bragg_edges
        hkl = _handler.hkl

        print(_handler)

    def select_normalized_data_set(self):
        self.o_selection = FileSelection(working_dir=self.working_dir)
        self.o_selection.select_data()

    def load_time_spectra(self, time_spectra_file):
        print(time_spectra_file)

    def select_time_spectra_file(self):
        self.data = self.o_selection.data_dict['sample']

        self.time_spectra_ui = ipywe.fileselector.FileSelectorPanel(instruction='Select Time Spectra File ...',
                                                             start_dir=self.working_dir,
                                                             next=self.load_time_spectra,
                                                             multiple=False)

        self.time_spectra_ui.show()