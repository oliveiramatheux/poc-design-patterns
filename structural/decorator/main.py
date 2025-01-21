from abc import ABC, abstractmethod
import json


class Converter(ABC):
    @abstractmethod
    def convert(self):
        pass


class BaseConverter(Converter):
    def __init__(self, data):
        self.data = data

    def convert(self):
        return self.data


class JsonDecorator(Converter):
    def __init__(self, converter: Converter):
        self.converter = converter

    def convert(self):
        data = self.converter.convert()
        return json.dumps(data, indent=2)


class XMLDecorator(Converter):
    def __init__(self, converter: Converter):
        self.converter = converter

    def convert(self):
        data = self.converter.convert()

        xml = "<root>"

        for i in data:
            xml += "<item>"
            for j, k in i.items():
                xml += f"<{j}>{k}</{j}>"

            xml += "</item>"

        xml += "</root>"

        return xml


if __name__ == '__main__':
    data = [
        {"test": "test1", "test2": "test3"},
        {"test4": "test5", "test6": "test7"}
    ]

    base_converter = BaseConverter(data)
    json_converter = JsonDecorator(base_converter)
    xml_converter = XMLDecorator(base_converter)

    response_json = json_converter.convert()
    response_xml = xml_converter.convert()

    print('response: ' + str(response_json))
    print('response: ' + str(response_xml))
