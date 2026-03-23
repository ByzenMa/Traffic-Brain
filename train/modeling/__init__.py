# encoding: utf-8
"""
@author:  sherlock
@contact: sherlockliao01@gmail.com
"""

from .baseline import Baseline
from .baseline_modular import ConfigurableBaseline


def build_model(cfg, num_classes):
    # if cfg.MODEL.NAME == 'resnet50':
    #     model = Baseline(num_classes, cfg.MODEL.LAST_STRIDE, cfg.MODEL.PRETRAIN_PATH, cfg.MODEL.NECK, cfg.TEST.NECK_FEAT)
    use_modular_model = any([
        cfg.MODEL.MODULES.USE_MSF,
        cfg.MODEL.MODULES.USE_RSCAMA,
        cfg.MODEL.MODULES.USE_TFF,
        cfg.MODEL.MODULES.USE_SFF,
    ])

    if use_modular_model:
        model = ConfigurableBaseline(
            num_classes,
            cfg.MODEL.LAST_STRIDE,
            cfg.MODEL.PRETRAIN_PATH,
            cfg.MODEL.NECK,
            cfg.TEST.NECK_FEAT,
            cfg.MODEL.NAME,
            cfg.MODEL.PRETRAIN_CHOICE,
            cfg,
        )
    else:
        model = Baseline(num_classes, cfg.MODEL.LAST_STRIDE, cfg.MODEL.PRETRAIN_PATH, cfg.MODEL.NECK, cfg.TEST.NECK_FEAT, cfg.MODEL.NAME, cfg.MODEL.PRETRAIN_CHOICE)
    return model
