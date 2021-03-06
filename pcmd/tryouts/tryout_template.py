"""
    tryout_template
    ~~~~~~~
    tryout of a new command called template

    FUNCTIONS
    ~~~~~~~

    CLASSES
    ~~~~~~~
    Template
    TemplateProcessor
"""
# from dataclasses import dataclass not compatible in py - 3.6
from typing import Optional, Tuple


class Template:
    def __init__(self, heading: str, template: str):
        self.__heading = heading
        self.__template = template

    def get(self) -> Tuple[str, str]:
        return (self.__heading, self.__template)

    def __repr__(self):
        return str(self.__dict__)


class TemplateProcessor:
    def __init__(self):
        self.__templates: list[Template] = []

    def __repr__(self):
        return str(self.__dict__)

    def add_template(self, temp: Template) -> None:
        self.__templates.append(temp)

    def find_template(self, header: str) -> Optional[Template]:
        for template in self.__templates:
            if template.get()[0] == header:
                return template
        return None


if __name__ == "__main__":
    t = Template('head', 'ing')
    print(t)
    print(t.get())
    temps = TemplateProcessor()
    temps.add_template(t)
    temps.add_template(Template('x', 'pcmd on the groove!'))
    print(temps)
    print(temps.find_template('x'))
