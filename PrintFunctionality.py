import FirebaseFunction
import subprocess

def printPdf(filename):
    print("Yesh")
    p = subprocess.Popen([r"GS\\gsview\\gsprint.exe", f"{filename}"], 
                     stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()
    print(stdout)
    print(stderr)

# ###################################
# Help




def createAndLoadPdf(filename,imageurl,val):
    # ###################################
    # Help
    try:
        
        def drawMyRuler(pdf):
            pdf.drawString(100,810, 'x100')
            pdf.drawString(200,810, 'x200')
            pdf.drawString(300,810, 'x300')
            pdf.drawString(400,810, 'x400')
            pdf.drawString(500,810, 'x500')

            pdf.drawString(10,100, 'y100')
            pdf.drawString(10,200, 'y200')
            pdf.drawString(10,300, 'y300')
            pdf.drawString(10,400, 'y400')
            pdf.drawString(10,500, 'y500')
            pdf.drawString(10,600, 'y600')
            pdf.drawString(10,700, 'y700')
            pdf.drawString(10,800, 'y800')    


    # ###################################
    # Content
        fileName = filename
        documentTitle = 'Document title!'
        title = 'Fined person'
        subTitle = 'Fine Reciept For Not Wearing a mask'

        textLines = [
        'You are detected by our systems & officials that ',
        'you are not wearing  a mask in our premises.You',
        f'are fined with [ RS.{val} ].Here\'s the proof '] 


        image = imageurl

        # ###################################
        # 0) Create document 
        from reportlab.pdfgen import canvas 

        pdf = canvas.Canvas(fileName)
        pdf.setTitle(documentTitle)

        #drawMyRuler(pdf)
        # ###################################
        # 1) Title :: Set fonts 
        # # Print available fonts
        # for font in pdf.getAvailableFonts():
        #     print(font)

        # Register a new font
        from reportlab.pdfbase.ttfonts import TTFont
        from reportlab.pdfbase import pdfmetrics


        # ###################################
        # 2) Sub Title 
        # RGB - Red Green and Blue
        pdf.setFillColorRGB(0, 0, 255)
        pdf.setFont("Courier-Bold", 24)
        pdf.drawCentredString(290,720, subTitle)


        # ###################################
        # 3) Draw a line
        pdf.line(30, 710, 550, 710)

        # ###################################
        # 4) Text object :: for large amounts of text
        from reportlab.lib import colors

        text = pdf.beginText(40, 680)
        text.setFont("Courier", 18)
        text.setFillColor(colors.red)
        for line in textLines:
            text.textLine(line)

        pdf.drawText(text)

        # ###################################
        # 5) Draw a image
        pdf.drawInlineImage(image,130,350, width=(1024/3), height=(720/3))

        pdf.line(30,300, 550, 300)

        textLines1 = [
        'Signature(Authority) _______________________ ',
        '',
        'Recieved by:________________________________',
        '',
        'Reciever\'s Signature:______________________'] 

        from reportlab.lib import colors

        text = pdf.beginText(30, 220)
        text.setFont("Courier", 18)
        text.setFillColor(colors.red)
        for line in textLines1:
            text.textLine(line)

        pdf.drawText(text)

        pdf.save()

        printPdf(filename);
    
    
    except Exception as e:
        print(f"{e} is not defined")