# Official Document Standardizer

一个用于 Codex 的中文行政公文排版 skill。它可以把 Word 稿件和配图整理为统一的行政公文版式，同时保留原文件名与文件格式。

## 能做什么

- A4 纵向页面及标准页边距
- 2 号小标宋标题、3 号仿宋正文和分级标题样式
- 28–32 磅固定行距、首行缩进和双面外侧页码
- 无标题稿件自动使用文件名作为标题
- 图片内容识别后按正文语义插入对应段落
- 图片统一为 16:9，并采用上下型环绕
- 正文少于 200 字且只有一张照片时，将照片放在正文最后
- 输出文件保持原文件名和原扩展名
- 完成前要求逐页渲染检查

## 安装

将仓库克隆到 Codex 的个人 skill 目录：

```powershell
git clone https://github.com/2856801816-art/official-document-standardizer.git "$env:CODEX_HOME\skills\official-document-standardizer"
```

如果没有设置 `CODEX_HOME`，Windows 通常可以安装到：

```powershell
git clone https://github.com/2856801816-art/official-document-standardizer.git "$HOME\.codex\skills\official-document-standardizer"
```

重新打开 Codex 后，使用 `$official-document-standardizer` 调用。

## 使用方法

在对话中提供稿件和照片，例如：

```text
使用 $official-document-standardizer 处理这份稿件和这些照片。
保持原文件名和格式，照片按内容插入相关段落。
```

也可以只处理稿件：

```text
使用 $official-document-standardizer 把这份 Word 稿件整理成标准公文格式。
```

skill 会先识别标题、正文结构和图片内容，再决定排版方式。它不会自行改写稿件事实内容。

## 脚本

安装依赖：

```powershell
python -m pip install -r requirements.txt
```

将图片处理成 16:9：

```powershell
python scripts/prepare_image.py input.jpg output.jpg --mode cover --focus center
```

应用 DOCX 基础版式：

```powershell
python scripts/apply_docx_layout.py input.docx output.docx --source-filename "原文件名.docx"
```

插图时可传入 JSON 计划：

```powershell
python scripts/apply_docx_layout.py input.docx output.docx --image-plan image-plan.json --source-filename "原文件名.docx"
```

插图计划格式见 [references/image-placement.md](references/image-placement.md)。

## 字体说明

本项目不包含 `仿宋_GB2312`、方正小标宋等商业或系统字体文件。请使用操作系统或单位已合法授权的字体。不得从来源不明的网站下载并重新分发字体。

## 目录结构

```text
official-document-standardizer/
├── SKILL.md
├── agents/openai.yaml
├── references/
│   ├── format-spec.md
│   └── image-placement.md
├── scripts/
│   ├── apply_docx_layout.py
│   └── prepare_image.py
└── requirements.txt
```

## 适用边界

- 主要面向中文 Word 公文稿件。
- `.docx` 可直接处理；旧版 `.doc` 需要 Microsoft Word 进行格式往返。
- 自动脚本不能代替图片语义判断和最终视觉检查。
- 各单位如有更具体的公文规范，应以其正式规范为准。

## License

MIT License。字体、用户稿件和照片不在本许可证范围内。

---

English summary: A Codex skill for formatting Chinese official documents and placing 16:9 images according to paragraph semantics. It preserves filenames and formats, adds a filename-derived title when missing, and requires rendered visual QA before delivery.
