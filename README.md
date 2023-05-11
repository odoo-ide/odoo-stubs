# odoo-stubs

> A stub file is a file containing a skeleton of the public interface of that Python module,
> including classes, variables, functions – and most importantly, their types.
>
> https://mypy.readthedocs.io/en/stable/stubs.html 

By using these stubs, IDEs will provide better code completion,
and static type checkers will provide better reports.
These stubs should be used in conjunction with:
- [PyCharm plugin for Odoo](https://plugins.jetbrains.com/plugin/13499-odoo)
- [Visual Studio Code extension for Odoo](https://marketplace.visualstudio.com/items?itemName=trinhanhngoc.vscode-odoo)

## Usage

### 1. Clone the branch corresponding to the Odoo version

Example, for Odoo 16:
```
git clone -b 16.0 https://github.com/odoo-ide/odoo-stubs.git odoo-stubs16
```

### 2. Configure IDEs

#### PyCharm

First make sure you have attached the [Odoo source code](https://github.com/odoo/odoo)
to your project.
Then open `Settings > Project > Project Structure`,
select the project containing the Odoo source code and click `Add Content Root` to add the odoo-stubs folder.

![PyCharm](images/pycharm.png)

#### Visual Studio Code

Create [`pyrightconfig.json`](https://microsoft.github.io/pyright/#/configuration) in the Odoo source code folder
(should be the root folder of your workspace) with something like the following example:

```json
{
    "stubPath": "path/to/odoo-stubs"
}
```

![VSCode](images/vscode.png)
