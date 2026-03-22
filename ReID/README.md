# ReID

独立的 CRTrack 行人重识别项目代码，仅保留 CRTrack 数据集相关训练与转换能力。

## 项目目标

- 项目目录名固定为 `ReID/`。
- 训练数据统一使用 `CRTrack_In-domain_gt` 转换后的 ReID 数据集。
- 身份标签只从 `ids_with_text_cross_view_selected` 中读取。
- 转换脚本按完整 `scene/clip/view` 层级遍历，既能处理当前示例 2 帧数据，也能处理假设的完整数据集。

## 目录结构

```text
ReID/
├── CRTrack_In-domain_gt/          # 示例 CRTrack 数据
├── data/                          # 转换后的 ReID 训练数据输出目录
├── tools/prepare_crtrack_reid.py  # 数据转换脚本
├── train/                         # 训练代码
└── data.md                        # CRTrack 数据说明
```

## 1. 生成 ReID 数据集

```bash
cd ReID
python3 tools/prepare_crtrack_reid.py \
  --source-root CRTrack_In-domain_gt \
  --output-root data/CRTrack-ReID \
  --split-mode train_query_gallery \
  --overwrite
```

输出目录为：

- `data/CRTrack-ReID/train`
- `data/CRTrack-ReID/query`
- `data/CRTrack-ReID/test`
- `data/CRTrack-ReID/metadata.csv`
- `data/CRTrack-ReID/summary.json`

## 2. 训练

```bash
cd ReID/train
sh run.sh
```

默认训练配置已经切换为 `CRTrack`，并且项目内已去除其他数据集相关注册与入口代码。

## 3. 关键约定

- `View1 / View2 / View3` 分别映射为 `c1 / c2 / c3`。
- 每个 `(scene, clip, csv中的id)` 会被重映射为新的全局 `pid`。
- 生成文件名格式为：`{pid:06d}_c{camid}_{scene}_{clip}_f{frame_id:06d}_lid{local_id:04d}.jpg`。
- `query/test` 目录用于兼容当前验证流程；如果只需要训练集，可使用 `--split-mode train_only`。

## 4. 依赖说明

数据裁剪脚本依赖 Pillow；训练代码依赖 PyTorch、torchvision、yacs、ignite 等常见 ReID 训练依赖。
