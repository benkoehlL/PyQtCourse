from PyQt6.QtWidgets import QMainWindow, QApplication, QFileDialog, \
    QMessageBox, QFontDialog, QColorDialog 
from PyQt6.QtPrintSupport import QPrinter, QPrintDialog, QPrintPreviewDialog
from PyQt6.QtCore import QFileInfo, Qt
from PyQt6.QtGui import QFont, QTextCharFormat
import sys, os
from SaxonQ_Editor import Ui_SaxonQTextEditor


class SaxonQEditorWindow(QMainWindow, Ui_SaxonQTextEditor):
    def __init__(self, directory):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.directory = directory

        self.font = QFont()
        self.font.setBold(False)
        self.font.setItalic(False)
        self.font.setUnderline(False)
        self.actionSave.triggered.connect(self.save_file)
        self.actionNew.triggered.connect(self.new_file)
        self.actionOpen.triggered.connect(self.open_file)
        self.actionPrint.triggered.connect(self.print_file)
        self.actionPreview.triggered.connect(self.preview_dialog)
        self.actionExport_PDF.triggered.connect(self.export_pdf)
        self.actionExit.triggered.connect(self.quit)

        self.actionUndo.triggered.connect(self.textEdit.undo)
        self.actionRedo.triggered.connect(self.textEdit.redo)
        
        self.actionCut.triggered.connect(self.textEdit.cut)
        self.actionPaste.triggered.connect(self.textEdit.paste)
        self.actionCopy.triggered.connect(self.textEdit.copy)

        self.actionBold.setCheckable(True)        
        self.actionBold.triggered.connect(self.make_bold)
        self.actionItalic.setCheckable(True)
        self.actionItalic.triggered.connect(self.make_italic)
        self.actionUnderline.setCheckable(True)
        self.actionUnderline.triggered.connect(self.make_underline)

        self.actionLeft.triggered.connect(self.align_left)
        self.actionRight.triggered.connect(self.align_right)
        self.actionCenter.triggered.connect(self.align_center)
        self.actionJustify.triggered.connect(self.justify)

        self.actionColor.triggered.connect(self.colour_dialog)
        self.actionFont.triggered.connect(self.font_dialog)

        self.actionAbout_App.triggered.connect(self.about)

    def maybe_save(self):
        if not self.textEdit.document().isModified():
            return True
        
        else:
            ret = QMessageBox.warning(self, "Application",
                    "The document has been modified.\n \
                        Do you want to save your changes?",
                    QMessageBox.StandardButton.Save | \
                    QMessageBox.StandardButton.Discard |\
                    QMessageBox.StandardButton.Cancel
                        )
            if ret == QMessageBox.StandardButton.Save:
                return self.save_file()
            
            elif ret == QMessageBox.StandardButton.Cancel:
                return False
            
            else:
                return True

    def new_file(self):
        if self.maybe_save():
            self.textEdit.clear()


    def save_file(self):
        filename = QFileDialog.getSaveFileName(self, "SaveFile")

        if filename[0]:
            f = open(filename[0], 'w')

            with f:
                text = self.textEdit.toPlainText()
                f.write(text)

                QMessageBox.about(self, "Save File", "The file has been saved")

    def open_file(self):
        fname = QFileDialog.getOpenFileName(self, "Open File", self.directory)

        if fname[0]:
            f = open(fname[0], 'r')

            with f:
                data = f.read()
                self.textEdit.setText(data)

    def print_file(self):
        printer = QPrinter(QPrinter.PrinterMode.HighResolution)
        dialog = QPrintDialog(printer)
        if dialog.exec() == QPrintDialog.DialogCode.Accepted:
            self.textEdit.print(printer)

    def preview_dialog(self):
        printer = QPrinter(QPrinter.PrinterMode.HighResolution)
        previewDialog = QPrintPreviewDialog(printer, self)
        previewDialog.paintRequested.connect(self.print_preview)
        previewDialog.exec()

    def print_preview(self, printer):
        self.textEdit.print(printer)

    def export_pdf(self):
        fn, _ = QFileDialog.getSaveFileName(self, "Export PDF", 
                                         "new_file.pdf")
        if fn != "":
            if QFileInfo(fn).suffix() == "" :
                fn += '.pdf'
            printer = QPrinter(QPrinter.PrinterMode.HighResolution)
            printer.setOutputFormat(QPrinter.OutputFormat.PdfFormat)
            printer.setOutputFileName(fn)
            self.textEdit.document().print(printer)

    def quit(self):
        self.close()

    def make_bold(self):
        self.font.setBold(not self.font.bold())
        self.textEdit.setFont(self.font)

    def make_italic(self):
        self.font.setItalic(not self.font.italic())
        self.textEdit.setFont(self.font)

    def make_underline(self):
        self.font.setUnderline(not self.font.underline())
        self.textEdit.setFont(self.font)

    def align_left(self):
        self.textEdit.setAlignment(Qt.AlignmentFlag.AlignLeft)

    def align_right(self):
        self.textEdit.setAlignment(Qt.AlignmentFlag.AlignRight)

    def align_center(self):
        self.textEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def align_left(self):
        self.textEdit.setAlignment(Qt.AlignmentFlag.AlignLeft)

    def justify(self):
        self.textEdit.setAlignment(Qt.AlignmentFlag.AlignJustify)
    
    def font_dialog(self):
        font, ok = QFontDialog.getFont()

        if ok:
            self.textEdit.setFont(font)

    def colour_dialog(self):
        colour = QColorDialog.getColor()

        self.textEdit.setTextColor(colour)

    def about(self):
        QMessageBox.about(self, "About App",
            "This is a simple SaxonQ Texteditor with PyQt6.\n"\
            "Have fun and do not blame yourself for any mistakes.\n"\
            "All is Benjamin Köhler's fault :)")

directory = os.getcwd()
app = QApplication(sys.argv)
Note = SaxonQEditorWindow(directory)
sys.exit(app.exec())