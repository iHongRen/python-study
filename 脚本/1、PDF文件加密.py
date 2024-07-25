# PDF文件加密
# pip3 install pikepdf

import pikepdf as pike

# 默认加密密码为 123456
def encryptionPDF(pdf_files, key="123456"):
    for file in pdf_files:
        with pike.open(file) as pdf:  
            pdf.save("lock.pdf", encryption=pike.Encryption(owner="cxy", user=key))


if __name__ == '__main__' :
    encryptionPDF(["test.pdf"]) 


