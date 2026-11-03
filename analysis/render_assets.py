#!/usr/bin/env python3
"""Render the frozen manuscript table cells and regenerated vector figures.

Table cells are frozen authored inputs; numerical claims are cross-checked by
verify.py. No manuscript or author metadata is required or exported.
"""
from pathlib import Path
import csv,json,re,unicodedata,hashlib
from xml.sax.saxutils import escape
import fitz,matplotlib
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4,A3,A2,A1,landscape
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph,Table,TableStyle
ROOT=Path(__file__).resolve().parent.parent
FIGURES={'1': ('Configuration disagreement and later unchanged repeats', 'fig1_floor_vs_configurations'), '2': ('Extracted scores and hypothetical review routing', 'fig2_confidence_collapse'), '3': ('Weighted shares of Government Operations and International Affairs', 'fig3_leading_topic_by_year'), 'A1': ('Per-category F1 spread', 'figA1_per_category_f1_spread'), 'A2': ('Destinations of CAP-disagreeing classification outputs', 'figA2_error_absorption'), 'A3': ('Retained-subset accuracy and hypothetical review across configurations', 'figA3_threshold_curves_all')}

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()

def norm(s): return re.sub(r'\s+','',unicodedata.normalize('NFKC',s))
def fonts():
    folder=Path(matplotlib.get_data_path())/'fonts/ttf'
    for name,file in [('AssetSerif','DejaVuSerif.ttf'),('AssetSerifBold','DejaVuSerif-Bold.ttf')]:
        pdfmetrics.registerFont(TTFont(name,str(folder/file)))
    pdfmetrics.registerFontFamily('AssetSerif',normal='AssetSerif',bold='AssetSerifBold')
    return folder/'DejaVuSerif.ttf'

def table_pdf(path,caption,rows):
    count=len(rows[0]); assert all(len(row)==count for row in rows)
    style=ParagraphStyle('cell',fontName='AssetSerif',fontSize=9.5,leading=12.5,spaceAfter=0)
    heading=ParagraphStyle('heading',fontName='AssetSerifBold',fontSize=12.5,leading=16)
    def para(s,bold=False):
        s=escape(s).replace('\n','<br/>')
        return Paragraph('<b>'+s+'</b>' if bold else s,style)
    title=Paragraph(escape(caption),heading)
    for size in [A4,landscape(A4),landscape(A3),landscape(A2),landscape(A1)]:
        width,height=size;usable=width-56
        weights=[]
        for j in range(count):
            lengths=[len(row[j]) for row in rows]
            weights.append(max(4,min(30,(sum(lengths)/len(lengths))**.65)))
        colwidths=[usable*v/sum(weights) for v in weights]
        if count==3 and all(len(r[1])<12 and len(r[2])<12 for r in rows):colwidths=[usable*.72,usable*.14,usable*.14]
        data=[[para(s,i==0) for s in row] for i,row in enumerate(rows)]
        table=Table(data,colWidths=colwidths,hAlign='LEFT')
        table.setStyle(TableStyle([
            ('VALIGN',(0,0),(-1,-1),'TOP'),('BACKGROUND',(0,0),(-1,0),colors.HexColor('#e9eef2')),
            ('LINEBELOW',(0,0),(-1,0),.7,colors.HexColor('#415161')),
            ('LINEBELOW',(0,1),(-1,-1),.25,colors.HexColor('#ccd2d8')),
            ('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),6),
            ('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6),
        ]))
        tw,th=table.wrap(usable,height);hw,hh=title.wrap(usable,height)
        if th+hh+14<=height-56:break
    else: raise ValueError('Table does not fit at legible font size: '+caption)
    height=th+hh+14+56;size=(width,height)
    c=canvas.Canvas(str(path),pagesize=size,invariant=1,pageCompression=1)
    c.setTitle(caption);c.setAuthor('');title.drawOn(c,28,height-28-hh);table.drawOn(c,28,height-28-hh-14-th)
    c.showPage();c.save()
    return {'page_size_points':list(size),'font_size':9.5,'rows':len(rows),'columns':count}

def figure_pdf(path,source,number,title,font):
    with fitz.open(source) as src:
        assert src.page_count==1
        rect=src[0].rect;width=max(rect.width+36,600);scale=(width-36)/rect.width
        header=55;height=rect.height*scale+header+18
        out=fitz.open();page=out.new_page(width=width,height=height)
        page.insert_font(fontname='AssetTitle',fontfile=str(font))
        free=page.insert_textbox(fitz.Rect(18,10,width-18,header-5),f'Figure {number}. {title}',fontname='AssetTitle',fontsize=12)
        assert free>=0,(number,'title overflow')
        page.show_pdf_page(fitz.Rect(18,header,width-18,height-18),src,0)
        out.set_metadata({'title':f'Figure {number}. {title}'})
        out.save(path,garbage=4,deflate=True,no_new_id=True);out.close()
    return {'source':str(source),'source_sha256':sha(source),'vector_source_preserved':True}

def main():
 out=ROOT/'06_outputs/paper_assets';out.mkdir(parents=True,exist_ok=True);font=fonts()
 for row in json.loads((ROOT/'paper_tables/catalogue.json').read_text()):
  with (ROOT/'paper_tables'/row['file']).open(newline='') as f:cells=list(csv.reader(f))
  table_pdf(out/('Table_'+row['number']+'.pdf'),row['caption'],cells)
 for number,(title,stem) in FIGURES.items():figure_pdf(out/('Figure_'+number+'.pdf'),ROOT/'06_outputs/figures'/(stem+'.pdf'),number,title,font)
 assert len(list(out.glob('*.pdf')))==22
 print('Rendered 16 table and 6 figure PDFs from anonymous inputs.')
if __name__=='__main__':main()
