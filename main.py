import pdfquery
import pandas as pd

PDF_FILE = '11140-00-PLT1-R00.pdf'

pdf = pdfquery.PDFQuery(PDF_FILE)
pdf.load()
pdf.tree.write('pdfXML.txt', pretty_print = True)


def pdfscrape(pdf):
    # Extraemos cada campo de manera individual según las coordenadas que este tenga en la hoja del pdf
    elemento            = pdf.pq('LTTextLineHorizontal:overlaps_bbox("195, 735,  243, 745")').text()
    h                   = pdf.pq('LTTextLineHorizontal:overlaps_bbox("48,  686,  300, 696")').text()
    tipo                = pdf.pq('LTTextLineHorizontal:overlaps_bbox("48,  649,  300, 684")').text()
    mediana             = pdf.pq('LTTextLineHorizontal:overlaps_bbox("48,  590,  150, 601")').text()
    cantidad            = pdf.pq('LTTextLineHorizontal:overlaps_bbox("175, 590,  280, 601")').text()
    volumen             = pdf.pq('LTTextLineHorizontal:overlaps_bbox("48,  543,  260, 577")').text()
    total_barras        = pdf.pq('LTTextLineHorizontal:overlaps_bbox("370, 662,  430, 672")').text()
    total_mallas        = pdf.pq('LTTextLineHorizontal:overlaps_bbox("370, 662,  430, 672")').text()
    total_trilogic      = pdf.pq('LTTextLineHorizontal:overlaps_bbox("370, 662,  430, 672")').text()
    peso_total_insertos = pdf.pq('LTTextLineHorizontal:overlaps_bbox("370, 662,  430, 672")').text()
    peso_total_armadura = pdf.pq('LTTextLineHorizontal:overlaps_bbox("370, 662,  430, 672")').text()
# Combined all relevant information into single observation
    page = pd.DataFrame({
                         'elemento': elemento,
                         'h': h,
                         'tipo': tipo,
                         'mediana': mediana,
                         'cantidad': cantidad,
                         'volumen': volumen,
                         'total_barras': total_barras,
                         'total_mallas': total_mallas,
                         'total_trilogic': total_trilogic,
                         'peso_total_insertos': peso_total_insertos,
                         'peso_total_armadura': peso_total_armadura,
                       }, index=[0])
    return(page)