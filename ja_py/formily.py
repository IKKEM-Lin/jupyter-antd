import anywidget
import traitlets
import os
from ._contant import PARENT_DIR_PATH

ESM = os.path.join(PARENT_DIR_PATH, f"ja_fe{os.sep}dist{os.sep}Formily.js")
CSS = os.path.join(PARENT_DIR_PATH, f"ja_fe{os.sep}dist{os.sep}Formily.css")


default_schema = {
  "type": "object",
  "properties": {
      "example": {
        "type": "string",
        "title": "Example",
        "x-decorator": "FormItem",
        "x-component": "Input",
        "x-validator": [],
        "x-component-props": {},
        "x-decorator-props": {},
        "x-designable-id": "cgp0vw9a874",
        "x-index": 0,
        "name": "example"
      },
      "tip": {
        "type": "string",
        "x-component": "Text",
        "x-component-props": {
          "content": "可以前往：https://designable-antd.formilyjs.org/ 设计表单，并获取JSON schema",
          "style": {
            "margin": "0px 0px 0px 0px",
            "display": "flex",
            "justifyContent": "center"
          }
        },
        "x-designable-id": "tucchh62ask",
        "x-index": 1
      }
  }
}

class Formily(anywidget.AnyWidget):
    _esm = ESM
    _css = CSS

    # generate schema from https://designable-antd.formilyjs.org/
    schema = traitlets.Dict({}).tag(sync=True)
    value = traitlets.Dict({}).tag(sync=True)
    options = traitlets.Dict({
        "show_modal": True,
        "ok_label": "Update",
        "cancel_label": "Cancel",
        "ok_props": {},
        "cancel_props": {},
    }).tag(sync=True)
    
    # variable for custom file selector
    os_sep= traitlets.Unicode(os.sep).tag(sync=True)
    pwd = traitlets.Unicode("").tag(sync=True)
    files = traitlets.List([]).tag(sync=True)
    msg = traitlets.Dict({"content": ""}).tag(sync=True) # use for error msg action

    def __init__(self, schema = default_schema, options = {}):
        super(Formily, self).__init__()
        self.value = {"default": 1}
        self.schema = schema
        self.options = {**self.options, **options}

        self.pwd = os.getcwd()
        self._get_files()
        self.observe(self._get_files, names='pwd')
    
    def _get_files(self, change = ""):
        path = self.pwd
        try:
            files = os.listdir(path)
        except PermissionError as e:
            self.msg = {"content": str(e), "type": "error"}
            self.pwd = os.path.dirname(self.pwd)
            return
        files = [{"name": file, "isDir":  os.path.isdir(os.path.join(path, file))} for file in files]
        files.sort(key=lambda item: item["isDir"], reverse=True)
        self.files = files
