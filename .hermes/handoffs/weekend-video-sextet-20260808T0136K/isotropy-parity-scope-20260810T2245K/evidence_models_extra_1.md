# URL: https://zoobot.readthedocs.io/en/latest/pretrained_models.html

ContentsMenuExpandLight modeDark modeAuto light/dark mode

[Back to top](https://zoobot.readthedocs.io/en/latest/pretrained_models.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# Pretrained Models [\#](https://zoobot.readthedocs.io/en/latest/pretrained_models.html\#pretrained-models "Permalink to this heading")

## Loading Models [\#](https://zoobot.readthedocs.io/en/latest/pretrained_models.html\#loading-models "Permalink to this heading")

Pretrained models are available via HuggingFace (🤗) with

```
from zoobot.pytorch.training.finetune import FinetuneableZoobotClassifier
# or FinetuneableZoobotRegressor, or FinetuneableZoobotTree

model = FinetuneableZoobotClassifier(name='hf_hub:mwalmsley/zoobot-encoder-convnext_nano')
```

For more options (e.g. loading the `timm` encoder directly) see [Advanced Finetuning](https://zoobot.readthedocs.io/en/latest/guides/advanced_finetuning.html).

## Available Models [\#](https://zoobot.readthedocs.io/en/latest/pretrained_models.html\#available-models "Permalink to this heading")

Zoobot includes weights for the following pretrained models:

| Architecture | Parameters | Test loss | Finetune | HF 🤗 |
| --- | --- | --- | --- | --- |
| ConvNeXT-Pico | 9.1M | 19.33 | Yes | [Link](https://huggingface.co/mwalmsley/zoobot-encoder-convnext_pico) |
| ConvNeXT-Nano | 15.6M | 19.23 | Yes | [Link](https://huggingface.co/mwalmsley/zoobot-encoder-convnext_nano) |
| ConvNeXT-Tiny | 44.6M | 19.08 | Yes | [Link](https://huggingface.co/mwalmsley/zoobot-encoder-convnext_tiny) |
| ConvNeXT-Small | 58.5M | 19.06 | Yes | [Link](https://huggingface.co/mwalmsley/zoobot-encoder-convnext_small) |
| ConvNeXT-Base | 88.6M | **19.05** | Yes | [Link](https://huggingface.co/mwalmsley/zoobot-encoder-convnext_base) |
| ConvNeXT-Large | 197.8M | 19.09 | Yes | [Link](https://huggingface.co/mwalmsley/zoobot-encoder-convnext_large) |
| MaxViT-Tiny | 29.1M | 19.22 | Yes | [Link](https://huggingface.co/mwalmsley/zoobot-encoder-maxvit_rmlp_tiny_rw_224) |
| MaxViT-Small | 64.9M | 19.20 | Yes | [Link](https://huggingface.co/mwalmsley/zoobot-encoder-maxvit_rmlp_small_rw_224) |
| MaxViT-Base | 124.5 | 19.09 | Yes | [Link](https://huggingface.co/mwalmsley/zoobot-encoder-maxvit_base_rw_224) |
| Max-ViT-Large | 211.8M | 19.18 | Yes | [Link](https://huggingface.co/mwalmsley/zoobot-encoder-maxvit_large_tf_224) |
| EfficientNetB0 | 5.33M | 19.48 | Yes | WIP |
| EfficientNetV2-S | 48.3M | 19.33 | Yes | WIP |
| ResNet18 | 11.7M | 19.83 | Yes | [Link](https://huggingface.co/mwalmsley/zoobot-encoder-resnet18) |
| ResNet50 | 25.6M | 19.43 | Yes | [Link](https://huggingface.co/mwalmsley/zoobot-encoder-resnet50) |
| ResNet101 | 44.5M | 19.37 | Yes | [Link](https://huggingface.co/mwalmsley/zoobot-encoder-resnet101) |

Note

Missing a model you need? Reach out! There’s a good chance we can train any model supported by [timm](https://github.com/huggingface/pytorch-image-models).

Note

New in Zoobot v2.0.1: greyscale (single channel) versions are available [here](https://huggingface.co/collections/mwalmsley/zoobot-encoders-greyscale-66427c51133285ca01b490c6).

## Which model should I use? [\#](https://zoobot.readthedocs.io/en/latest/pretrained_models.html\#which-model-should-i-use "Permalink to this heading")

We suggest starting with ConvNeXT-Nano for most users.
ConvNeXT-Nano performs very well while still being small enough to train on a single gaming GPU.
You will be able to experiment quickly.

For maximum performance, you could swap ConvNeXT-Nano for ConvNeXT-Small or ConvNeXT-Base.
MaxViT-Base also performs well and includes an ingenious attention mechanism, if you’re interested in that.
All these models are much larger and need cluster-grade GPUs (e.g. V100 or above).

Other models are included for reference or as benchmarks.
EfficientNetB0 is equivalent to the model used in the GZ DECaLS and GZ DESI papers.
ResNet18 and ResNet50 are classics of the genre and may be useful for comparison or as part of other frameworks (like as an [object detection backbone](https://arxiv.org/abs/2312.03503)).

## How were the models trained? [\#](https://zoobot.readthedocs.io/en/latest/pretrained_models.html\#how-were-the-models-trained "Permalink to this heading")

The models were trained as part of the report [Scaling Laws for Galaxy Images](https://zoobot.readthedocs.io/en/latest/TODO).
This report systematically investigates how increasing labelled galaxy data and model size improves performance
and leads to adaptable models that generalise well to new tasks and new telescopes.

All models are trained on the GZ Evo dataset,
which includes 820k images and 100M+ volunteer votes drawn from every major Galaxy Zoo campaign: GZ2, GZ UKIDSS (unpublished), GZ Hubble, GZ CANDELS, GZ DECaLS/DESI, and GZ Cosmic Dawn (HSC, in prep.).
They learn an adaptable representation of galaxy images by training to answer every Galaxy Zoo question at once.

Versions**[latest](https://zoobot.readthedocs.io/en/latest/pretrained_models.html)**On Read the Docs[Project Home](https://app.readthedocs.org/projects/zoobot/?utm_source=zoobot&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/zoobot/builds/?utm_source=zoobot&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=zoobot&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=zoobot&utm_content=flyout)