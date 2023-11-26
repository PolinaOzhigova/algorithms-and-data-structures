import struct
from enum import Enum
import json


class Alignment(Enum):
    HORIZONTAL = 1
    VERTICAL = 2


class Widget():

    def __init__(self, parent):
        self.parent = parent
        self.childrens = []

        if self.parent is not None:
            self.parent.add_children(self)

    def add_children(self, children: "Widget"):
        if children not in self.childrens:
            self.childrens.append(children)

    def to_json(self):
        result_json = {
            "class_name": self.__class__.__name__,
            "children": [child.to_json() for child in self.childrens]
        }
        if isinstance(self, MainWindow):
            result_json["title"] = self.title
        elif isinstance(self, Layout):
            result_json["alignment"] = self.alignment.name
        elif isinstance(self, LineEdit):
            result_json["max_length"] = self.max_length
        elif isinstance(self, ComboBox):
            result_json["items"] = self.items

        return result_json

    @classmethod
    def from_json(cls, data, parent=None):
        class_name = data["class_name"]
        root = None

        if class_name == "MainWindow":
            root = cls(data["title"])
        elif class_name == "Layout":
            alignment = Alignment[data.get("alignment", "HORIZONTAL")]
            root = Layout(parent, alignment)
        elif class_name == "LineEdit":
            max_length = data.get("max_length", 10)
            root = LineEdit(parent, max_length)
        elif class_name == "ComboBox":
            items = data.get("items", [])
            root = ComboBox(parent, items)

        for child_data in data.get("children", []):
            child_node = cls.from_json(child_data, parent=root)
            root.add_children(child_node)

        return root

    def __str__(self):
        return f"{self.__class__.__name__}{self.childrens}"

    def __repr__(self):
        return str(self)


class MainWindow(Widget):

    def __init__(self, title: str):
        super().__init__(None)
        self.title = title


class Layout(Widget):

    def __init__(self, parent, alignment: Alignment):
        super().__init__(parent)
        self.alignment = alignment


class LineEdit(Widget):

    def __init__(self, parent, max_length: int = 10):
        super().__init__(parent)
        self.max_length = max_length


class ComboBox(Widget):

    def __init__(self, parent, items):
        super().__init__(parent)
        self.items = items


app = MainWindow("Application")
layout1 = Layout(app, Alignment.HORIZONTAL)
layout2 = Layout(app, Alignment.VERTICAL)

edit1 = LineEdit(layout1, 20)
edit2 = LineEdit(layout1, 30)

box1 = ComboBox(layout2, [1, 2, 3, 4])
box2 = ComboBox(layout2, ["a", "b", "c"])

print(app)

app1 = app.to_json()
print(app1)

app2 = MainWindow.from_json(app1)
print(app2)

if str(app) == str(app2):
    print("Good job")