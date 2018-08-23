# -*- coding: utf-8 -*-
#
#
# Project name: OpenVAS Reporting: A tool to convert OpenVAS XML reports into Excel files.
# Project URL: https://github.com/TheGroundZero/openvas_to_report

"""This file contains data structures"""


class Config(object):
    def __init__(self, input_files, output_file="openvas_report", min_level="none", filetype="xlsx"):
        """
        :param input_files: input file path
        :type input_files: list(str)

        :param output_file: output file path and name
        :type output_file: str

        :param min_level: minimal level to add to output
        :type min_level: str

        :param filetype: output file filetype
        :type filetype: str

        :raises: TypeError, ValueError
        """
        if not isinstance(input_files, list):
            raise TypeError("Expected list, got '{}' instead".format(type(input_files)))
        else:
            for i in input_files:
                if not isinstance(i, str):
                    raise TypeError("Expected basestring, got '{}' instead".format(type(i)))

        if not isinstance(output_file, str):
            raise TypeError("Expected basestring, got '{}' instead".format(type(output_file)))
        if not isinstance(min_level, str):
            raise TypeError("Expected basestring, got '{}' instead".format(type(min_level)))
        if not isinstance(filetype, str):
            raise TypeError("Expected basestring, got '{}' instead".format(type(filetype)))
        else:
            if filetype not in self.filetypes():
                raise ValueError("Filetype not supported, got {}, expecting one of {}".format(filetype,
                                                                                              self.filetypes()))

        self.input_files = input_files
        self.output_file = output_file
        self.min_level = min_level
        self.filetype = filetype

    @staticmethod
    def colors():
        return {
            'blue': '#183868',
            'critical': '#702da0',
            'high': '#c80000',
            'medium': '#ffc000',
            'low': '#00b050',
            'none': '#0070c0',
        }

    @staticmethod
    def levels():
        return {
            'c': 'critical',
            'h': 'high',
            'm': 'medium',
            'l': 'low',
            'n': 'none'
        }

    @staticmethod
    def filetypes():
        return list('xlsx')
