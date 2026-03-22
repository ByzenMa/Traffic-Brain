# Traffic-Brain

当前仓库包含两个相对独立的子项目：

- `ReID/`：基于 `CRTrack` 数据的行人重识别项目。
- `AI-City-MTMC/`：原始多相机跟踪与聚类代码。

## ReID

`ReID/` 目录已经从原来的 `AI-City-Vehicle-Reid/` 重新整理为独立项目，默认围绕 `CRTrack_In-domain_gt` 数据使用。可参考 `ReID/README.md` 进行数据转换与训练。

## AI-City-MTMC

保留原始多相机关联工具代码，供需要复现实验流程时使用。
