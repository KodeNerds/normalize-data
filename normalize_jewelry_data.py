import pandas as pd
from pathlib import Path
from typing import List

# Define a mapping of vendor-specific fields to unified WooCommerce fields
FIELD_MAPPING = {
    "Ray-ID": ["Ray-ID"],
    "Item #": ["Sku", "Item #", "style", "sku"],
    "Status": ["Status"],
    "MSRP": ["MSRP"],
    "Regular Price": ["Price", "goldprice", "price", "Regular Price"],
    "Sales Price": ["Sales Price"],
    "UPC": ["UPC"],
    "Short description": ["Description", "name", "product_name", "Short description"],
    "Description": ["description", "long description ", "ShortDescription", "Description"],
    "Item Weight": ["Weight", "metalWeight"],
    "Item UOM": ["Item UOM"],
    "Sell UOM": ["Sell UOM"],
    "Size": ["RingSize", "FingerSize"],
    "Width": ["Width (mm)", "Top Width (mm)", "Width"],
    "Manufacturer": ["Manufacturer"],
    "Collection": ["Collection"],
    "Category": ["category", "Category"],
    "Sub Categroy": ["subcat", "MerchandisingCategory2"],
    "In-Stock": ["OnHand", "In-Stock"],
    "Availability": ["availability", "Availability", "Status"],
    "Style": ["GroupDescription", "style"],
    "Metal type": ["metaltype", "Metal", "metal"],
    "Metal quality": ["QualityCatalogValue", "Metal Long Desc"],
    "Metal Weight": ["metalWeight"],
    "Center stone": ["Center stone"],
    "Halo": ["Halo"],
    "Hidden Halo": ["Hidden Halo"],
    "Accent stone": ["stones", "Accent stone"],
    "Shape": ["Primary Stone Shape", "shape1", "CenterShape"],
    "Carat": ["carat_weight", "Carat", "TotalDiamondWeight"],
    "Diamond type": ["Diamond type"],
    "Diamond color": ["DiamondColor", "color1", "metalcolor"],
    "Diamond clarity": ["DiamondClarity", "clarity1", "DiamondClarity1"],
    "Diamond Cut": ["Diamond Cut"],
    "Diamond Report": ["Diamond Report"],
    "Gemstone type": ["Primary Stone Type", "GemstoneType1"],
    "Gemstone color": ["Gemstone color"],
    "Stone Setting": ["Stone Setting", "Setting Type"],
    "Stone Weight": ["Stone Weight", "weight1"],
    "Center stone included": ["Center Stone Included"],
    "Shipping": ["Shipping", "shippingDay"],
    "Image Link": ["FullySetImage1", "default_image_url", "image", "Image Link"],
    "Image Link2": ["Image2", "image1"],
    "Image Link3": ["Image3"],
    "Image Link4": ["GroupImage1"],
    "Image Link5": ["GroupImage2"],
    "Image Link6": ["GroupImage3"],
    "Image Link7": [],
    "Image Link8": [],
    "Image Link9": [],
    "Image Link10": [],
    "Image Link11": [],
    "Image Link12": [],
    "Image Link13": [],
    "Image Link14": [],
    "Image Link15": [],
    "VideoURL": ["Video", "videourl"]
}

# Helper function to get the matching column name
def get_column(df_columns: List[str], possible_names: List[str]) -> str:
    for name in possible_names:
        for col in df_columns:
            if col.strip().lower() == name.strip().lower():
                return col
    return None

# Normalize one file
def normalize_file(filepath: str, vendor_name: str = "") -> pd.DataFrame:
    ext = Path(filepath).suffix.lower()
    if ext == ".csv":
        df = pd.read_csv(filepath)
    elif ext in [".xls", ".xlsx"]:
        df = pd.read_excel(filepath)
    else:
        raise ValueError("Unsupported file format: " + filepath)

    norm = {}
    for unified_field, possible_fields in FIELD_MAPPING.items():
        col = get_column(df.columns, possible_fields)
        norm[unified_field] = df[col] if col else ""

    norm_df = pd.DataFrame(norm)
    if "Manufacturer" not in norm_df.columns:
        norm_df["Manufacturer"] = vendor_name

    return norm_df
