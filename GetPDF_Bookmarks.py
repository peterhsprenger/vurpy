import PyPDF2
class GetPDFBookmarks(PyPDF2.PdfFileReader):

        def getDestinationPageNumbers(self):
            def _setup_outline_page_ids(outline, _result=None):
                if _result is None:
                    _result = {}
                for obj in outline:
                    if isinstance(obj, PyPDF2.pdf.Destination):
                        _result[(id(obj), obj.title)] = obj.page.idnum
                    elif isinstance(obj, list):
                        _setup_outline_page_ids(obj, _result)
                return _result

            def _setup_page_id_to_num(pages=None, _result=None, _num_pages=None):
                if _result is None:
                    _result = {}
                if pages is None:
                    _num_pages = []
                    pages = self.trailer["/Root"].getObject()["/Pages"].getObject()
                t = pages["/Type"]
                if t == "/Pages":
                    for page in pages["/Kids"]:
                        _result[page.idnum] = len(_num_pages)
                        _setup_page_id_to_num(page.getObject(), _result, _num_pages)
                elif t == "/Page":
                    _num_pages.append(1)
                return _result

            outline_page_ids = _setup_outline_page_ids(self.getOutlines())
            page_id_to_page_numbers = _setup_page_id_to_num()

            result = {}
            for (_, title), page_idnum in outline_page_ids.iteritems():
                result[title] = page_id_to_page_numbers.get(page_idnum, '???')
            return result