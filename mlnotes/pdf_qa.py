# AUTOGENERATED! DO NOT EDIT! File to edit: 01_qa_on_pdf.ipynb (unless otherwise specified).

__all__ = ['PDF_DIR_PATH']

# Cell
import os
import pandas as pd
import numpy as np
from haystack.nodes import PDFToTextConverter, PreProcessor
from haystack.utils import convert_files_to_docs, print_answers

PDF_DIR_PATH = os.path.join("data")