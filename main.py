import pdfquery
import pandas as pd

PDF_FILE = '11140-00-PLT1-R00.pdf'

pdf = pdfquery.PDFQuery(PDF_FILE)
pdf.load()
pdf.tree.write('pdfXML.txt', pretty_print = True)


def pdfscrape(pdf):
    # Extraemos cada campo de manera individual según las coordenadas que este tenga en la hoja del pdf
    elemento            = pdf.pq('LTTextLineHorizontal:overlaps_bbox("109.12, 808.925, 127.798, 816.484")').text()
    h                   = pdf.pq('LTTextLineHorizontal:overlaps_bbox("167.084, 808.925, 180.977, 816.484")').text()
    tipo                = pdf.pq('LTTextLineHorizontal:overlaps_bbox("148.528, 808.925, 162.255, 816.484")').text()
    medida              = pdf.pq('LTTextLineHorizontal:overlaps_bbox("49.57, 761.182, 61.458, 766.851")').text()
    cantidad            = pdf.pq('LTTextLineHorizontal:overlaps_bbox("69.734, 761.182, 72.376, 766.851")').text()
    volumen             = pdf.pq('LTTextLineHorizontal:overlaps_bbox("116.752, 761.182, 125.998, 766.851")').text()
    total_barras        = pdf.pq('LTTextLineHorizontal:overlaps_bbox("211.461, 176.345, 227.153, 183.828")').text()
    total_mallas        = pdf.pq('LTTextLineHorizontal:overlaps_bbox("213.201, 116.477, 228.893, 123.96")').text()
    total_trilogic      = pdf.pq('LTTextLineHorizontal:overlaps_bbox("210.537, 63.157, 226.229, 70.64")').text()
    peso_total_insertos = pdf.pq('LTTextLineHorizontal:overlaps_bbox("211.458, 53.803, 223.663, 61.286")').text()
    peso_total_armadura = pdf.pq('LTTextLineHorizontal:overlaps_bbox("144.198, 44.916, 235.974, 52.867")').text()
    
    # Combinamos toda la información en un data frame
    page = pd.DataFrame({
                         'elemento': elemento,
                         'h': h,
                         'tipo': tipo,
                         'medida': mediana,
                         'cantidad': cantidad,
                         'volumen': volumen,
                         'total_barras': total_barras,
                         'total_mallas': total_mallas,
                         'total_trilogic': total_trilogic,
                         'peso_total_insertos': peso_total_insertos,
                         'peso_total_armadura': peso_total_armadura,
                       }, index=[0])
    return(page)