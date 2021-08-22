This is used by [PyCharm Odoo](https://plugins.jetbrains.com/plugin/13499-odoo) to help PyCharm better understands your Odoo source code.

### Why do you need this stubs for Odoo?

Python is a dynamic language that makes difficult for any IDE to understand and provide a great code completion. For example in Odoo, some automatic fields such as `id`, `create_date`, `create_uid`,... are declared dynamically (https://github.com/odoo/odoo/blob/14.0/odoo/models.py#L450) so PyCharm could not know if they are attributes of model and you might see warnings such as `Unresolved attribute reference` when trying reference them from a recordset. It's the reason why we need stubs for Odoo. The stubs provides additional info to help PyCharm know these attributes and its type, and thereby provides better code completion, navigation and inspection.

### How to use this stubs in PyCharm?

#### 1. Clone and checkout the branch corresponding to the Odoo version

Example, for Odoo 14:
```
git clone -b 14.0 https://github.com/trinhanhngoc/odoo-stubs.git odoo-stubs14
```

#### 2. Attach to your project
First make sure that you attached the Odoo source code (https://github.com/odoo/odoo) to your project window. Open **Settings** > **Project** > **Project Structure**, select Odoo source code and click **Add Content Root** and add odoo-stubs folder:

![Screenshot from 2021-08-16 22-29-17](https://user-images.githubusercontent.com/11208291/129589513-280555ba-c0bc-4f3c-ab8a-218c0d48d685.png)

For custom addons folders, you can attach them as content roots beside Odoo source code or attach them as projects into the same window and setup project dependencies in Settings.
