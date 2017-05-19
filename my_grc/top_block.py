#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Fri May 19 22:17:00 2017
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import numpy
import ruiy
import sip
import sys
from gnuradio import qtgui


class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.variable_qtgui_range_3 = variable_qtgui_range_3 = 0
        self.variable_qtgui_range_2 = variable_qtgui_range_2 = 0
        self.variable_qtgui_range_1 = variable_qtgui_range_1 = 0
        self.variable_qtgui_range_0 = variable_qtgui_range_0 = 0
        self.samp_rate = samp_rate = 1e7

        ##################################################
        # Blocks
        ##################################################
        self._variable_qtgui_range_3_range = Range(-100, 100, 1, 0, 200)
        self._variable_qtgui_range_3_win = RangeWidget(self._variable_qtgui_range_3_range, self.set_variable_qtgui_range_3, 'DC_Q', "counter_slider", float)
        self.top_layout.addWidget(self._variable_qtgui_range_3_win)
        self._variable_qtgui_range_2_range = Range(-100, 100, 1, 0, 200)
        self._variable_qtgui_range_2_win = RangeWidget(self._variable_qtgui_range_2_range, self.set_variable_qtgui_range_2, 'DC_I', "counter_slider", float)
        self.top_layout.addWidget(self._variable_qtgui_range_2_win)
        self._variable_qtgui_range_1_range = Range(0, 180, 1, 0, 200)
        self._variable_qtgui_range_1_win = RangeWidget(self._variable_qtgui_range_1_range, self.set_variable_qtgui_range_1, 'theta', "counter_slider", int)
        self.top_layout.addWidget(self._variable_qtgui_range_1_win)
        self._variable_qtgui_range_0_range = Range(0, 100, 1, 0, 200)
        self._variable_qtgui_range_0_win = RangeWidget(self._variable_qtgui_range_0_range, self.set_variable_qtgui_range_0, 'mag', "counter_slider", int)
        self.top_layout.addWidget(self._variable_qtgui_range_0_win)
        self.ruiy_nonlinear_0 = ruiy.nonlinear(True)
        self.ruiy_mul_mod_0 = ruiy.mul_mod("qpsk", "gray", True, 0.35, 1, 0.35, False, False, 2)
        self.ruiy_iqbal_gen_3_0_0 = ruiy.iqbal_gen_3_0(variable_qtgui_range_0, variable_qtgui_range_1, variable_qtgui_range_2, variable_qtgui_range_3)
        self.ruiy_carrier_offset_0 = ruiy.carrier_offset(0)
        self.qtgui_const_sink_x_0 = qtgui.const_sink_c(
        	1024, #size
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0.enable_grid(False)
        self.qtgui_const_sink_x_0.enable_axis_labels(True)

        if not True:
          self.qtgui_const_sink_x_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_const_sink_x_0_win)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.analog_random_source_x_0 = blocks.vector_source_b(map(int, numpy.random.randint(0, 2, int(1e7))), True)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_random_source_x_0, 0), (self.ruiy_mul_mod_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_const_sink_x_0, 0))
        self.connect((self.ruiy_carrier_offset_0, 0), (self.ruiy_nonlinear_0, 0))
        self.connect((self.ruiy_iqbal_gen_3_0_0, 0), (self.ruiy_carrier_offset_0, 0))
        self.connect((self.ruiy_mul_mod_0, 0), (self.ruiy_iqbal_gen_3_0_0, 0))
        self.connect((self.ruiy_nonlinear_0, 0), (self.blocks_throttle_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_variable_qtgui_range_3(self):
        return self.variable_qtgui_range_3

    def set_variable_qtgui_range_3(self, variable_qtgui_range_3):
        self.variable_qtgui_range_3 = variable_qtgui_range_3
        self.ruiy_iqbal_gen_3_0_0.set_dc_q(self.variable_qtgui_range_3)

    def get_variable_qtgui_range_2(self):
        return self.variable_qtgui_range_2

    def set_variable_qtgui_range_2(self, variable_qtgui_range_2):
        self.variable_qtgui_range_2 = variable_qtgui_range_2
        self.ruiy_iqbal_gen_3_0_0.set_dc_i(self.variable_qtgui_range_2)

    def get_variable_qtgui_range_1(self):
        return self.variable_qtgui_range_1

    def set_variable_qtgui_range_1(self, variable_qtgui_range_1):
        self.variable_qtgui_range_1 = variable_qtgui_range_1
        self.ruiy_iqbal_gen_3_0_0.set_theta(self.variable_qtgui_range_1)

    def get_variable_qtgui_range_0(self):
        return self.variable_qtgui_range_0

    def set_variable_qtgui_range_0(self, variable_qtgui_range_0):
        self.variable_qtgui_range_0 = variable_qtgui_range_0
        self.ruiy_iqbal_gen_3_0_0.set_mag(self.variable_qtgui_range_0)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)


def main(top_block_cls=top_block, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
