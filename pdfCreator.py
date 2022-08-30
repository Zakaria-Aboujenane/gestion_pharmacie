from reportlab.lib.enums import TA_JUSTIFY,TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,Image
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.lib.units import inch


class PdfCreator :

    def __init__(self,pdfName,myL,totalF):
        self.total = totalF
        self.pdfN = pdfName
        self.list = myL
        self.doc = []
        self.doc .append((Image('pics/logoPh.png', 2.2 * inch, 2.2 * inch)))
        self.doc  = self.addTitle()
        SimpleDocTemplate(self.pdfN, pagesize=letter,
                          rightMargin=12, leftMargin=12,
                          topMargin=12, bottomMargin=6).build(self.addParagraph())
    def addTitle(self):
        self.doc.append(Spacer(1, 20))
        self.doc.append(Paragraph('Pharmacie ZAHM',
                             ParagraphStyle(name='NAme', fontFamily='Helvetica', fontSize=36, alignment=TA_CENTER)))
        self.doc.append(Spacer(1, 50))
        return self.doc

    def addParagraph(self):

        for i in self.list:
            self.doc.append(Paragraph(i))
            self.doc.append(Spacer(1, 12))
        self.addBottomText()
        return self.doc
    def addBottomText(self):
        self.doc.append(Spacer(1, 20))
        self.doc.append(Paragraph('Total : ',
                                  ParagraphStyle(name='NAme', fontFamily='Helvetica', fontSize=20,
                                                 alignment=TA_CENTER)))
        self.doc.append(Paragraph(str(self.total)+" DH",
                                  ParagraphStyle(name='Name', fontFamily='Helvetica', fontSize=36,text_color="red",
                                                 alignment=TA_CENTER)))
        self.doc.append(Spacer(1, 50))
        return self.doc



