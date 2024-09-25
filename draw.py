import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from types import FunctionType


def draw_a_line(data: pd.DataFrame, kwargs: dict) -> None:
	"""
	为draw函数内部调用的函数。接受两列数据分别作为x、y轴数据，绘制两者的折线图。
	如果你要调用这个函数引擎画图，可以向draw函数传入以下关键字参数：
	:keyword xytext: 传入一个元组，包含从标签向坐标点的x、y轴偏移量，默认值为(40, 0)
	:keyword xydecimal: 传入一个元组，包含标签小数点后的保留位数，默认值为(2, 2)
	"""
	style = {}
	style['xytext'] = kwargs['xytext'] if 'xytext' in kwargs else (40, 0)
	style['xydecimal'] = kwargs['xydecimal'] if 'xydecimal' in kwargs else (2, 2)

	x_label = data.iloc[:, 0].name
	y_label = data.iloc[:, 1].name

	data[x_label] = data[x_label].round(style['xydecimal'][0])
	data[y_label] = data[y_label].round(style['xydecimal'][1])

	# 绘制散点图
	ax = sns.scatterplot(x=x_label, y=y_label, data=data, s=50)

	# 添加坐标标签
	for _, row in data.iterrows():
		ax.annotate(f"({row[x_label]}, {row[y_label]})", (row[x_label], row[y_label]),
					textcoords="offset points", xytext=(40, 0), ha='center')

	# 拟合曲线
	sns.regplot(x=x_label, y=y_label, data=data, scatter=False)


def draw(input_file: str, sheet_name: str, colomns_index: tuple[int] | list[int] = (0, 1),
		 output_file: str = 'output.png',
		 pic_type: FunctionType = draw_a_line, **kwargs) -> None:
	"""
	主画图函数。
	:param input_file: 数据源的文件名，在input文件夹内。
	:param sheet_name: 数据源的工作表名。
	:param colomns_index: 要选取第几列作为图表的数据源，传入一个元组。（索引从0开始）
	:param output_file: 输出图片的文件名，输出在output文件夹内。
	:param pic_type: 传入一个绘图引擎（函数名），指定绘图的样式。默认是 draw_a_line这个函数。
	:param kwargs: 其它参数。
	"""

	df = pd.read_excel('input/' + input_file, sheet_name=sheet_name)
	colomns_index = list(colomns_index)
	df = df.iloc[:, colomns_index]

	font_path = 'resources/times.ttf'
	font_prop = fm.FontProperties(fname=font_path)
	fm.fontManager.addfont(font_path)   # for linux
	sns.set(font=font_prop.get_name())

	# 调用绘图函数
	pic_type(df, kwargs)

	# 保存图像
	plt.savefig('output/' + output_file, dpi=600)

	# 显示图形
	plt.show()


if __name__ == '__main__':
	draw("物理实验1  理想气体实验.xlsx", sheet_name='Sheet1', colomns_index=(0, 2), output_file='output1.png',
		 pic_type=draw_a_line, xydecimal=(1, 4), xytext=(50, 0))
	draw("物理实验1  理想气体实验.xlsx", sheet_name='Sheet2', colomns_index=(1, 2), output_file='output2.png',
		 pic_type=draw_a_line, xydecimal=(2, 2), xytext=(50, 0))
	draw("物理实验1  理想气体实验.xlsx", sheet_name='Sheet3', colomns_index=(1, 2), output_file='output3.png',
		 pic_type=draw_a_line, xydecimal=(2, 1), xytext=(50, 0))
