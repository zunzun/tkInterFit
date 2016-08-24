import time
import reportlab
import reportlab.platypus
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
import reportlab.lib.pagesizes


# from http://code.activestate.com/recipes/576832-improved-reportlab-recipe-for-page-x-of-y/
class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        canvas.Canvas.__init__(self, *args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        """add page info to each page (page x of y)"""
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_number(num_pages)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_page_number(self, page_count):
        self.setFont("Helvetica", 7)
        self.drawRightString(200*mm, 20*mm, "Page %d of %d" % (self._pageNumber, page_count))
        self.drawCentredString(25*mm, 20*mm, 'https://github.com/zunzun/zunzunsite3')


def CreatePDF(inFileAndPathName, inEquation, inGraphList, inTextList, inSourceCodeList):
    pageElements = []

    styles = reportlab.lib.styles.getSampleStyleSheet()

    styles.add(reportlab.lib.styles.ParagraphStyle(name='CenteredBodyText', parent=styles['BodyText'], alignment=reportlab.lib.enums.TA_CENTER))
    styles.add(reportlab.lib.styles.ParagraphStyle(name='SmallCode', parent=styles['Code'], fontSize=6, alignment=reportlab.lib.enums.TA_LEFT)) # 'Code' and wordwrap=CJK causes problems

    myTableStyle = [('ALIGN', (1,1), (-1,-1), 'CENTER'),
                    ('VALIGN', (1,1), (-1,-1), 'MIDDLE')]

    tableRow = ['ZunZunSite3'] # originally included images that are now unused

    table = reportlab.platypus.Table([tableRow], style=myTableStyle)

    pageElements.append(table)

    pageElements.append(reportlab.platypus.XPreformatted('<br/><br/><br/><br/>', styles['CenteredBodyText']))

    pageElements.append(reportlab.platypus.Paragraph(inEquation.GetDisplayName(), styles['CenteredBodyText']))
    pageElements.append(reportlab.platypus.XPreformatted('<br/><br/>', styles['CenteredBodyText']))

    #titleXML = self.pdfTitleHTML.replace('sup>', 'super>').replace('SUP>', 'super>').replace('<br>', '<br/>').replace('<BR>', '<br/>')
    #pageElements.append(reportlab.platypus.Paragraph(titleXML, styles['CenteredBodyText']))

    pageElements.append(reportlab.platypus.XPreformatted('<br/><br/>', styles['CenteredBodyText']))
    pageElements.append(reportlab.platypus.Paragraph(time.asctime(time.localtime()) + ' local server time', styles['CenteredBodyText']))

    pageElements.append(reportlab.platypus.PageBreak())

    # convert HTML tags to reportlab-specific tags
    '''
    titleXML = pdfTitleHTML.replace('sup>', 'super>').replace('SUP>', 'super>').replace('<br>', '<br/>').replace('<BR>', '<br/>')
    pageElements.append(reportlab.platypus.Paragraph(titleXML, styles['CenteredBodyText']))

    pageElements.append(reportlab.platypus.XPreformatted('<br/><br/>', styles['CenteredBodyText']))
    pageElements.append(reportlab.platypus.Paragraph(time.asctime(time.localtime()) + ' local time', styles['CenteredBodyText']))
    '''

    # make a page for each report output, with report name as page header
    tempImageFileName = 'temp.png'
    for report in inGraphList:
        pageElements.append(reportlab.platypus.Paragraph(report[1], styles['CenteredBodyText']))
        pageElements.append(reportlab.platypus.XPreformatted('<br/><br/>', styles['CenteredBodyText']))
        
        # could not get io.BytesIO and ImageReader to work, use file instead
        report[0].savefig(tempImageFileName, format='png')
        im = reportlab.platypus.Image(tempImageFileName)
        im.hAlign = 'CENTER'
        pageElements.append(im)

        pageElements.append(reportlab.platypus.PageBreak())
    
    for report in inTextList + inSourceCodeList:
        pageElements.append(reportlab.platypus.Preformatted(report[1], styles['SmallCode']))
        pageElements.append(reportlab.platypus.XPreformatted('<br/><br/><br/>', styles['CenteredBodyText']))

        replacedText = report[1]
        
        if -1 != report[1].find('Coefficients'):
            reportText = reportText.replace('<sup>', '^')
            reportText = reportText.replace('<SUP>', '^')

        replacedText = replacedText.replace('\t', '    ') # convert tabs to four spaces
        replacedText = replacedText.replace('\r\n', '\n')

        rebuiltText = ''
        for line in replacedText.split('\n'):
            if line == '':
                rebuiltText += '\n'
            else:
                if line[0] == '<':
                    splitLine = line.split('>')
                    if len(splitLine) > 1:
                        newLine = splitLine[len(splitLine)-1]
                    else:
                        newLine = ''
                else:
                    newLine = line

                # crude line wrapping
                if len(newLine) > 500:
                    rebuiltText += newLine[:100] + '\n'
                    rebuiltText += newLine[100:200] + '\n'
                    rebuiltText += newLine[200:300] + '\n'
                    rebuiltText += newLine[300:400] + '\n'
                    rebuiltText += newLine[400:500] + '\n'
                    rebuiltText += newLine[500:] + '\n'
                elif len(newLine) > 400:
                    rebuiltText += newLine[:100] + '\n'
                    rebuiltText += newLine[100:200] + '\n'
                    rebuiltText += newLine[200:300] + '\n'
                    rebuiltText += newLine[300:400] + '\n'
                    rebuiltText += newLine[400:] + '\n'
                elif len(newLine) > 300:
                    rebuiltText += newLine[:100] + '\n'
                    rebuiltText += newLine[100:200] + '\n'
                    rebuiltText += newLine[200:300] + '\n'
                    rebuiltText += newLine[300:] + '\n'
                elif len(newLine) > 200:
                    rebuiltText += newLine[:100] + '\n'
                    rebuiltText += newLine[100:200] + '\n'
                    rebuiltText += newLine[200:] + '\n'
                elif len(newLine) > 100:
                    rebuiltText += newLine[:100] + '\n'
                    rebuiltText += newLine[100:] + '\n'
                else:
                    rebuiltText += newLine + '\n'
                    
        pageElements.append(reportlab.platypus.Preformatted(rebuiltText, styles['SmallCode']))

        pageElements.append(reportlab.platypus.PageBreak())
        
    doc = reportlab.platypus.SimpleDocTemplate(inFileAndPathName, pagesize=reportlab.lib.pagesizes.letter)
    doc.build(pageElements, canvasmaker=NumberedCanvas)
