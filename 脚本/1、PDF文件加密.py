# PDF文件加密
# pip3 install pikepdf
import pikepdf as pike

def Lock_PDF(pdf_files):
    for file in pdf_files:
        with pike.open(file) as pdf:  
            pdf.save("lock.pdf", encryption=pike.Encryption(owner="cxy", user="123456"))

Lock_PDF(["test.pdf"]) 
