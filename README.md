# 📝 json2docx

**json2docx** is a Python library that fills Word `.docx` templates using a dictionary of values.  
It replaces **text placeholders** and **base64-encoded images** (matched via alt text) recursively in paragraphs and tables.

---

## ✅ Features

- 🔤 Replace text placeholders like `{{key}}`
- 🖼 Replace images using base64 data matched by image **Alt Text**
- 🔁 Works recursively inside tables, rows, and cells
- 📄 Supports both `.docx` paragraphs and tables
- 🪄 Easy to integrate in automation and document generation workflows

---

## 📦 Installation & Usage

```bash
pip install json2docx
```

> **Note:** Before using this tool, make sure your `template.docx` file includes placeholders in the form `{{key}}`.  
> For example, use placeholders like `{{name}}`, `{{age}}`, and `{{profile_image}}` in your document.  
> To replace an image, insert a sample image in the DOCX file and set its **alt text** to `{{profile_image}}`.

```python
from json2docx import render_docx

data = {
    "name": "Ali",
    "age": 28,
    "profile_image": "{{image_base64}}"
}

render_docx("template.docx", "output.docx", data)
```
