import wbdata, pandas as pd, requests

INDICATORS = {
    "SP.POP.TOTL":    "population",
    "EN.POP.DNST":    "pop_density",
    "NY.GDP.MKTP.CD": "gdp",
    "NY.GDP.PCAP.CD": "gdp_pc",
    "AG.LND.TOTL.K2": "land_area",
}
YEAR = "2022"                     # 最新完整年

# ---------------- ① 指标数据 ----------------
wb_raw = wbdata.get_dataframe(
    INDICATORS, country="all", date=YEAR,
    parse_dates=False, keep_levels=True
).reset_index()                 # 有 'country' 和 'name' 两列

# ---- ①.1  国家元数据：英文名 ↔ ISO‑3 ----
meta = pd.DataFrame(wbdata.get_countries())           # 列：id name iso2Code ...
meta = meta[['name', 'id']].rename(columns={'id': 'iso3', 'name': 'country'})

# ---- ①.2  合并得到真正 ISO‑3 ----
wb_df = (wb_raw.merge(meta, on='country', how='left')
               .drop(columns=['date'])              # 只抓单一年份可删
               .rename(columns={'country': 'name_en'}))


# ② REST Countries 基础信息
rc = requests.get(
    "https://restcountries.com/v3.1/all?fields=name,cca3,region,latlng,area"
).json()

rc_df = (
    pd.json_normalize(rc)
      .loc[:, ["cca3", "name.common", "region", "latlng", "area"]]
      .rename(columns={
          "cca3": "iso3",
          "name.common": "name",
          "region": "continent",
          "area": "area_total_rest",
      })
)
rc_df["latitude"] = rc_df["latlng"].apply(
    lambda x: x[0] if isinstance(x, list) and x else None
)
rc_df = rc_df.drop(columns="latlng")

print(wb_df.columns) 
print(wb_df.head())  # ← 这里可以查看数据
print(rc_df.columns)
print(rc_df.head())  # ← 这里可以查看数据
# ③ 合并并保存
final = rc_df.merge(wb_df, on="iso3", how="left")
final.to_csv("global_stats_2022.csv", index=False, encoding="utf-8-sig")
print("Saved global_stats_2022.csv ✔")
