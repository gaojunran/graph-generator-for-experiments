# 大物实验图表脚本
## 简介
一个简洁的Python脚本，导入一个包含源数据的Excel表格，一行代码即可生成精美的图表！

## 使用说明
1. 将项目文件夹下载到本地。在`input`文件夹中放入一个Excel表格，表格允许的结构如下：
   1. 第一行是列名，在图表中将作为x、y轴的标签名。
   2. 允许放置多列（包括无用数据列）。
2. 在项目根目录运行`pip install -r requirements.txt`，如果运行失败需要手动安装以下依赖库：
   ```text
   matplotlib==3.8.3
   pandas==2.0.2
   openpyxl==3.1.2
   seaborn==0.13.2
   ```
3. 打开`draw.py`，你可以在`if __name__ == '__main__':`下，根据示例和函数说明调用函数生成图表，也可以在其它Python文件中导入`draw.py`，示例：
   ```python
   import draw
   draw.draw(...)  # 按代码示例传入参数 
   ```
   
## 其它
作者欢迎大家的建议哦！欢迎来issue里提意见！