# DataFeaturization.py

from matminer.datasets.convenience_loaders import load_elastic_tensor
from matminer.featurizers.conversions import (
    StrToComposition,
    CompositionToOxidComposition
)
from matminer.featurizers.composition import (
    ElementProperty,
    OxidationStates
)
from matminer.featurizers.structure import DensityFeatures


def build_features(save_path="data/elastic_features.pkl"):
    """
    Load elastic tensor dataset, perform feature engineering,
    and save featurized DataFrame.
    """

    # =========================
    # 1. Load dataset
    # =========================
    df = load_elastic_tensor()

    unwanted_columns = [
        "volume", "nsites",
        "compliance_tensor", "elastic_tensor",
        "elastic_tensor_original",
        "K_Voigt", "G_Voigt",
        "K_Reuss", "G_Reuss"
    ]
    df = df.drop(columns=unwanted_columns)

    # =========================
    # 2. Composition features
    # =========================
    df = StrToComposition().featurize_dataframe(df, "formula", ignore_errors=True)

    ep_feat = ElementProperty.from_preset("magpie")
    df = ep_feat.featurize_dataframe(df, "composition", ignore_errors=True)

    df = CompositionToOxidComposition().featurize_dataframe(df, "composition", ignore_errors=True)

    df = OxidationStates().featurize_dataframe(df, "composition_oxid", ignore_errors=True)

    density_feat = DensityFeatures()
    df = density_feat.featurize_dataframe(
        df, "structure", ignore_errors=True
    )

    df.to_pickle(save_path)
    print(f"[INFO] Features saved to {save_path}")

    return df


if __name__ == "__main__":
    build_features()
