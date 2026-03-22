#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CHECKPOINT_PATH="${ROOT_DIR}/outputs/crtrack_reid/resnet50_checkpoint_6900.pt"

cd "${ROOT_DIR}/train"

python3 tools/test.py \
  --config_file='configs/softmax_triplet.yml' \
  MODEL.NAME "('resnet50')" \
  DATASETS.NAMES "('CRTrack')" \
  DATASETS.ROOT_DIR "('..')" \
  TEST.WEIGHT "('${CHECKPOINT_PATH}')" \
  OUTPUT_DIR "('../outputs/crtrack_reid_test')"
