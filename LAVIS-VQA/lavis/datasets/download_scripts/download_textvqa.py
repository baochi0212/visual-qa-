import os
from pathlib import Path

from omegaconf import OmegaConf

from lavis.common.utils import (
    cleanup_dir,
    download_and_extract_archive,
    get_abs_path,
    get_cache_path,
)


DATA_URL = "https://dl.fbaipublicfiles.com/textvqa/images/train_val_images.zip"


def download_datasets(root, url):
    download_and_extract_archive(url=url, download_root=root, extract_root=storage_dir)


if __name__ == "__main__":

    config_path = get_abs_path("configs/datasets/textvqa/defaults_vqa.yaml")

    storage_dir = OmegaConf.load(
        config_path
    ).datasets.text_vqa.build_info.images.storage

    download_dir = Path(get_cache_path(storage_dir)).parent / "download"
    storage_dir = Path(get_cache_path(storage_dir))

    if storage_dir.exists():
        print(f"Dataset already exists at {storage_dir}. Aborting.")
        exit(0)

    try:
        print("Downloading {}".format(DATA_URL))
        download_datasets(download_dir, DATA_URL)
    except Exception as e:
        # remove download dir if failed
        cleanup_dir(download_dir)
        print("Failed to download or extracting datasets. Aborting.")

    cleanup_dir(download_dir)
