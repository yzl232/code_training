# encoding=utf-8
#3.1     Guess how a PDF file is structured
#http://resources.infosecinstitute.com/pdf-file-format-basic-structure/



'''
-- Header: This is the first line of a PDF file and specifies the version number of the used PDF specification which the document uses.

- Body: In the body of the PDF document, there are objects that typically include text streams, images, other multimedia elements, etc. The Body section is used to hold all the document’s data being shown to the user.

- xref Table: This is the cross reference table, which contains contains the references to all the objects in the document. The purpose of a cross reference table is that it allows random access to objects in the file, so we don’t need to read the whole PDF document to locate the particular object. Each object is represented by one entry in the cross reference table, which is always 20 bytes long. Let’s show an example:

'''