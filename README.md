# cadquery-template

A ready-made template for developing CAD models using [CadQuery](https://github.com/CadQuery/cadquery) in [Codespaces](https://github.com/features/codespaces), a cloud-based developer environment.

This basic template doesn't yet have all the bells and whistles - it's just the minimum to get you started quickly. In the future, it might also support GitHub Actions integration for auto-compiling CAD files.

## Getting Started

1. Create a new repository from this template repo by clicking [**Use this template**](https://github.com/iansan5653/cadquery-template/generate)
2. Create a codespace in that new repository ([docs](https://docs.github.com/en/codespaces/developing-in-codespaces/creating-a-codespace))
    - Your codespace will be automatically configured with Python, CadQuery, and [cadquery-server](https://pypi.org/project/cadquery-server/) for previewing models
3. Run `cq-server run` in a terminal or run the **Start CadQuery Server** task in VSCode
4. The preview server will be available on port `5000` by default. You can open this in your browser or directly inside VSCode by clicking the preview icon in the CadQuery row in the **Ports** tab in the bottom panel
5. Simply create your model using `box.py` as a template. The rendered output will automatically update upon save (enable autosave for totally automatic reloading). You can rename the file - just make sure to keep the `from cq_server.ui import ui, show_object` import and the `show_object` call at the end
