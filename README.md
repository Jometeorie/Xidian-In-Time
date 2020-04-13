# Xidian-In-Time
时间上的西电素材批量生成工具

## 项目概述
本项目为互联网+项目“时间上的西电”的子项目，“时间上的西电”需要我们以时间轴、地理空间全面展示西电的发展历程，生成巨幅时间图谱，约10米长、2米高。本子项目计划为生成的时间图谱提供批量的素材图片。

在此基础上，我们希望将生成素材的子项目做成一个开源工具，以此为更多类似的项目生成需要的图片素材和时间片。

目前，项目处于开源初期，由于前期内容均由个人完成，没有开源的打算，因此部分架构和注释较为凌乱，之后会进一步进行完善，希望多多包涵。

## Demo
### 批量素材生成
目前需要将生成的批量素材以如下两种格式放入Excel表格中，并运行process_excel.py生成批量图片，并可以运行generate_json.py文件将生成的素材按年代和种类分类保存在生成素材中。Excel格式如下：

![](https://github.com/frozenlalala/Xidian-In-Time/raw/master/images/素材生成Excel.png)

![](https://github.com/frozenlalala/Xidian-In-Time/raw/master/images/素材生成Excel2.png)

最终生成素材图片如下：

![](https://github.com/frozenlalala/Xidian-In-Time/raw/master/images/ID1001_Type1_Year1931.png)

![](https://github.com/frozenlalala/Xidian-In-Time/raw/master/images/ID8033_Type8_Year1895.png)

![](https://github.com/frozenlalala/Xidian-In-Time/raw/master/images/ID8159_Type8_Year2019.png)

### 时间片生成
为了导入AI时的需求，该项目也可以为AI提供时间片的素材，目前还没有制作成完整的批量生成工具，界面也需要进一步美观，其效果如下：

![](https://github.com/frozenlalala/Xidian-In-Time/raw/master/images/1790_1800.png)

![](https://github.com/frozenlalala/Xidian-In-Time/raw/master/images/1961.png)

## 总结
目前该开源项目还处于预开源阶段，许多架构和内容尚未完善，今后会尝试将其做成一款更加完备的批量生产素材工具。