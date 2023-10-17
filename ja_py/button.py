import pathlib
import anywidget
import traitlets
import os


DIR_PATH = os.path.dirname(os.path.realpath(__file__))

ESM = os.path.join(os.path.abspath(os.path.join(DIR_PATH, "..")), "ja-fe/dist/Button.js")
CSS = ""  # ("styles.css").read_text()


class Button(anywidget.AnyWidget):
    _esm = ESM
    _css = CSS
    on_click = traitlets.Bool().tag(sync=True)
    label = traitlets.Unicode("").tag(sync=True)
    props = traitlets.Dict({}).tag(sync=True)

    # on_click function's first argv is required
    # eg:
    #     def handle_click(change):
    #         do something
    #     Button("test", handle_click)
    # props ref: https://ant.design/components/button-cn#api
    def __init__(self, label="", on_click=lambda x: x, props={}):
        super(Button, self).__init__()
        self.label = label
        self.props = props
        self.observe(on_click, names='on_click')
