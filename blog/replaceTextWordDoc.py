from docx import Document

def replaceTextWordDoc(search, replace, path_in, path_out=None):
    document = Document(path_in)
    
    if path_out is None:
        path_out = path_in

    for p in document.paragraphs:
        if search in p.text:
            inline = p.runs
            for i in range(len(inline)):
                if search in inline[i].text:
                    text = inline[i].text.replace(search, replace)
                    inline[i].text = text
                   
    document.save(path_out)