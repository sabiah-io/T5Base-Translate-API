# T5Base-Translate-API

A multilingual translation api built with the t5-base model from the T5 series.

T5-Base model documentation

Hugging face: [(https://huggingface.co/t5-base?text=My+name+is+Wolfgang+and+I+live+in+Berlin)]

Github: [(https://github.com/google-research/text-to-text-transfer-transformer)]

#### Docker

Pull image from repository

```
docker pull sabiah/translate
```

Run the image after pull complete while exposing the appropriate port (8000)

```
docker run -p 8000:80 --name t5base-translate translate
```

or to run it in the background

```
docker run -p 8000:80 --name t5base-translate -d translate
```

## Model Features

T5-Base is a text-to-text transformer model with the following features:

- **Model type:** Language model
- **Languages:** English, German, Romanian and French
- **Uses:**
  - machine translation
  - document summarization
  - question answering
  - and classification tasks e.g sentiment analysis

## Hardware Requirements

Hardware requirements for t5-base model inference

#### Memory

- **CPU:** Minimum 4GB; Recommended 8GB
- **GPU:** Minimum 2GB; Recommended 4GB

#### Processor

- **CPU:** Intel or AMD processor with 64-bit support; Minimum: 1.9 GHz; Recommended: 2.8 GHz or faster processor
- **GPU** nVidia GeForce GTX 1050 or equivalent; Recommended: nVidia GeForce GTX 1660 or Quadro T1000

#### Storage

Minimum 1GB of free disk space; Recommended 2GB or higher
