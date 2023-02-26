import camelot
import pandas as pd
import sys
import config

def extract_table_from_pdf(filepath,page):

    if config.border is True:
        "lattice for tables with border lines to separate cells"
        flavor='lattice'
    else:
        "strean for tables with white space to separate cells"
        flavor='stream'

    tables = camelot.read_pdf(filepath,flavor=flavor,pages=str(page))

    output_df = pd.DataFrame()

    if tables._tables:
        print(f" Parsing report -->\n {tables[0].parsing_report}")

        df_output=tables[0].df

    return output_df

if __name__=="__main__":
    page_no=1
    filepath = '/home/harshad/workspace/Table-Extraction-PDF/data/foo.pdf'
    df=extract_table_from_pdf(filepath,1)


