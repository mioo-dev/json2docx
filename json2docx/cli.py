import json
import argparse
from .core import render_docx


def main():
    parser = argparse.ArgumentParser(description="Render a Word .docx file from a template and JSON data.")
    parser.add_argument("template", help="Path to the input Word template (.docx)")
    parser.add_argument("json_data", help="Path to the JSON file containing replacement data")
    parser.add_argument("output", help="Path to save the output Word file")

    args = parser.parse_args()

    with open(args.json_data, "r", encoding="utf-8") as f:
        data = json.load(f)

    render_docx(args.template, args.output, data)
    print(f"✅ Generated: {args.output}")


if __name__ == "__main__":
    main()