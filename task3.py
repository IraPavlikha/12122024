def format_csv(func):
    def wrapper(*args, **kwargs):
        data = func(*args, **kwargs)
        csv_output = "\n".join(",".join(map(str, row)) for row in data)
        return csv_output
    return wrapper

def format_json(func):
    def wrapper(*args, **kwargs):
        import json
        data = func(*args, **kwargs)
        json_output = json.dumps(data, indent=4)
        return json_output
    return wrapper

def format_xml(func):
    def wrapper(*args, **kwargs):
        data = func(*args, **kwargs)
        xml_output = "<report>\n"
        for row in data:
            xml_output += "  <entry>\n"
            for i, value in enumerate(row):
                xml_output += f"    <field{i}>{value}</field{i}>\n"
            xml_output += "  </entry>\n"
        xml_output += "</report>"
        return xml_output
    return wrapper

@format_csv
@format_json
@format_xml
def generate_report():
    return [
        ["Year", "Income", "Expenses", "Profit"],
        [2023, 100000, 50000, 50000],
        [2024, 150000, 70000, 80000]
    ]
try:
    print("Оберіть формат звітності (csv, json, xml):")
    report_format = input("> ").strip().lower()
    if report_format == "csv":
        print("CSV формат звітності:")
        print(format_csv(generate_report)())
    elif report_format == "json":
        print("JSON формат звітності:")
        print(format_json(generate_report)())
    elif report_format == "xml":
        print("XML формат звітності:")
        print(format_xml(generate_report)())
    else:
        print("Невідомий формат. Будь ласка, оберіть csv, json або xml.")
except Exception as e:
    print(f"Сталася помилка: {e}")
