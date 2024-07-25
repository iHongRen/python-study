# 获取PDF文件所用全部字体
# pip3 install pdfplumber

import pdfplumber

def getPDFonts(pdf_file):
    all_fonts = set()
    with pdfplumber.open(pdf_file) as pdf:
        num_pages = len(pdf.pages)
        for page_num in range(num_pages):
            page = pdf.pages[page_num]
            lines = page.extract_text_lines()
            for line in lines:
                chars = line['chars']
                for char in chars:
                    font = char['fontname']
                    all_fonts.add(font)

    return all_fonts


if __name__ == '__main__':
    fonts = getPDFonts('test.pdf')
    print("所有使用的字体:")
    for font in fonts:
        print(font)

    # XEKKFX+SimHei
    # YWSWBG+MicrosoftYaHei-Bold
    # LNUHNF+SimSun
    # KCHSKM+SegoePrint-Bold
    # YMVEVT+MicrosoftYaHei
    # VMBCQV+ArialMT
    # SYPQXA+SegoePrint
